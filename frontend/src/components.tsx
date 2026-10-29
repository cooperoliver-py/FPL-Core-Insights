import { useEffect, useRef, useSyncExternalStore } from 'react';
import type { ReactNode } from 'react';
import { X, ChevronDown, CircleHelp, ArrowUpRight, ArrowDownRight } from 'lucide-react';
import { localTime, money, number, points, positions, positionShort } from './domain';
import type { Player, Snapshot, SquadAnalysis } from './domain';

export function Icon({ children }: { children: ReactNode }) { return <span className="icon" aria-hidden="true">{children}</span>; }
export function useMobile(): boolean {
  return useSyncExternalStore(callback => { const media = matchMedia('(max-width: 767px)'); media.addEventListener('change', callback); return () => media.removeEventListener('change', callback); }, () => matchMedia('(max-width: 767px)').matches, () => false);
}
export function Dialog({ title, children, close }: { title: string; children: ReactNode; close: () => void }) {
  const ref = useRef<HTMLDialogElement>(null);
  useEffect(() => { ref.current?.showModal(); return () => { ref.current?.close(); }; }, []);
  return <dialog ref={ref} className="sheet" aria-label={title} onCancel={event => { event.preventDefault(); close(); }}>
    <header className="sheet-header"><h2>{title}</h2><button className="icon-button" aria-label={`Close ${title}`} onClick={close}><X size={20}/></button></header>{children}
  </dialog>;
}
export function Disclosure({ title, children, open = false }: { title: string; children: ReactNode; open?: boolean }) {
  return <details className="disclosure" open={open || undefined}><summary>{title}<Icon><ChevronDown size={16}/></Icon></summary><div className="disclosure-body">{children}</div></details>;
}
export function Help({ label, children }: { label: string; children: ReactNode }) {
  return <details className="help"><summary aria-label={`About ${label}`}><CircleHelp size={15}/></summary><div>{children}</div></details>;
}
export function Gain({ value }: { value: number }) {
  return <span className={value > 0 ? 'gain' : value < 0 ? 'loss' : ''}>{value >= 0 ? <ArrowUpRight size={17} aria-hidden="true"/> : <ArrowDownRight size={17} aria-hidden="true"/>}{value > 0 ? '+' : ''}{number(value, 2)}</span>;
}
export function ForecastStrip({ player, snapshot, gw }: { player: Player; snapshot: Snapshot; gw: number }) {
  return <div className="forecast-strip" aria-label={`${player.web_name} forecast points`}>{snapshot.gameweeks.map(week => <div key={week} className={week === gw ? 'current' : ''}><span>GW{week}</span><strong>{number(points(player, week))}</strong></div>)}</div>;
}
export function PlayerDetails({ player, snapshot, gw, owned, excluded, onExclude, close }: { player: Player; snapshot: Snapshot; gw: number; owned: boolean; excluded: boolean; onExclude: () => void; close: () => void }) {
  return <div className="player-detail">
    <header className="section-heading"><span className="muted">Player detail</span><button className="icon-button desktop-only" aria-label="Close player detail" onClick={close}><X size={18}/></button></header>
    <span className="club-label">{player.team} <span>{positionShort[player.position] || player.position}</span></span>
    <h2>{[player.first_name, player.second_name].filter(Boolean).join(' ') || player.web_name}</h2>
    <div className="player-price">{money(player.now_cost)}{owned && <span className="tag">Owned</span>}</div>
    <ForecastStrip player={player} snapshot={snapshot} gw={gw}/>
    {excluded && <p className="notice">Excluded from your suggestions. Your team analysis scores this player at zero; the strip above shows the original forecast.</p>}
    <dl className="facts"><div><dt>Weighted score <Help label="weighted score">Forecast points weighted {snapshot.weights.join(', ')} across the available Gameweeks.</Help></dt><dd>{number(player.weighted_score, 2)}</dd></div><div><dt>Value <Help label="value">Weighted forecast points per £1m of current price.</Help></dt><dd>{number(player.predicted_value, 2)}</dd></div><div><dt>History coverage</dt><dd className="sentence-case">{player.confidence}</dd></div><div><dt>Availability</dt><dd>{player.status === 'a' ? 'Available' : player.status === 'i' ? 'Injured' : player.status === 's' ? 'Suspended' : player.status === 'd' ? 'Doubtful' : 'Unavailable'}</dd></div></dl>
    <section className="detail-section"><h3>Recent points</h3><p className="recent-history">{player.recent_gameweek_points || player.recent_points_breakdown || 'No recorded history'}</p><div className="inline-stats"><span>Total <b>{number(player.recent_points_total, 0)}</b></span><span>Average <b>{number(player.recent_points_average)}</b></span><span>Recorded <b>{number(player.recent_points_count, 0)} GWs</b></span></div></section>
    <section className="detail-section"><h3>Forecast inputs</h3><p className="input-description">{player.drivers || 'No descriptive inputs available.'}</p><p className="caption">Descriptive inputs, not causal explanations.</p></section>
    {player.news && <p className="notice">{player.news}</p>}
    <dl className="facts compact">{snapshot.gameweeks.map(week => <div key={week}><dt>GW{week} availability</dt><dd>{typeof player[`GW${week}_availability`] === 'number' ? `${number(Number(player[`GW${week}_availability`]) * 100, 0)}%` : '—'}</dd></div>)}</dl>
    <button className="secondary full" onClick={onExclude}>{excluded ? 'Include in suggestions' : 'Exclude from suggestions'}</button><p className="caption">Changes your preview. Save the team to keep this preference.</p>
  </div>;
}
export function SquadRows({ squad, snapshot, gw, onPlayer, compact = false, excluded = [] }: { squad: SquadAnalysis; snapshot: Snapshot; gw: number; onPlayer: (id: number) => void; compact?: boolean; excluded?: number[] }) {
  const lineup = squad.lineups[String(gw)];
  const catalog = new Map(snapshot.players.map(p => [p.player_code, p]));
  const rows = (codes: number[], bench: boolean) => positions.flatMap(position => {
    const members = codes.map(id => catalog.get(id)).filter((p): p is Player => p !== undefined && p.position === position);
    if (!members.length) return [];
    return [<div key={`${position}-${bench}`} className="position-group"><h3>{position === 'Goalkeeper' ? 'Goalkeeper' : `${position}s`}</h3>{members.map(player => <button key={player.player_code} className="player-row" onClick={() => onPlayer(player.player_code)}>
      <span className="position-abbr">{positionShort[player.position]}</span><span className="player-identity"><strong>{player.web_name}{excluded.includes(player.player_code) && <small className="excluded-label"> Excluded</small>}</strong><span>{player.team_short_name} <span className="mobile-only">{money(player.now_cost)}</span></span></span><span className="role-mark">{lineup?.captain === player.player_code ? <abbr title="Captain">C</abbr> : lineup?.vice_captain === player.player_code ? <abbr title="Vice-captain">V</abbr> : null}</span>{!compact && <span className="row-price">{money(player.now_cost)}</span>}<span className="row-points">{number(excluded.includes(player.player_code) ? 0 : points(player, gw))}<small>pts</small></span><ArrowUpRight className="row-open" size={17} aria-hidden="true"/>
    </button>)}</div>];
  });
  return <div className="squad-rows">{lineup ? <>{rows(lineup.starters, false)}<div className="bench-heading"><h3>Bench</h3><span>No autosubs included</span></div>{rows(lineup.bench, true)}</> : rows(squad.players, false)}</div>;
}
export function SnapshotStatus({ snapshot }: { snapshot: Snapshot }) {
  const stale = Date.now() - new Date(snapshot.generated_at).getTime() > 24 * 60 * 60 * 1000;
  return <div className="snapshot-status"><span className={`status-dot ${stale ? 'stale' : ''}`}/><span>{stale ? 'Forecast may be stale' : 'Forecast updated'} <time dateTime={snapshot.generated_at}>{localTime(snapshot.generated_at)}</time></span>{snapshot.freshness.length > 0 && <span className="warning-text">Incomplete source fixtures</span>}</div>;
}
