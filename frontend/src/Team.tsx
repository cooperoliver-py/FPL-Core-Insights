import { useState } from 'react';
import { ArrowRight, ArrowUpRight, Check, Pencil, Plus, Upload, X } from 'lucide-react';
import { Disclosure, ForecastStrip, Gain, Help, Icon, SquadRows } from './components';
import { money, number, positionShort, sellingPrice } from './domain';
import type { Analysis, Player, Snapshot, Squad, Transfer } from './domain';

export function Team({ snapshot, analysis, savedSquad, gw, onPlayer, onEdit, onTransfer, isPreview }: { snapshot: Snapshot; analysis: Analysis | null; savedSquad: Squad | null; gw: number; onPlayer: (id: number) => void; onEdit: () => void; onTransfer: (transfer: Transfer) => void; isPreview: boolean }) {
  if (!analysis && savedSquad) return <>
    <header className="page-heading"><div><h1>Your team</h1><p>Your squad is saved. Calculate a preview for the latest forecasts.</p></div><button className="secondary" onClick={onEdit}><Icon><Pencil size={16}/></Icon>Edit team</button></header>
    <section className="lineup-section" aria-label="Saved squad">
      <div className="section-heading"><h2>Saved squad</h2><span>Bank {money(savedSquad.bank)}</span></div>
      <div className="table-scroll"><table><thead><tr><th>Player</th><th>Position</th><th>Paid</th></tr></thead><tbody>{savedSquad.players.map(holding => {
        const player = snapshot.players.find(p => p.player_code === holding.player_code);
        return <tr key={holding.player_code}><th scope="row">{player?.web_name || `Player ${holding.player_code}`}</th><td>{player?.position || 'Unavailable'}</td><td>{money(holding.purchase_price)}</td></tr>;
      })}</tbody></table></div>
      <button className="primary" onClick={onEdit}>Review and calculate</button>
    </section>
  </>;
  if (!analysis) return <section className="empty-team"><div className="empty-mark"><Plus size={30}/></div><h1>Your team, your next move.</h1><p>Add your current 15 players and bank to see your lineup and legal transfer options.</p><button className="primary" onClick={onEdit}>Set up your team</button><p className="caption">You can import your existing squad JSON in the editor.</p></section>;
  const lineup = analysis.current.lineups[String(gw)];
  const best = analysis.transfers[0];
  const incoming = best ? snapshot.players.find(p => p.player_code === best.in_player_code) : undefined;
  const caption = `${snapshot.gameweeks.length}-GW weighted XI + captain`;
  return <>
    <header className="page-heading"><div><h1>{isPreview ? 'Team preview' : 'Your team'}</h1><p>{snapshot.season.replace('-', '/')} <span className="text-divider"/> GW{gw} projected lineup</p></div><button className="secondary" onClick={onEdit}><Icon><Pencil size={16}/></Icon>Edit team</button></header>
    <div className="budget-bar"><div><span>Projected XI + captain</span><strong>{number(lineup?.points)}<small> pts</small></strong></div><div><span>Bank</span><strong>{money(analysis.budget.bank)}</strong></div><div><span>Selling value</span><strong>{money(analysis.budget.selling_value)}</strong></div><div><span>Available funds</span><strong>{money(analysis.budget.available)}</strong></div></div>
    <div className="team-layout"><section className="lineup-section"><div className="section-heading"><h2>Starting lineup</h2><span className="caption">GW{gw} forecast</span></div><SquadRows squad={analysis.current} excluded={analysis.team.excluded_player_codes} snapshot={snapshot} gw={gw} onPlayer={onPlayer}/></section>
      <aside className="decision-column"><section className="next-move"><div className="section-heading"><h2>Your next move</h2><span className="tag">One transfer</span></div>
        {analysis.hold || !best ? <><div className="hold-mark"><Check size={20}/></div><h3 className="move-title">Hold your team.</h3><p className="muted">No legal same-position transfer improves the projected XI + captain score.</p></> : <>
          <div className="transfer-pair"><div><span>Out</span><button className="text-button" onClick={() => onPlayer(best.out_player_code)}>{best.out}</button><small>{money(best.selling_price)} sell</small></div><ArrowRight size={22} aria-hidden="true"/><div><span>In</span><button className="text-button" onClick={() => onPlayer(best.in_player_code)}>{best.in}</button><small>{money(best.buy_price)} buy</small></div></div>
          {incoming && <ForecastStrip player={incoming} snapshot={snapshot} gw={gw}/>}
          <div className="move-gain"><Gain value={best.weighted_gain}/><span>Weighted {snapshot.gameweeks.length}-GW XI + captain gain <Help label="transfer gain">Improvement after selecting the best legal XI and captain each week, with the forecast horizon's discount weights. This is not the incoming player's raw points.</Help></span></div>
          <div className="bank-after"><span>Bank after</span><strong>{money(best.bank_after)}</strong></div><button className="primary full" onClick={() => onTransfer(best)}>Preview transfer<Icon><ArrowUpRight size={17}/></Icon></button>
        </>}
        <p className="caption">Suggestions only. FPML never submits changes to FPL.</p>
      </section>
      <Disclosure title={`Transfer options (${analysis.transfers.length})`}>
        {analysis.transfers.length ? <ol className="transfer-options">{analysis.transfers.map((option, index) => <li key={`${option.out_player_code}-${option.in_player_code}`}><div className="option-heading"><span>{index + 1}</span><div><strong>{option.out} <ArrowRight size={13} aria-label="to"/> {option.in}</strong><small>Sell {money(option.selling_price)} · Buy {money(option.buy_price)} · Bank {money(option.bank_after)}</small></div><Gain value={option.weighted_gain}/></div><button className="text-button" onClick={() => onTransfer(option)}>Preview this transfer</button></li>)}</ol> : <p>No legal same-position swaps are available within your funds.</p>}
      </Disclosure>
      <section className="comparison-summary"><div className="section-heading"><h2>Optimal comparison</h2><Help label="optimal comparison">The best affordable squad using your sale values and bank. It may need multiple transfers and is not the one-transfer recommendation.</Help></div><div className="comparison-numbers"><div><span>Your team</span><strong>{number(analysis.current.weighted_points)}</strong></div><ArrowRight size={20} aria-hidden="true"/><div><span>Optimal</span><strong>{number(analysis.optimal.weighted_points)}</strong></div></div><p className="caption">{caption}. May require multiple transfers.</p><Disclosure title="View optimal squad"><p className="caption">Affordable with {money(analysis.budget.optimal_bank)} bank remaining.</p><SquadRows squad={analysis.optimal} excluded={analysis.team.excluded_player_codes} snapshot={snapshot} gw={gw} onPlayer={onPlayer} compact/></Disclosure></section>
      <Disclosure title="Squad prices and budget"><p className="caption">Keeping an owned player does not require buying them back. Your market value is {money(analysis.budget.market_value)}.</p><div className="table-scroll"><table><thead><tr><th>Player</th><th>Paid</th><th>Sell</th><th>Now</th></tr></thead><tbody>{analysis.team.players.map(holding => { const player = snapshot.players.find(p => p.player_code === holding.player_code); if (!player) return null; const sale = sellingPrice(holding.purchase_price, player.now_cost); return <tr key={holding.player_code}><th scope="row">{player.web_name}</th><td>{money(holding.purchase_price)}</td><td>{money(sale)}</td><td>{money(player.now_cost)}</td></tr>; })}</tbody></table></div></Disclosure>
      </aside></div>
  </>;
}

