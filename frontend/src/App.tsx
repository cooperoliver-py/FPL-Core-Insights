import { lazy, Suspense, useCallback, useEffect, useRef, useState } from 'react';
import type { FormEvent } from 'react';
import { NavLink, Navigate, Route, Routes, useLocation, useSearchParams } from 'react-router-dom';
import { Activity, ArrowUpRight, Check, ChevronDown, Download, LogOut, RefreshCw, Users, X } from 'lucide-react';
import { z } from 'zod';
import { ApiError, authClient, download, request, workspaceRequest } from './api';
import { applyTransfer, fingerprint, localTime, previewSchema, saveSchema, squadSchema, workspaceSchema } from './domain';
import type { Analysis, Preview, Snapshot, Squad, Transfer, Workspace } from './domain';
import { Dialog, Icon, PlayerDetails, SnapshotStatus, useMobile } from './components';
import { Team, TeamEditor } from './Team';
import Players from './Players';
const Model = lazy(() => import('./Model'));
const emptySquad: Squad = { bank: 0, players: [], excluded_player_codes: [] };
const jobRecoverySchema = z.object({ owner: z.string(), revision: z.number(), snapshot: z.string(), signature: z.string(), id: z.string() });
const recoverSchema = z.object({ owner: z.string(), revision: z.number(), draft: squadSchema.extend({ players: z.array(squadSchema.shape.players.element).max(15) }) });

type Calculation = { kind: 'idle' } | { kind: 'pending'; id: string; signature: string; snapshot: Snapshot; revision: number } | { kind: 'ready'; preview: Preview; analysis: Analysis; signature: string; snapshot: Snapshot; revision: number };
function message(error: unknown): string { if (error instanceof ApiError && error.status === 401) return 'Your sign-in expired. Sign out and sign in again.'; if (error instanceof TypeError) return navigator.onLine === false ? 'You’re offline. Reconnect and reload the workspace.' : 'Cannot reach the analysis service. Try reloading in a moment.'; return error instanceof z.ZodError ? `Check your team: ${error.issues[0]?.message || 'invalid data'}` : error instanceof Error ? error.message : 'Something went wrong. Try again.'; }
function clearRecovery(key: string) { try { sessionStorage.removeItem(key); } catch { /* Storage may be disabled. */ } }
function Skeleton() { return <div className="loading-skeleton" aria-label="Loading FPML" role="status"><div/><div/><div/><div/><span className="caption">Connecting to analysis…</span></div>; }

function Login({ onSignedIn }: { onSignedIn: () => void }) {
  const [email, setEmail] = useState(''); const [password, setPassword] = useState(''); const [error, setError] = useState(''); const [busy, setBusy] = useState(false);
  async function submit(event: FormEvent) { event.preventDefault(); if (!authClient || busy) return; setBusy(true); setError(''); const result = await authClient.auth.signInWithPassword({ email, password }); setBusy(false); if (result.error) setError(result.error.message); else onSignedIn(); }
  return <main className="login-page"><div className="login-brand">FPML<span className="brand-bars" aria-hidden="true"><i/><i/><i/><i/><i/></span></div><form className="login-form" onSubmit={submit}><h1>Sign in to FPML</h1><p>Your personal FPL workspace.</p><label>Email<input type="email" name="email" autoComplete="username" required value={email} onChange={e => setEmail(e.target.value)}/></label><label>Password<input type="password" name="password" autoComplete="current-password" required value={password} onChange={e => setPassword(e.target.value)}/></label>{error && <p role="alert" className="error-text">{error}</p>}<button className="primary full" disabled={busy}>{busy ? 'Signing in…' : 'Sign in'}</button><p className="caption">A personal workspace. No public signup.</p></form></main>;
}

