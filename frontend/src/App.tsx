import { lazy, Suspense, useCallback, useEffect, useRef, useState } from 'react';
import type { FormEvent } from 'react';
import { NavLink, Navigate, Route, Routes, useLocation, useSearchParams } from 'react-router-dom';
import { Activity, ArrowUpRight, Check, ChevronDown, Download, LogOut, RefreshCw, Users, X } from 'lucide-react';
import { z } from 'zod';
import { ApiError, authClient, download, request } from './api';
import { applyTransfer, fingerprint, localTime, previewSchema, saveSchema, squadSchema, workspaceSchema } from './domain';
import type { Analysis, Preview, Snapshot, Squad, Transfer, Workspace } from './domain';
import { Dialog, Icon, PlayerDetails, SnapshotStatus, useMobile } from './components';
import { Team, TeamEditor } from './Team';
import Players from './Players';
const Model = lazy(() => import('./Model'));
const emptySquad: Squad = { bank: 0, players: [], excluded_player_codes: [] };
const recoverSchema = z.object({ owner: z.string(), revision: z.number(), draft: squadSchema.extend({ players: z.array(squadSchema.shape.players.element).max(15) }) });

type Calculation = { kind: 'idle' } | { kind: 'pending'; id: string; signature: string; snapshot: Snapshot; revision: number } | { kind: 'ready'; preview: Preview; analysis: Analysis; signature: string; snapshot: Snapshot; revision: number };
function message(error: unknown): string { return error instanceof z.ZodError ? `Check your team: ${error.issues[0]?.message || 'invalid data'}` : error instanceof Error ? error.message : 'Something went wrong. Try again.'; }
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
        setWorkspace(null); setDraft(null); setCalculation({ kind: 'idle' }); restored.current = false;
      }
      setToken(session?.access_token || null); setOwner(nextOwner); setSignedIn(Boolean(session)); setAuthReady(true);
    };
    void authClient.auth.getSession().then(result => apply(result.data.session));
    const { data } = authClient.auth.onAuthStateChange((_event, session) => apply(session));
    return () => { live = false; data.subscription.unsubscribe(); };
  }, []);
  const load = useCallback(async (signal?: AbortSignal) => {
    const version = ++workspaceVersion.current;
    setLoading(true);
    try {
      let data = await request('/api/workspace', workspaceSchema, token, { signal });
      if (import.meta.env.DEV) {
        const { fixtureWorkspace } = await import('./fixtures');
        data = fixtureWorkspace(data, new URLSearchParams(window.location.search).get('fixture'));
      }
      if (version !== workspaceVersion.current || signal?.aborted) return null;
      setWorkspace(data); setError(''); return data;
    } catch (reason) {
      if (version === workspaceVersion.current && !(reason instanceof DOMException && reason.name === 'AbortError')) setError(message(reason));
      return null;
    } finally { if (version === workspaceVersion.current && !signal?.aborted) setLoading(false); }
  }, [token]);
  useEffect(() => { if (!authReady || !signedIn) return; const controller = new AbortController(); void load(controller.signal); return () => controller.abort(); }, [authReady, signedIn, load]);
  useEffect(() => {
    if (!workspace || restored.current) return;
    restored.current = true;
    try { const raw = sessionStorage.getItem('fpml-draft-v1'); if (!raw) return; const recovered = recoverSchema.parse(JSON.parse(raw)); if (recovered.owner !== owner) return; setDraft(recovered.draft); setNotice(recovered.revision === (workspace.team?.revision || 0) ? 'Recovered your unsaved preview. Calculate before saving.' : 'Recovered a preview based on an older team. Review it before recalculating.'); } catch { sessionStorage.removeItem('fpml-draft-v1'); }
  }, [workspace, owner]);
  useEffect(() => { try { if (draft) sessionStorage.setItem('fpml-draft-v1', JSON.stringify({ owner, revision: workspace?.team?.revision || 0, draft })); else if (restored.current) sessionStorage.removeItem('fpml-draft-v1'); } catch { /* Editing remains available when browser storage is full or disabled. */ } }, [draft, owner, workspace?.team?.revision]);
  useEffect(() => {
    const previous = positions.current.get(location.pathname) || 0;
    window.scrollTo(0, previous);
    return () => { positions.current.set(location.pathname, window.scrollY); };
  }, [location.pathname]);
  useEffect(() => { routeQueries.current.set(location.pathname, location.search); }, [location.pathname, location.search]);
  const dirty = Boolean(draft && (!workspace?.team || fingerprint(draft) !== fingerprint(workspace.team.squad)));
  useEffect(() => { if (!dirty) return; const warn = (event: BeforeUnloadEvent) => { event.preventDefault(); }; addEventListener('beforeunload', warn); return () => removeEventListener('beforeunload', warn); }, [dirty]);
  useEffect(() => {
    if (calculation.kind !== 'pending') return;
    let alive = true; let timer: ReturnType<typeof setTimeout>;
    async function poll() {
      try {
        const result = await request(`/api/previews/${calculation.kind === 'pending' ? calculation.id : ''}`, previewSchema, token);
        if (!alive || calculation.kind !== 'pending') return;
        if (result.status === 'completed' && result.analysis) { setCalculation({ kind: 'ready', preview: result, analysis: result.analysis, signature: calculation.signature, snapshot: calculation.snapshot, revision: calculation.revision }); setNotice('Preview calculated. Your saved team is unchanged.'); setError(''); }
        else if (result.status === 'failed' || result.status === 'interrupted') { setCalculation({ kind: 'idle' }); setError(result.error || 'Calculation interrupted. Try again.'); }
        else timer = setTimeout(poll, 1000);
      } catch (reason) { if (alive) { setCalculation({ kind: 'idle' }); setError(`${message(reason)} Your draft is still here. Calculate again to retry.`); } }
    }
    timer = setTimeout(poll, 500);
    return () => { alive = false; clearTimeout(timer); };
  }, [calculation, token]);

  const snapshot = workspace?.snapshot;
  const gwParam = Number(params.get('gw'));
  const gw = snapshot?.gameweeks.includes(gwParam) ? gwParam : snapshot?.gameweeks[0] || 1;
  const teamSnapshot = calculation.kind === 'ready' ? calculation.snapshot : snapshot;
  const detailSnapshot = location.pathname === '/team' ? teamSnapshot : snapshot;
  const selected = detailSnapshot?.players.find(player => player.player_code === Number(params.get('player')));
  const savedAnalysis = workspace?.analysis && workspace.analysis.snapshot_id === snapshot?.id ? workspace.analysis : null;
  const activeAnalysis = calculation.kind === 'ready' ? calculation.analysis : savedAnalysis;
  const currentSquad = draft || workspace?.team?.squad || null;
  const readyToSave = calculation.kind === 'ready' && draft && fingerprint(draft) === calculation.signature && calculation.analysis.snapshot_id === snapshot?.id && calculation.revision === (workspace?.team?.revision || 0);
  const busy = submitting || calculation.kind === 'pending';
  const stalePreview = Boolean(draft && (!readyToSave || busy));
  const selectPlayer = (id: number) => setParams(previous => { const next = new URLSearchParams(previous); next.set('player', String(id)); return next; });
  const closePlayer = () => setParams(previous => { const next = new URLSearchParams(previous); next.delete('player'); return next; }, { replace: true });
  function update(next: Squad) { if (saving) return; requestVersion.current += 1; setDraft(next); setNotice(''); }
  function edit() { if (saving) return; if (!draft) update(workspace?.team?.squad || emptySquad); setEditor(true); }
  function closeEditor() { setEditor(false); }
  async function calculate() {
    if (!workspace || !draft || busy) return;
    if (fixtureMode) { setError('Exit the development fixture before calculating or saving a real team.'); return; }
    const form = document.getElementById('team-editor');
    if (form instanceof HTMLFormElement && !form.reportValidity()) return;
    const parsed = squadSchema.safeParse(draft);
    if (!parsed.success) { setError(message(parsed.error)); return; }
    const version = ++requestVersion.current;
    const signature = fingerprint(parsed.data);
    setError(''); setSubmitting(true);
    try {
      const result = await request('/api/previews', previewSchema, token, { method: 'POST', body: JSON.stringify({ snapshot_id: workspace.snapshot.id, revision: workspace.team?.revision || 0, draft: parsed.data }) });
      if (version !== requestVersion.current) return;
      setCalculation(result.status === 'completed' && result.analysis ? { kind: 'ready', preview: result, analysis: result.analysis, signature, snapshot: workspace.snapshot, revision: workspace.team?.revision || 0 } : { kind: 'pending', id: result.id, signature, snapshot: workspace.snapshot, revision: workspace.team?.revision || 0 }); setEditor(false);
    } catch (reason) { setError(message(reason)); if (reason instanceof ApiError && reason.status === 409) { setCalculation({ kind: 'idle' }); await load(); setError(message(reason)); } }
    finally { setSubmitting(false); }
  }
  function previewTransfer(transfer: Transfer) {
    if (!activeAnalysis) return;
    if (draft && fingerprint(draft) !== fingerprint(activeAnalysis.team)) { setError('Calculate your current edits before previewing another transfer. Your draft is unchanged.'); return; }
    try { update(applyTransfer(activeAnalysis.team, transfer)); setParams(previous => { const next = new URLSearchParams(previous); next.set('edit', '1'); next.delete('player'); return next; }); setNotice('Transfer added to your preview. Check the prices and calculate.'); } catch (reason) { setError(message(reason)); }
  }
  async function save() {
    if (!readyToSave || calculation.kind !== 'ready' || !workspace || saving || fixtureMode) return;
    const version = requestVersion.current;
    workspaceVersion.current += 1;
    setSaving(true); setError('');
    try { const result = await request('/api/team', saveSchema, token, { method: 'PUT', body: JSON.stringify({ preview_id: calculation.preview.id, revision: workspace.team?.revision || 0 }) }); if (version !== requestVersion.current) return; workspaceVersion.current += 1; setLoading(false); setWorkspace({ ...workspace, ...result }); setDraft(null); setCalculation({ kind: 'idle' }); setNotice('Current team saved. Available on your other devices.'); }
    catch (reason) { if (version !== requestVersion.current) return; setError(message(reason)); if (reason instanceof ApiError && reason.status === 409) { setCalculation({ kind: 'idle' }); await load(); setError(message(reason)); } }
    finally { setSaving(false); }
  }
  function discard() { requestVersion.current += 1; setDraft(null); setCalculation({ kind: 'idle' }); setDiscardConfirm(false); setEditor(false); setError(''); setNotice('Preview discarded.'); }
  async function exportFile(format: 'json' | 'csv' | 'md') { try { await download(format, token); } catch (reason) { setError(message(reason)); } }
  const importSquad = (text: string) => { const data: unknown = JSON.parse(text); update(squadSchema.parse(data)); };
  function toggleExclude() { if (!selected) return; const base = draft || workspace?.team?.squad; if (!base) { edit(); return; } const codes = new Set(base.excluded_player_codes); if (codes.has(selected.player_code)) codes.delete(selected.player_code); else codes.add(selected.player_code); update({ ...base, excluded_player_codes: [...codes] }); setNotice('Exclusions changed in your preview. Calculate before saving.'); }
  const detail = selected && detailSnapshot ? <PlayerDetails player={selected} snapshot={detailSnapshot} gw={gw} owned={Boolean(currentSquad?.players.some(p => p.player_code === selected.player_code))} excluded={Boolean(currentSquad?.excluded_player_codes.includes(selected.player_code))} onExclude={toggleExclude} close={closePlayer}/> : null;
  if (!authReady) return <Skeleton/>;
  if (!signedIn) return <Login onSignedIn={() => setNotice('Signed in.')}/>;
  return <div className={draft ? 'app has-draft' : 'app'}>
    <a className="skip-link" href="#main">Skip to content</a>
    <header className="app-header"><NavLink className="wordmark" to="/team" aria-label="FPML Team">FPML<span className="brand-bars" aria-hidden="true"><i/><i/><i/><i/><i/></span></NavLink>
      <nav className="main-nav" aria-label="Main navigation">{[{ path: '/team', label: 'Team', icon: <Users size={18}/> }, { path: '/players', label: 'Players', icon: <ArrowUpRight size={18}/> }, { path: '/model', label: 'Model', icon: <Activity size={18}/> }].map(item => <NavLink key={item.path} to={`${item.path}${item.path === location.pathname ? location.search : routeQueries.current.get(item.path) || `?gw=${gw}`}`}><Icon>{item.icon}</Icon>{item.label}</NavLink>)}</nav>
      <div className="header-actions"><span className="private-label">Personal workspace</span><details className="download-menu"><summary aria-label="Downloads"><Download size={18}/><ChevronDown size={12}/></summary><div><button onClick={() => void exportFile('json')}>Squad JSON</button><button onClick={() => void exportFile('csv')}>Player CSV</button><button onClick={() => void exportFile('md')}>Full report</button></div></details>{authClient && <button className="icon-button" aria-label="Sign out" onClick={() => void authClient?.auth.signOut()}><LogOut size={17}/></button>}</div>
    </header>
    <main id="main" tabIndex={-1}>
      {snapshot && <div className="workspace-toolbar"><SnapshotStatus snapshot={snapshot}/><div className="gameweek-switch" role="group" aria-label="Forecast Gameweek">{snapshot.gameweeks.map(week => <button key={week} aria-pressed={gw === week} onClick={() => setParams(previous => { const next = new URLSearchParams(previous); next.set('gw', String(week)); return next; })}>GW{week}</button>)}<button className="refresh-button" aria-label="Refresh forecasts" disabled={loading || saving} onClick={() => void load()}><RefreshCw size={15}/></button></div></div>}
      {import.meta.env.DEV && <details className="fixture-control"><summary>Development data{fixtureMode ? `: ${fixtureMode}` : ''}</summary><label>Dataset<select value={fixtureMode || ''} onChange={event => { const next = new URLSearchParams(params); if (event.target.value) next.set('fixture', event.target.value); else next.delete('fixture'); window.location.assign(`${location.pathname}?${next}`); }}><option value="">Real data</option><option value="worst">Difficult sample</option><option value="empty">Empty sample</option><option value="large">2,000 sample players</option></select></label>{fixtureMode && <p className="caption">Synthetic layout fixture. Saving is disabled.</p>}</details>}
      {error && <div className="error-banner" role="alert" tabIndex={-1}><p>{error}</p><button className="text-button" onClick={() => void load()}>Reload workspace</button><button className="icon-button" aria-label="Dismiss error" onClick={() => setError('')}><X size={16}/></button></div>}
      {notice && <div className="notice-banner" role="status"><Check size={16} aria-hidden="true"/><p>{notice}</p><button className="icon-button" aria-label="Dismiss notice" onClick={() => setNotice('')}><X size={16}/></button></div>}
      {calculation.kind === 'ready' && calculation.snapshot.id !== snapshot?.id && <p className="notice">Preview uses the forecast from {localTime(calculation.snapshot.generated_at)}. Recalculate to use the latest forecast.</p>}
      {busy && <p className="calculation-status" role="status">Calculating your preview… Your saved team is unchanged.</p>}
      {draft && !busy && stalePreview && <p className="calculation-status">Needs recalculation. {activeAnalysis ? 'Showing the last calculated lineup.' : 'Your changes have not been saved.'}</p>}
      {!snapshot ? <>{loading ? <Skeleton/> : <section className="empty-results"><h1>Workspace unavailable</h1><p>Check that the analysis service is running, then try again.</p><button className="primary" onClick={() => void load()}>Try again</button></section>}</> : <div className={detail && !mobile ? 'workspace-with-inspector' : ''}><div className="route-content"><Suspense fallback={<Skeleton/>}><Routes><Route path="/team" element={<Team snapshot={teamSnapshot || snapshot} analysis={activeAnalysis} savedSquad={workspace?.team?.squad || null} gw={teamSnapshot?.gameweeks.includes(gw) ? gw : teamSnapshot?.gameweeks[0] || gw} onPlayer={selectPlayer} onEdit={edit} onTransfer={previewTransfer} isPreview={calculation.kind === 'ready'}/>}/><Route path="/players" element={<Players snapshot={snapshot} squad={currentSquad} gw={gw} onPlayer={selectPlayer}/>}/><Route path="/model" element={<Model snapshot={snapshot}/>}/><Route path="*" element={<Navigate to="/team" replace/>}/></Routes></Suspense></div>{detail && !mobile && <aside className="inspector">{detail}</aside>}</div>}
      <footer className="app-footer"><span>FPML</span><p>Predictions are estimates.</p>{workspace?.team && <span>Team saved {localTime(workspace.team.saved_at)}</span>}</footer>
    </main>
    {detail && mobile && !editor && <Dialog title={selected?.web_name || 'Player details'} close={closePlayer}>{detail}</Dialog>}
    {editor && draft && snapshot && <Dialog title="Edit your team" close={closeEditor}>{error && <p role="alert" className="error-text editor-error">{error}</p>}<TeamEditor draft={draft} snapshot={snapshot} update={update} importSquad={importSquad} calculate={() => void calculate()} busy={busy}/></Dialog>}
    {discardConfirm && <Dialog title="Discard this preview?" close={() => setDiscardConfirm(false)}><div className="confirm-content"><p>Your saved current team stays unchanged.</p><div><button className="secondary" onClick={() => setDiscardConfirm(false)}>Keep editing</button><button className="primary" onClick={discard}>Discard preview</button></div></div></Dialog>}
    {draft && <div className="draft-bar"><div><span className="draft-dot"/><strong>{busy ? 'Calculating…' : readyToSave ? 'Preview ready' : 'Unsaved preview'}</strong><span className="draft-explanation">{readyToSave ? 'Save only after updating your actual FPL team.' : 'Your current team is unchanged.'}</span></div><div><button className="text-button" disabled={saving} onClick={() => dirty ? setDiscardConfirm(true) : discard()}>Discard</button>{readyToSave ? <button className="primary" disabled={saving} onClick={() => void save()}>{saving ? 'Saving…' : 'Save as current team'}</button> : <button className="primary" disabled={busy} onClick={() => void calculate()}>{busy ? 'Calculating…' : 'Calculate preview'}</button>}</div></div>}
  </div>;
}
