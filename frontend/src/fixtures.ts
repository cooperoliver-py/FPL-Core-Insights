import type { Workspace } from './domain';

export function fixtureWorkspace(workspace: Workspace, mode: string | null): Workspace {
  if (mode === 'empty') return { ...workspace, snapshot: { ...workspace.snapshot, players: [], performance: [], evaluation: {}, evaluation_context: {} }, analysis: null };
  if (mode === 'large') return { ...workspace, snapshot: { ...workspace.snapshot, players: Array.from({ length: 2000 }, (_, index) => ({ ...workspace.snapshot.players[index % workspace.snapshot.players.length], player_code: 10000000 + index, web_name: `Sample player ${index + 1}` })) } };
  if (mode !== 'worst') return workspace;
  return { ...workspace, snapshot: { ...workspace.snapshot, players: workspace.snapshot.players.map((player, index) => index < 3 ? {
    ...player,
    web_name: index === 0 ? 'Alexander-Arnold' : index === 1 ? 'Muharemović' : 'Dewsbury-Hall',
    first_name: 'Crysencio Jilbert Sylverio', second_name: 'Summerville',
    news: 'Development sample: long availability news must wrap without hiding prices, actions, or the forecast strip. A return date is not confirmed.',
    now_cost: index === 0 ? 0 : 15.9,
    recent_gameweek_points: null, recent_points_breakdown: null, recent_points_total: null, recent_points_average: null, recent_points_count: 0,
  } : player) } };
}
