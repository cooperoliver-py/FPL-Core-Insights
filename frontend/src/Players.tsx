import { useDeferredValue } from 'react';
import { useSearchParams } from 'react-router-dom';
import { ArrowDown, ArrowUpRight, Search, SlidersHorizontal } from 'lucide-react';
import { money, number, points, positions, positionShort } from './domain';
import type { Snapshot, Squad } from './domain';
import { Disclosure, ForecastStrip, Icon } from './components';

export default function Players({ snapshot, squad, gw, onPlayer }: { snapshot: Snapshot; squad: Squad | null; gw: number; onPlayer: (id: number) => void }) {
  const [params, setParams] = useSearchParams();
  const view = params.get('view') === 'recent' ? 'recent' : 'forecast';
  const query = params.get('q') || '';
  const deferredQuery = useDeferredValue(query);
  const sort = params.get('sort') || (view === 'recent' ? 'recent' : 'points');
  const ascending = params.get('direction') === 'asc';
  const position = params.get('position') || '';
  const club = params.get('club') || '';
  const max = params.get('max') || '';
  const owned = params.get('owned') === '1';
  const includeExcluded = view === 'recent' || params.get('excluded') === '1';
  const selected = new Set(squad?.players.map(p => p.player_code));
  const excluded = new Set(squad?.excluded_player_codes);
  const clubs = [...new Set(snapshot.players.map(p => p.team_short_name))].sort();
  function change(key: string, value: string) { setParams(previous => { const next = new URLSearchParams(previous); if (value) next.set(key, value); else next.delete(key); if (key !== 'page') next.delete('page'); return next; }, { replace: key === 'q' }); }
  function switchView(nextView: 'recent' | 'forecast') {
    setParams(previous => {
      const next = new URLSearchParams(previous);
      next.set('view', nextView);
      next.set('sort', nextView === 'recent' ? 'recent' : 'points');
      next.delete('page');
      return next;
    });
  }
  function value(player: Snapshot['players'][number]): number {
    if (sort === 'price') return player.now_cost;
    if (sort === 'weighted') return player.weighted_score;
    if (sort === 'value') return player.predicted_value ?? -Infinity;
    if (sort === 'recent') return player.recent_points_total ?? -Infinity;
    return points(player, gw) ?? -Infinity;
  }
  const filtered = snapshot.players.filter(player => {
    const needle = deferredQuery.toLocaleLowerCase();
    return `${player.web_name} ${player.first_name} ${player.second_name} ${player.team}`.toLocaleLowerCase().includes(needle) && (!position || player.position === position) && (!club || player.team_short_name === club) && (!max || player.now_cost <= Number(max)) && (!owned || selected.has(player.player_code)) && (includeExcluded || !excluded.has(player.player_code));
  }).sort((a, b) => {
    const av = value(a), bv = value(b);
    if (av === bv) return a.player_code - b.player_code;
    return ascending ? av - bv : bv - av;
  });
  const totalPages = Math.max(1, Math.ceil(filtered.length / 25));
  const page = Math.min(Math.max(1, Number(params.get('page')) || 1), totalPages);
  const visible = filtered.slice((page - 1) * 25, page * 25);
  const resetFilters = () => setParams({ gw: String(gw), view });
  const controls = <><label>Position<select value={position} onChange={e => change('position', e.target.value)}><option value="">All positions</option>{positions.map(p => <option key={p}>{p}</option>)}</select></label><label>Club<select value={club} onChange={e => change('club', e.target.value)}><option value="">All clubs</option>{clubs.map(c => <option key={c}>{c}</option>)}</select></label><label>Max price (£m)<input type="number" min="0" step="0.1" inputMode="decimal" placeholder="Any price" value={max} onChange={e => change('max', e.target.value)}/></label><label className="check-label"><input type="checkbox" checked={owned} onChange={e => change('owned', e.target.checked ? '1' : '')}/>Owned only</label>{view === 'forecast' && <label className="check-label"><input type="checkbox" checked={includeExcluded} onChange={e => change('excluded', e.target.checked ? '1' : '')}/>Include excluded</label>}</>;
  return <>
    <header className="page-heading"><div><h1>Players</h1><p>Forecasts and recorded form.</p></div><span className="muted">{number(filtered.length, 0)} players</span></header>
    <div className="view-tabs" role="group" aria-label="Player view"><button aria-pressed={view === 'forecast'} onClick={() => switchView('forecast')}>Forecasts</button><button aria-pressed={view === 'recent'} onClick={() => switchView('recent')}>Recent form</button></div>
    <div className="search-sort"><label className="search-field"><Search size={19} aria-hidden="true"/><span className="sr-only">Search players</span><input type="search" name="player-search" placeholder="Search a player or club…" value={query} onChange={e => change('q', e.target.value)}/></label><label className="sort-field"><span className="sr-only">Sort players</span><select value={sort} onChange={e => change('sort', e.target.value)}><option value="points">GW{gw} points</option><option value="weighted">Weighted score</option><option value="value">Value</option><option value="price">Price</option><option value="recent">Recent total</option></select></label><button className="icon-button sort-direction" aria-label={ascending ? 'Sort descending' : 'Sort ascending'} onClick={() => change('direction', ascending ? '' : 'asc')}><ArrowDown size={18} className={ascending ? 'rotated' : ''}/></button></div>
    <div className="filters desktop-only">{controls}</div><div className="mobile-only"><Disclosure title="Filter players"><div className="filters">{controls}</div></Disclosure></div>
    {view === 'recent' && <p className="caption form-note">Recorded points over the previous five Gameweeks. Includes injured and excluded players. Missing records are not zero.</p>}
    <div className="player-ledger"><div className="ledger-head"><span>Player</span><span>Price</span><span>{view === 'recent' ? 'Total' : `GW${gw}`}</span><span className="ledger-horizon">{view === 'recent' ? 'Recorded points' : `${snapshot.gameweeks.length}-GW forecast`}</span><span>{view === 'recent' ? 'Average' : 'Weighted'}</span><span/></div>{visible.map((player, index) => <button key={player.player_code} className="ledger-row" onClick={() => onPlayer(player.player_code)}>
      <span className="ledger-player"><span className="row-rank">{(page - 1) * 25 + index + 1}</span><span><strong>{player.web_name}{selected.has(player.player_code) && <span className="owned-dot" title="Owned"/>}</strong><small>{player.team_short_name} <span className="text-divider"/>{positionShort[player.position]}</small></span></span><span>{money(player.now_cost)}</span><strong className="ledger-main-points">{number(view === 'recent' ? player.recent_points_total : points(player, gw))}</strong><span className="ledger-horizon">{view === 'recent' ? <span className="recent-history">{player.recent_points_breakdown || player.recent_gameweek_points || '—'}</span> : <ForecastStrip player={player} snapshot={snapshot} gw={gw}/>}</span><span className="ledger-score">{number(view === 'recent' ? player.recent_points_average : player.weighted_score)}<small>{view === 'recent' ? `${player.recent_points_count ?? 0} recorded` : 'weighted'}</small></span><ArrowUpRight className="row-open" size={17} aria-hidden="true"/>
    </button>)}</div>
    {!visible.length && <section className="empty-results"><Icon><SlidersHorizontal size={24}/></Icon><h2>No matching players</h2><p>Try another name or clear your filters.</p><button className="secondary" onClick={resetFilters}>Clear filters</button></section>}
    <div className="pagination"><span>{filtered.length ? `${(page - 1) * 25 + 1}–${Math.min(page * 25, filtered.length)} of ${filtered.length}` : '0 players'}</span><div><button className="secondary" disabled={page === 1} onClick={() => change('page', String(page - 1))}>Previous</button><span>{page} / {totalPages}</span><button className="secondary" disabled={page === totalPages} onClick={() => change('page', String(page + 1))}>Next</button></div></div>
  </>;
}