export default function App() {
  const [token, setToken] = useState<string | null>(null);
  const [owner, setOwner] = useState('local');
  const [authReady, setAuthReady] = useState(!authClient);
  const [signedIn, setSignedIn] = useState(!authClient);
  const [workspace, setWorkspace] = useState<Workspace | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [notice, setNotice] = useState('');
  const [draft, setDraft] = useState<Squad | null>(null);
  const [calculation, setCalculation] = useState<Calculation>({ kind: 'idle' });
  const [previousResult, setPreviousResult] = useState<Extract<Calculation, { kind: 'ready' }> | null>(null);
  const [transferReview, setTransferReview] = useState<Transfer | null>(null);
  const [saving, setSaving] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [discardConfirm, setDiscardConfirm] = useState(false);
  const [params, setParams] = useSearchParams();
  const editor = params.get('edit') === '1';
  const fixtureMode = import.meta.env.DEV ? params.get('fixture') : null;
  function setEditor(open: boolean) {
    setParams(previous => { const next = new URLSearchParams(previous); if (open) next.set('edit', '1'); else next.delete('edit'); return next; }, { replace: !open });
  }
  const location = useLocation(); const mobile = useMobile();
  const loadController = useRef<AbortController | null>(null);
  const requestVersion = useRef(0);
  const workspaceVersion = useRef(0);
  const activeOwner = useRef('local');
  const activeToken = useRef<string | null>(null);
  const restored = useRef(false);
  const positions = useRef(new Map<string, number>());
  const routeQueries = useRef(new Map<string, string>());
  useEffect(() => {
    if (!authClient) return;
    let live = true;
    const apply = (session: { access_token: string; user: { id: string } } | null) => {
      if (!live) return;
      const nextOwner = session?.user.id || '';
      const nextToken = session?.access_token || null;
      if (nextToken !== activeToken.current || nextOwner !== activeOwner.current) workspaceVersion.current += 1;
      activeToken.current = nextToken;
      if (nextOwner !== activeOwner.current) {
        activeOwner.current = nextOwner;
        requestVersion.current += 1;
        setPreviousResult(null); setWorkspace(null); setDraft(null); setCalculation({ kind: 'idle' }); restored.current = false;
      }
      setToken(session?.access_token || null); setOwner(nextOwner); setSignedIn(Boolean(session)); setAuthReady(true);
    };
    void authClient.auth.getSession().then(result => apply(result.data.session));
    const { data } = authClient.auth.onAuthStateChange((_event, session) => apply(session));
    return () => { live = false; data.subscription.unsubscribe(); };
  }, []);
  const load = useCallback(async (signal?: AbortSignal) => {
    const version = ++workspaceVersion.current;
    loadController.current?.abort();
    const controller = new AbortController();
    loadController.current = controller;
    const abort = () => controller.abort();
    signal?.addEventListener('abort', abort, { once: true });
    if (signal?.aborted) controller.abort();
    setLoading(true); setError('');
    try {
      let data = await workspaceRequest('/api/workspace', workspaceSchema, token, controller.signal);
      if (import.meta.env.DEV) {
        const { fixtureWorkspace } = await import('./fixtures');
        data = fixtureWorkspace(data, new URLSearchParams(window.location.search).get('fixture'));
      }
      if (version !== workspaceVersion.current || controller.signal.aborted) return null;
      setWorkspace(data); setError(''); return data;
    } catch (reason) {
      if (version === workspaceVersion.current && !(reason instanceof DOMException && reason.name === 'AbortError')) setError(message(reason));
      return null;
    } finally { signal?.removeEventListener('abort', abort); if (version === workspaceVersion.current) setLoading(false); }
  }, [token]);
  useEffect(() => { if (!authReady || !signedIn) return; const controller = new AbortController(); void load(controller.signal); return () => controller.abort(); }, [authReady, signedIn, load]);
  useEffect(() => {
    if (!workspace || restored.current) return;
    restored.current = true;
    try { const job = sessionStorage.getItem('fpml-job-v1'); if (job) { const recoveredJob = jobRecoverySchema.parse(JSON.parse(job)); if (recoveredJob.owner === owner && recoveredJob.revision === (workspace.team?.revision || 0) && recoveredJob.snapshot === workspace.snapshot.id) { setCalculation({ kind: 'pending', id: recoveredJob.id, signature: recoveredJob.signature, snapshot: workspace.snapshot, revision: recoveredJob.revision }); setNotice('Resuming your calculation…'); } else { clearRecovery('fpml-job-v1'); setNotice('The team or forecast changed. Recalculate to update your preview.'); } } } catch { clearRecovery('fpml-job-v1'); }
    try { const raw = sessionStorage.getItem('fpml-draft-v1'); if (!raw) return; const recovered = recoverSchema.parse(JSON.parse(raw)); if (recovered.owner !== owner) return; setDraft(recovered.draft); if (!sessionStorage.getItem('fpml-job-v1')) setNotice(recovered.revision === (workspace.team?.revision || 0) ? 'Recovered your unsaved preview. Calculate before saving.' : 'Recovered a preview based on an older team. Review it before recalculating.'); } catch { clearRecovery('fpml-draft-v1'); }
  }, [workspace, owner]);
  useEffect(() => { try { if (draft) sessionStorage.setItem('fpml-draft-v1', JSON.stringify({ owner, revision: workspace?.team?.revision || 0, draft })); else if (restored.current) clearRecovery('fpml-draft-v1'); } catch { /* Editing remains available when browser storage is full or disabled. */ } }, [draft, owner, workspace?.team?.revision]);
  useEffect(() => {
    if (calculation.kind === 'idle') return;
    try { sessionStorage.setItem('fpml-job-v1', JSON.stringify({ owner, revision: calculation.revision, snapshot: calculation.snapshot.id, signature: calculation.signature, id: calculation.kind === 'pending' ? calculation.id : calculation.preview.id })); } catch { /* Calculations still work without session storage. */ }
  }, [calculation, owner]);
  useEffect(() => {
    const previous = positions.current.get(location.pathname) || 0;
    window.scrollTo(0, previous);
    return () => { positions.current.set(location.pathname, window.scrollY); };
  }, [location.pathname]);
  useEffect(() => { routeQueries.current.set(location.pathname, location.search); }, [location.pathname, location.search]);
  const dirty = Boolean(draft && (!workspace?.team || fingerprint(draft) !== fingerprint(workspace.team.squad)));
  useEffect(() => { if (!dirty) return; const warn = (event: BeforeUnloadEvent) => { event.preventDefault(); }; addEventListener('beforeunload', warn); return () => removeEventListener('beforeunload', warn); }, [dirty]);
  const rememberSavedAnalysis = useCallback((analysis: Analysis, revision: number) => {
    setWorkspace(current => current?.team && current.team.revision === revision && current.snapshot.id === analysis.snapshot_id && fingerprint(current.team.squad) === fingerprint(analysis.team) ? { ...current, analysis } : current);
  }, []);
  useEffect(() => {
    if (calculation.kind !== 'pending') return;
    let alive = true; let timer: ReturnType<typeof setTimeout>;
    async function poll() {
      try {
        const result = await request(`/api/previews/${calculation.kind === 'pending' ? calculation.id : ''}`, previewSchema, token);
        if (!alive || calculation.kind !== 'pending') return;
        if (result.status === 'completed' && result.analysis) { rememberSavedAnalysis(result.analysis, calculation.revision); setCalculation({ kind: 'ready', preview: result, analysis: result.analysis, signature: calculation.signature, snapshot: calculation.snapshot, revision: calculation.revision }); setNotice('Calculation ready. Your saved squad is unchanged.'); setError(''); }
        else if (result.status === 'failed' || result.status === 'interrupted') { clearRecovery('fpml-job-v1'); setCalculation({ kind: 'idle' }); setError(result.error || 'Calculation interrupted. Try again.'); }
        else timer = setTimeout(poll, 1000);
      } catch (reason) { if (alive) { setCalculation({ kind: 'idle' }); setError(`${message(reason)} Your draft is still here. Calculate again to retry.`); } }
    }
    timer = setTimeout(poll, 500);
    return () => { alive = false; clearTimeout(timer); };
  }, [calculation, token, rememberSavedAnalysis]);

  const snapshot = workspace?.snapshot;
  const gwParam = Number(params.get('gw'));
  const gw = snapshot?.gameweeks.includes(gwParam) ? gwParam : snapshot?.gameweeks[0] || 1;
  const displayedResult = calculation.kind === 'ready' ? calculation : previousResult;
  const teamSnapshot = displayedResult?.snapshot || snapshot;
  const detailSnapshot = location.pathname === '/team' ? teamSnapshot : snapshot;
  const selected = detailSnapshot?.players.find(player => player.player_code === Number(params.get('player')));
  const savedAnalysis = workspace?.analysis && workspace.analysis.snapshot_id === snapshot?.id ? workspace.analysis : null;
  const activeAnalysis = displayedResult?.analysis || savedAnalysis;
  const currentSquad = draft || workspace?.team?.squad || null;
  const readyToSave = dirty && calculation.kind === 'ready' && draft && fingerprint(draft) === calculation.signature && calculation.analysis.snapshot_id === snapshot?.id && calculation.revision === (workspace?.team?.revision || 0);
  const busy = submitting || calculation.kind === 'pending';
  const stalePreview = Boolean(dirty && (!readyToSave || busy));
  const selectPlayer = (id: number) => setParams(previous => { const next = new URLSearchParams(previous); next.set('player', String(id)); return next; });
  const closePlayer = () => setParams(previous => { const next = new URLSearchParams(previous); next.delete('player'); return next; }, { replace: true });
  function update(next: Squad) { if (saving) return; requestVersion.current += 1; setDraft(next); setNotice(''); }
  function edit() { if (saving) return; if (!draft) update(workspace?.team?.squad || emptySquad); setEditor(true); }
  function closeEditor() { setEditor(false); if (!dirty) setDraft(null); }
  async function calculate(saved = false) {
    const candidate = saved ? workspace?.team?.squad : draft;
    if (!workspace || !candidate || busy) return;
    if (saved && dirty) { setError('Calculate or discard your preview before recalculating the saved team.'); return; }
    if (fixtureMode) { setError('Exit the development fixture before calculating or saving a real team.'); return; }
    const form = document.getElementById('team-editor');
    if (form instanceof HTMLFormElement && !form.reportValidity()) return;
    const parsed = squadSchema.safeParse(candidate);
    if (!parsed.success) { const missing = 15 - candidate.players.length; setError(missing > 0 ? `Add ${missing} ${missing === 1 ? 'player' : 'players'} to complete your 15-player squad.` : message(parsed.error)); return; }
    const version = ++requestVersion.current;
    const signature = fingerprint(parsed.data);
    setError(''); setSubmitting(true);
    try {
      const result = await request(saved ? '/api/analysis' : '/api/previews', previewSchema, token, { method: 'POST', body: JSON.stringify({ snapshot_id: workspace.snapshot.id, revision: workspace.team?.revision || 0, ...(saved ? {} : { draft: parsed.data }) }) });
      if (version !== requestVersion.current) return;
      if (result.status === 'completed' && result.analysis) rememberSavedAnalysis(result.analysis, workspace.team?.revision || 0);
      if (calculation.kind === 'ready') setPreviousResult(calculation);
      setCalculation(result.status === 'completed' && result.analysis ? { kind: 'ready', preview: result, analysis: result.analysis, signature, snapshot: workspace.snapshot, revision: workspace.team?.revision || 0 } : { kind: 'pending', id: result.id, signature, snapshot: workspace.snapshot, revision: workspace.team?.revision || 0 }); setEditor(false);
    } catch (reason) { setError(message(reason)); if (reason instanceof ApiError && reason.status === 409) { setCalculation({ kind: 'idle' }); await load(); setError(message(reason)); } }
    finally { setSubmitting(false); }
  }
  function previewTransfer(transfer: Transfer) {
    if (!activeAnalysis) return;
    if (draft && fingerprint(draft) !== fingerprint(activeAnalysis.team)) { setError('Calculate your current edits before previewing another transfer. Your draft is unchanged.'); return; }
    try { update(applyTransfer(activeAnalysis.team, transfer)); closePlayer(); setTransferReview(transfer); setNotice(''); } catch (reason) { setError(message(reason)); }
  }
  async function save() {
    if (!readyToSave || calculation.kind !== 'ready' || !workspace || saving || fixtureMode) return;
    const version = requestVersion.current;
    workspaceVersion.current += 1;
    setSaving(true); setError('');
    try { const result = await request('/api/team', saveSchema, token, { method: 'PUT', body: JSON.stringify({ preview_id: calculation.preview.id, revision: workspace.team?.revision || 0 }) }); if (version !== requestVersion.current) return; workspaceVersion.current += 1; setLoading(false); setWorkspace({ ...workspace, ...result }); setDraft(null); setPreviousResult(null); clearRecovery('fpml-job-v1'); setCalculation({ kind: 'idle' }); setNotice('Current team saved. Available on your other devices.'); }
    catch (reason) { if (version !== requestVersion.current) return; setError(message(reason)); if (reason instanceof ApiError && reason.status === 409) { setCalculation({ kind: 'idle' }); await load(); setError(message(reason)); } }
    finally { setSaving(false); }
  }
  function discard() { requestVersion.current += 1; setPreviousResult(null); clearRecovery('fpml-job-v1'); setDraft(null); setCalculation({ kind: 'idle' }); setDiscardConfirm(false); setEditor(false); setError(''); setNotice('Preview discarded.'); }
  async function exportFile(format: 'json' | 'csv' | 'md') { try { await download(format, token, format !== 'json' && calculation.kind === 'ready' ? calculation.preview.id : undefined); } catch (reason) { setError(message(reason)); } }
  const importSquad = (text: string) => { const data: unknown = JSON.parse(text); update(squadSchema.parse(data)); };
  function toggleExclude() { if (!selected) return; const base = draft || workspace?.team?.squad; if (!base) { edit(); return; } const codes = new Set(base.excluded_player_codes); if (codes.has(selected.player_code)) codes.delete(selected.player_code); else codes.add(selected.player_code); update({ ...base, excluded_player_codes: [...codes] }); setNotice('Exclusions changed in your preview. Calculate before saving.'); }
  const detail = selected && detailSnapshot ? <PlayerDetails player={selected} snapshot={detailSnapshot} gw={gw} owned={Boolean(workspace?.team?.squad.players.some(p => p.player_code === selected.player_code))} previewStatus={dirty && draft?.players.some(p => p.player_code === selected.player_code) && !workspace?.team?.squad.players.some(p => p.player_code === selected.player_code) ? 'incoming' : dirty && !draft?.players.some(p => p.player_code === selected.player_code) && workspace?.team?.squad.players.some(p => p.player_code === selected.player_code) ? 'outgoing' : undefined} excluded={Boolean(currentSquad?.excluded_player_codes.includes(selected.player_code))} onExclude={toggleExclude} close={closePlayer}/> : null;
  if (!authReady) return <Skeleton/>;
  if (!signedIn) return <Login onSignedIn={() => setNotice('Signed in.')}/>;
  return <div className={dirty ? 'app has-draft' : 'app'}>
    <a className="skip-link" href="#main">Skip to content</a>
    <header className="app-header"><NavLink className="wordmark" to="/team" aria-label="FPML Team">FPML<span className="brand-bars" aria-hidden="true"><i/><i/><i/><i/><i/></span></NavLink>
      <nav className="main-nav" aria-label="Main navigation">{[{ path: '/team', label: 'Team', icon: <Users size={18}/> }, { path: '/players', label: 'Players', icon: <ArrowUpRight size={18}/> }, { path: '/model', label: 'Model', icon: <Activity size={18}/> }].map(item => <NavLink key={item.path} to={`${item.path}${item.path === location.pathname ? location.search : routeQueries.current.get(item.path) || `?gw=${gw}`}`}><Icon>{item.icon}</Icon>{item.label}</NavLink>)}</nav>
      <div className="header-actions"><span className="private-label">Personal workspace</span><details className="download-menu"><summary aria-label="Downloads"><Download size={18}/><ChevronDown size={12}/></summary><div><button onClick={() => void exportFile('json')}>Saved squad JSON</button><button onClick={() => void exportFile('csv')}>{calculation.kind === 'ready' ? 'Displayed analysis CSV' : 'Saved analysis CSV'}</button><button onClick={() => void exportFile('md')}>{calculation.kind === 'ready' ? 'Displayed analysis report' : 'Saved analysis report'}</button></div></details>{authClient && <button className="icon-button" aria-label="Sign out" onClick={() => void authClient?.auth.signOut()}><LogOut size={17}/></button>}</div>
    </header>
    <main id="main" tabIndex={-1}>
      {snapshot && <div className="workspace-toolbar"><div><SnapshotStatus snapshot={snapshot}/>{snapshot.deadline && <span className="caption">Deadline {localTime(snapshot.deadline)}</span>}</div><div className="gameweek-switch" role="group" aria-label="Forecast Gameweek">{snapshot.gameweeks.map(week => <button key={week} aria-pressed={gw === week} onClick={() => setParams(previous => { const next = new URLSearchParams(previous); next.set('gw', String(week)); return next; })}>GW{week}</button>)}<button className="refresh-button" aria-label="Refresh forecasts" disabled={loading || saving} onClick={() => void load()}><RefreshCw size={15}/></button></div></div>}
      {import.meta.env.DEV && <details className="fixture-control"><summary>Development data{fixtureMode ? `: ${fixtureMode}` : ''}</summary><label>Dataset<select value={fixtureMode || ''} onChange={event => { const next = new URLSearchParams(params); if (event.target.value) next.set('fixture', event.target.value); else next.delete('fixture'); window.location.assign(`${location.pathname}?${next}`); }}><option value="">Real data</option><option value="worst">Difficult sample</option><option value="empty">Empty sample</option><option value="large">2,000 sample players</option></select></label>{fixtureMode && <p className="caption">Synthetic layout fixture. Saving is disabled.</p>}</details>}
      {loading && <button className="text-button" onClick={() => { loadController.current?.abort(); setNotice('Connection stopped. Reload the workspace to try again.'); }}>Stop connecting</button>}
      {loading && snapshot && <p className="calculation-status" role="status">Refreshing workspace… Temporary connection failures retry automatically.</p>}
      {error && <div className="error-banner" role="alert" tabIndex={-1}><p>{error}</p><button className="text-button" onClick={() => void load()}>Reload workspace</button><button className="icon-button" aria-label="Dismiss error" onClick={() => setError('')}><X size={16}/></button></div>}
      {notice && <div className="notice-banner" role="status"><Check size={16} aria-hidden="true"/><p>{notice}</p><button className="icon-button" aria-label="Dismiss notice" onClick={() => setNotice('')}><X size={16}/></button></div>}
      {displayedResult && displayedResult.snapshot.id !== snapshot?.id && <p className="notice">Displayed result uses the forecast from {localTime(displayedResult.snapshot.generated_at)}. Recalculate to use the latest forecast.</p>}
      {busy && <p className="calculation-status" role="status">Calculating… {previousResult || calculation.kind === 'ready' ? 'Showing the previous result. ' : ''}Your saved squad is unchanged.</p>}
      {dirty && !busy && stalePreview && <p className="calculation-status">Needs recalculation. {activeAnalysis ? 'Showing the last calculated lineup.' : 'Your changes have not been saved.'}</p>}
      {!snapshot ? <>{loading ? <Skeleton/> : <section className="empty-results"><h1>Workspace unavailable</h1><p>Check that the analysis service is running, then try again.</p><button className="primary" onClick={() => void load()}>Try again</button></section>}</> : <div className={detail && !mobile ? 'workspace-with-inspector' : ''}><div className="route-content"><Suspense fallback={<Skeleton/>}><Routes><Route path="/team" element={<Team snapshot={teamSnapshot || snapshot} analysis={activeAnalysis} savedSquad={workspace?.team?.squad || null} gw={teamSnapshot?.gameweeks.includes(gw) ? gw : teamSnapshot?.gameweeks[0] || gw} onPlayer={selectPlayer} onEdit={edit} onTransfer={previewTransfer} onRecalculate={() => void calculate(true)} recalcBusy={busy || dirty} isPreview={Boolean(dirty && displayedResult)}/>}/><Route path="/players" element={<Players snapshot={snapshot} squad={workspace?.team?.squad || null} previewSquad={dirty ? draft : null} gw={gw} onPlayer={selectPlayer}/>}/><Route path="/model" element={<Model snapshot={snapshot}/>}/><Route path="*" element={<Navigate to="/team" replace/>}/></Routes></Suspense></div>{detail && !mobile && <aside className="inspector">{detail}</aside>}</div>}
{dirty && draft && location.pathname === '/team' && <section className="preview-changes" aria-label="Preview changes"><strong>Preview changes</strong><p>{workspace?.team?.squad.players.filter(p => !draft.players.some(next => next.player_code === p.player_code)).map(p => snapshot?.players.find(player => player.player_code === p.player_code)?.web_name || String(p.player_code)).join(', ') || 'No players out'} → {draft.players.filter(p => !workspace?.team?.squad.players.some(saved => saved.player_code === p.player_code)).map(p => snapshot?.players.find(player => player.player_code === p.player_code)?.web_name || String(p.player_code)).join(', ') || 'No players in'}</p><p className="caption">Bank £{workspace?.team?.squad.bank.toFixed(1) || '0.0'}m → £{draft.bank.toFixed(1)}m · {draft.excluded_player_codes.length} excluded · {draft.players.filter(p => workspace?.team?.squad.players.find(saved => saved.player_code === p.player_code)?.purchase_price !== p.purchase_price).length} purchase prices changed</p></section>}
      <footer className="app-footer"><span>FPML</span><p>Predictions are estimates.</p>{workspace?.team && <span>Team saved {localTime(workspace.team.saved_at)}</span>}</footer>
    </main>
    {detail && mobile && !editor && <Dialog title={selected?.web_name || 'Player details'} close={closePlayer}>{detail}</Dialog>}
    {editor && draft && snapshot && <Dialog title="Edit your team" close={closeEditor}>{error && <p role="alert" className="error-text editor-error">{error}</p>}<TeamEditor draft={draft} snapshot={snapshot} update={update} importSquad={importSquad} calculate={() => void calculate()} busy={busy}/></Dialog>}
    {transferReview && <Dialog title="Review transfer" close={() => setTransferReview(null)}><div className="confirm-content"><p>{transferReview.out} → {transferReview.in}</p><p>Sell £{transferReview.selling_price.toFixed(1)}m · Buy £{transferReview.buy_price.toFixed(1)}m · Bank £{transferReview.bank_after.toFixed(1)}m</p><p className="caption">Hypothetical transfer. Your saved squad stays unchanged.</p><button className="secondary" onClick={() => { setTransferReview(null); edit(); }}>Adjust team or prices</button><button className="primary" disabled={busy} onClick={() => { setTransferReview(null); void calculate(); }}>Calculate transfer</button></div></Dialog>}
    {discardConfirm && <Dialog title="Discard this preview?" close={() => setDiscardConfirm(false)}><div className="confirm-content"><p>Your saved current team stays unchanged.</p><div><button className="secondary" onClick={() => setDiscardConfirm(false)}>Keep editing</button><button className="primary" onClick={discard}>Discard preview</button></div></div></Dialog>}

    {dirty && <div className={location.pathname === '/team' ? 'draft-bar' : 'draft-bar compact'}><div><span className="draft-dot"/><strong>{busy ? 'Calculating…' : readyToSave ? 'Preview ready' : 'Unsaved preview'}</strong><span className="draft-explanation">{readyToSave ? `${draft?.players.filter(p => !workspace?.team?.squad.players.some(saved => saved.player_code === p.player_code)).length || 0} incoming · Bank £${draft?.bank.toFixed(1)}m. Save after updating your actual team.` : 'Your current team is unchanged.'}</span></div><div><button className="text-button" disabled={saving} onClick={() => dirty ? setDiscardConfirm(true) : discard()}>Discard</button>{location.pathname !== '/team' ? <NavLink className="primary" to="/team">Review preview</NavLink> : readyToSave ? <button className="primary" disabled={saving} onClick={() => void save()}>{saving ? 'Saving…' : 'Save as current team'}</button> : <button className="primary" disabled={busy} onClick={() => void calculate()}>{busy ? 'Calculating…' : 'Calculate preview'}</button>}</div></div>}
  </div>;
}