export function TeamEditor({ draft, snapshot, update, importSquad, calculate, busy }: { draft: Squad; snapshot: Snapshot; update: (squad: Squad) => void; importSquad: (text: string) => void; calculate: () => void; busy: boolean }) {
  const [replacement, setReplacement] = useState<number | null>(null);
  const [search, setSearch] = useState('');
  const [importError, setImportError] = useState('');
  const catalog = new Map(snapshot.players.map(p => [p.player_code, p]));
  const current = replacement !== null ? catalog.get(replacement) : undefined;
  const candidates = snapshot.players.filter(p => (!current || p.position === current.position) && (!draft.players.some(h => h.player_code === p.player_code) || p.player_code === replacement) && `${p.web_name} ${p.first_name} ${p.second_name} ${p.team}`.toLowerCase().includes(search.toLowerCase())).slice(0, 30);
  function replace(player: Player) {
    if (replacement === null) return;
    update({ ...draft, players: replacement === 0 ? [...draft.players, { player_code: player.player_code, purchase_price: player.now_cost }] : draft.players.map(p => p.player_code === replacement ? { player_code: player.player_code, purchase_price: player.now_cost } : p) });
    setReplacement(null); setSearch('');
  }
  return <form id="team-editor" className="team-editor" onSubmit={event => { event.preventDefault(); calculate(); }}>
    <p className="editor-intro">Record your actual squad and prices. Calculate a preview before saving.</p>
    <div className="editor-toolbar"><label>Bank (£m)<input type="number" name="bank" min="0" step="0.1" inputMode="decimal" required value={Number.isFinite(draft.bank) ? draft.bank : ''} onChange={event => update({ ...draft, bank: event.target.valueAsNumber })}/></label><label className="file-button"><Upload size={16} aria-hidden="true"/> Import squad JSON<input type="file" accept=".json,application/json" onChange={async event => { const file = event.target.files?.[0]; if (!file) return; try { if (file.size > 50000) throw new Error('Choose a squad JSON file smaller than 50 KB.'); importSquad(await file.text()); setImportError(''); } catch (error) { setImportError(error instanceof Error ? error.message : 'Could not import this file.'); } event.target.value = ''; }}/></label></div>
    {importError && <p role="alert" className="error-text">{importError}</p>}
    <div className="editor-list"><div className="editor-list-header"><span>Player</span><span>Purchase (£m)</span></div>{draft.players.map(holding => { const p = catalog.get(holding.player_code); return <div className="editor-row" key={holding.player_code}><button type="button" className="editor-player" onClick={() => { setReplacement(holding.player_code); setSearch(''); }}><strong>{p?.web_name || `Player ${holding.player_code}`}</strong><span>{p?.team_short_name} · {p ? positionShort[p.position] : 'Unknown'} <Pencil size={12} aria-hidden="true"/></span></button><label className="sr-only" htmlFor={`price-${holding.player_code}`}>Purchase price for {p?.web_name || holding.player_code}</label><input id={`price-${holding.player_code}`} name={`price-${holding.player_code}`} type="number" inputMode="decimal" min="0" step="0.1" required value={Number.isFinite(holding.purchase_price) ? holding.purchase_price : ''} onChange={event => update({ ...draft, players: draft.players.map(h => h.player_code === holding.player_code ? { ...h, purchase_price: event.target.valueAsNumber } : h) })}/><button type="button" className="icon-button" aria-label={`Remove ${p?.web_name || holding.player_code} from preview`} onClick={() => update({ ...draft, players: draft.players.filter(h => h.player_code !== holding.player_code) })}><X size={16}/></button></div>; })}</div>
    {draft.players.length < 15 && <button type="button" className="secondary full" onClick={() => { setReplacement(0); setSearch(''); }}><Plus size={16}/>Add player ({draft.players.length}/15)</button>}
    {replacement !== null && <section className="replacement-picker"><div className="section-heading"><h3>{replacement === 0 ? 'Add a player' : `Replace ${current?.web_name || 'player'}`}</h3><button type="button" className="text-button" onClick={() => setReplacement(null)}>Cancel</button></div><label>Find a {current?.position.toLowerCase() || 'player'}<input type="search" name="replacement-search" placeholder="Search players…" value={search} onChange={event => setSearch(event.target.value)}/></label><div className="replacement-results">{!candidates.length && <p className="caption">No matching players. Try another name.</p>}{candidates.map(p => <button key={p.player_code} type="button" onClick={() => replace(p)}><span>{p.web_name}<small>{p.team_short_name}</small></span><strong>{money(p.now_cost)}</strong></button>)}</div></section>}
    <Disclosure title={`Excluded players (${draft.excluded_player_codes.length})`}><p className="caption">Use any player's detail panel to exclude them from suggestions.</p>{draft.excluded_player_codes.map(code => <div className="excluded-row" key={code}><span>{catalog.get(code)?.web_name || code}</span><button type="button" className="text-button" onClick={() => update({ ...draft, excluded_player_codes: draft.excluded_player_codes.filter(x => x !== code) })}>Include</button></div>)}</Disclosure>
    <button className="primary full editor-calculate" type="submit" disabled={busy}>{busy ? 'Calculating…' : 'Calculate preview'}</button>
  </form>;
}
