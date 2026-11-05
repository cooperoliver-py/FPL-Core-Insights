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
  return <div className="forecast-strip" aria-label={`${player.web_name} forecast points`}>{snapshot.gameweeks.map(week => {
    const fixtures = snapshot.fixtures?.[String(week)];
    const opponents = fixtures?.flatMap(fixture => fixture.home_team === player.team_code ? [`${fixture.away_short_name} (H)`] : fixture.away_team === player.team_code ? [`${fixture.home_short_name} (A)`] : []);
    const context = opponents === undefined ? 'Fixture unknown' : opponents.length ? opponents.join(' · ') : 'Blank';
    return <div key={week} className={week === gw ? 'current' : ''}><span>GW{week}</span><strong>{number(points(player, week))}</strong><small className="fixture-context" title={context}>{context}</small></div>;
  })}</div>;
}
export function RecentPointsStrip({ player, snapshot }: { player: Player; snapshot: Snapshot }) {
  const target = snapshot.gameweeks[0];
  const weeks = Array.from({ length: Math.min(5, target - 1) }, (_, index) => Math.max(1, target - 5) + index);
  const legacy = new Map([...((player.recent_points_breakdown || player.recent_gameweek_points || '').matchAll(/GW(\d+):\s*(-?\d+(?:\.\d+)?|unavailable)/g))].map(match => [Number(match[1]), match[2] === 'unavailable' ? null : Number(match[2])]));
  if (!weeks.length) return <p className="caption">No completed Gameweeks yet.</p>;
  return <div className="forecast-strip" aria-label={`${player.web_name} recent points`}>{weeks.map(week => {
    const record = player.recent_gameweeks?.find(row => row.gameweek === week);
    const recordedPoints = player.recent_gameweeks ? record?.points : legacy.get(week);
    const fixtures = record?.team_code == null ? undefined : snapshot.recent_fixtures?.[String(week)];
    const opponents = fixtures?.flatMap(fixture => fixture.home_team === record?.team_code ? [`${fixture.away_short_name} (H)`] : fixture.away_team === record?.team_code ? [`${fixture.home_short_name} (A)`] : []);
    const context = opponents === undefined ? 'Fixture unknown' : opponents.length ? opponents.join(' · ') : 'Blank';
    return <div key={week}><span>GW{week}</span><strong aria-label={recordedPoints == null ? 'No recorded points' : `${recordedPoints} points`}>{number(recordedPoints, 0)}</strong><small className="fixture-context" title={context}>{context}</small></div>;
  })}</div>;
}
export function PlayerDetails({ player, snapshot, gw, owned, previewStatus, excluded, onExclude, close }: { player: Player; snapshot: Snapshot; gw: number; owned: boolean; previewStatus?: 'incoming' | 'outgoing'; excluded: boolean; onExclude: () => void; close: () => void }) {
  const closeRef = useRef(close);
  closeRef.current = close;
  useEffect(() => {
    const opener = document.activeElement;
    const dismiss = (event: KeyboardEvent) => { if (event.key === 'Escape' && !document.querySelector('dialog[open]')) { event.preventDefault(); closeRef.current(); } };
    document.addEventListener('keydown', dismiss);
    return () => { document.removeEventListener('keydown', dismiss); if (opener instanceof HTMLElement && opener.isConnected) opener.focus(); };
  }, []);
  return <div className="player-detail">
    <header className="section-heading"><span className="muted">Player detail</span><button className="icon-button desktop-only" aria-label="Close player detail" onClick={close}><X size={18}/></button></header>
    <span className="club-label">{player.team} <span>{positionShort[player.position] || player.position}</span></span>
    <h2>{[player.first_name, player.second_name].filter(Boolean).join(' ') || player.web_name}</h2>
    <div className="player-price">{money(player.now_cost)}{owned && <span className="tag">Owned</span>}{previewStatus && <span className="tag">{previewStatus === 'incoming' ? 'In preview' : 'Leaving preview'}</span>}</div>
    <ForecastStrip player={player} snapshot={snapshot} gw={gw}/>
    {excluded && <p className="notice">Excluded from your suggestions. Your team analysis scores this player at zero; the strip above shows the original forecast.</p>}
    <dl className="facts"><div><dt>Weighted score <Help label="weighted score">Forecast points weighted {snapshot.weights.join(', ')} across the available Gameweeks.</Help></dt><dd>{number(player.weighted_score, 2)}</dd></div><div><dt>Value <Help label="value">Weighted forecast points per £1m of current price.</Help></dt><dd>{number(player.predicted_value, 2)}</dd></div><div><dt>History coverage</dt><dd className="sentence-case">{player.confidence}</dd></div><div><dt>Availability</dt><dd>{player.status === 'a' ? 'Available' : player.status === 'i' ? 'Injured' : player.status === 's' ? 'Suspended' : player.status === 'd' ? 'Doubtful' : 'Unavailable'}</dd></div></dl>
    <section className="detail-section"><h3>Recent points</h3><RecentPointsStrip player={player} snapshot={snapshot}/><div className="inline-stats"><span>Total <b>{number(player.recent_points_total, 0)}</b></span><span>Average <b>{number(player.recent_points_average)}</b></span><span>Recorded <b>{number(player.recent_points_count, 0)} GWs</b></span></div></section>
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
