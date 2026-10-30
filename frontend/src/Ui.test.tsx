// @vitest-environment jsdom
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { act, cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { workspaceSchema, localTime } from './domain';
import Players from './Players';
const network = vi.hoisted(() => ({ request: vi.fn() }));
vi.mock('./api', () => ({ authClient: null, request: network.request, download: vi.fn(), ApiError: class extends Error { constructor(message: string, public status: number) { super(message); } } }));
import App from './App';
import { ApiError } from './api';

function fixture() {
  const players = Array.from({ length: 16 }, (_, i) => ({ player_code: i + 1, player_id: i + 1, first_name: 'Player', second_name: String(i + 1), web_name: `Player ${i + 1}`, team: `Club ${i % 6}`, team_code: i % 6, team_short_name: `C${i % 6}`, position: i < 2 ? 'Goalkeeper' : i < 7 ? 'Defender' : i < 12 ? 'Midfielder' : 'Forward', now_cost: 5, status: 'a', weighted_score: 3, predicted_value: 0.6, confidence: 'high', drivers: 'Observed inputs', GW9_predicted_points: 3, recent_points_total: i + 1, recent_points_average: 2, recent_points_count: 5 }));
  const squad = { bank: 1, players: players.slice(0, 15).map(p => ({ player_code: p.player_code, purchase_price: 5 })), excluded_player_codes: [] };
  const lineup = { starters: players.slice(0, 11).map(p => p.player_code), bench: [12, 13, 14, 15], captain: 1, vice_captain: 2, points: 36 };
  const squadAnalysis = { players: squad.players.map(p => p.player_code), lineups: { '9': lineup }, weighted_points: 36 };
  return workspaceSchema.parse({ snapshot: { id: 'snapshot', schema_version: 1, season: '2026-2027', gameweeks: [9], generated_at: '2026-10-28T08:00:00Z', deadline: null, weights: [1], players, evaluation: {}, evaluation_context: {}, freshness: [], performance: [], limits: [], methodology: 'Test' }, team: { revision: 1, saved_at: '2026-10-28T08:00:00Z', squad }, analysis: { snapshot_id: 'snapshot', team: squad, budget: { bank: 1, selling_value: 75, available: 76, optimal_bank: 1, market_value: 75 }, current: squadAnalysis, optimal: squadAnalysis, transfers: [{ out_player_code: 1, in_player_code: 16, out: 'Player 1', in: 'Player 16', selling_price: 5, buy_price: 5, bank_after: 1, weighted_gain: 2 }], hold: false }, auth: { mode: 'local' } });
}
const workspace = fixture();
const savedSquad = workspace.team?.squad;
if (!savedSquad) throw new Error('The test workspace must include a saved squad.');
function mount() { return render(<MemoryRouter initialEntries={['/team']}><App/></MemoryRouter>); }
async function readyPreview() {
  fireEvent.click(await screen.findByRole('button', { name: 'Edit team' }));
  fireEvent.click(within(screen.getByRole('dialog', { name: 'Edit your team' })).getByRole('button', { name: 'Calculate preview' }));
  await screen.findByRole('button', { name: 'Save as current team' });
}
beforeEach(() => {
  sessionStorage.clear();
  window.scrollTo = vi.fn();
  window.matchMedia = vi.fn().mockReturnValue({ matches: false, addEventListener: vi.fn(), removeEventListener: vi.fn() });
  HTMLDialogElement.prototype.showModal = function () { this.open = true; };
  HTMLDialogElement.prototype.close = function () { this.open = false; };
  network.request.mockReset();
  network.request.mockImplementation(async (path: string) => path === '/api/workspace' ? workspace : { id: 'preview', status: 'completed', analysis: workspace.analysis });
});
afterEach(cleanup);
describe('observable UI workflows', () => {
  it('keeps the saved team visible when a new forecast invalidates its old analysis', async () => {
    network.request.mockResolvedValue({ ...workspace, snapshot: { ...workspace.snapshot, id: 'new-forecast' } });
    mount();
    await screen.findByRole('heading', { name: 'Your team' });
    expect(screen.queryByRole('button', { name: 'Set up your team' })).toBeNull();
    expect(screen.getByText('Player 15')).toBeTruthy();
    expect(screen.queryByText('Projected XI + captain')).toBeNull();
    expect(screen.queryByRole('button', { name: 'Preview transfer' })).toBeNull();
    fireEvent.click(screen.getByRole('button', { name: 'Edit team' }));
    expect(screen.getByRole('spinbutton', { name: 'Bank (£m)' })).toHaveProperty('value', '1');
    expect(screen.getByRole('spinbutton', { name: 'Purchase price for Player 15' })).toHaveProperty('value', '5');
  });

  it('shows setup only when no team has been saved', async () => {
    network.request.mockResolvedValue({ ...workspace, team: null, analysis: null });
    mount();
    expect(await screen.findByRole('button', { name: 'Set up your team' })).toBeTruthy();
    expect(screen.queryByRole('region', { name: 'Saved squad' })).toBeNull();
  });
  it('switches to Recent form and changes the sort in the same navigation', () => {
    render(<MemoryRouter initialEntries={['/players?gw=9']}><Players snapshot={workspace.snapshot} squad={workspace.team?.squad || null} gw={9} onPlayer={() => {}}/></MemoryRouter>);
    fireEvent.click(screen.getByRole('button', { name: 'Recent form' }));
    expect(screen.getByRole('button', { name: 'Recent form' }).getAttribute('aria-pressed')).toBe('true');
    expect(screen.getByRole('combobox', { name: 'Sort players' })).toHaveProperty('value', 'recent');
    expect(screen.getByText(/Includes injured and excluded players/)).toBeTruthy();
  });
  it('preserves uncalculated bank edits when another transfer is requested', async () => {
    mount();
    fireEvent.click(await screen.findByRole('button', { name: 'Edit team' }));
    fireEvent.change(screen.getByRole('spinbutton', { name: 'Bank (£m)' }), { target: { value: '2' } });
    fireEvent.click(screen.getByRole('button', { name: 'Close Edit your team' }));
    fireEvent.click(screen.getByRole('button', { name: 'Preview transfer' }));
    expect(await screen.findByText(/Your draft is unchanged/)).toBeTruthy();
    fireEvent.click(screen.getByRole('button', { name: 'Edit team' }));
    expect(screen.getByRole('spinbutton', { name: 'Bank (£m)' })).toHaveProperty('value', '2');
  });
  it('offers recalculation after a save conflict instead of repeatedly saving the old preview', async () => {
    network.request.mockImplementation(async (path: string) => {
      if (path === '/api/workspace') return workspace;
      if (path === '/api/team') throw new ApiError('Team changed on another device', 409);
      return { id: 'preview', status: 'completed', analysis: workspace.analysis };
    });
    mount(); await readyPreview(); fireEvent.click(screen.getByRole('button', { name: 'Save as current team' }));
    await screen.findByRole('button', { name: 'Calculate preview' });
    expect(screen.queryByRole('button', { name: 'Save as current team' })).toBeNull();
  });
  it('ignores an old refresh that finishes after a successful save', async () => {
    let finishRefresh: ((value: unknown) => void) | undefined;
    let reads = 0;
    const saved = { team: { ...workspace.team, revision: 2, saved_at: '2026-10-28T15:00:00Z', squad: savedSquad }, analysis: workspace.analysis };
    network.request.mockImplementation(async (path: string) => {
      if (path === '/api/workspace') { reads += 1; return reads === 1 ? workspace : new Promise(resolve => { finishRefresh = resolve; }); }
      if (path === '/api/team') return saved;
      return { id: 'preview', status: 'completed', analysis: workspace.analysis };
    });
    mount(); await screen.findByRole('button', { name: 'Edit team' });
    fireEvent.click(screen.getByRole('button', { name: 'Refresh forecasts' }));
    await readyPreview(); fireEvent.click(screen.getByRole('button', { name: 'Save as current team' }));
    await waitFor(() => expect(screen.getByText(/Team saved/).textContent).toContain(localTime(saved.team.saved_at)));
    await act(async () => { finishRefresh?.(workspace); });
    expect(screen.getByText(/Team saved/).textContent).toContain(localTime(saved.team.saved_at));
  });
});
