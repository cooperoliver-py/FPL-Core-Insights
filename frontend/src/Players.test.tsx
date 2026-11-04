// @vitest-environment jsdom
import { afterEach, expect, it } from 'vitest';
import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter, Route, Routes, useLocation, useNavigate } from 'react-router-dom';
import { useState } from 'react';
import Players from './Players';
import { TeamEditor } from './Team';
import Model from './Model';
import { ForecastStrip, PlayerDetails } from './components';
import { snapshotSchema } from './domain';

const snapshot = snapshotSchema.parse({ id: 'test', schema_version: 1, season: '2026-2027', gameweeks: [10, 11, 12], generated_at: '2026-11-04T08:00:00Z', weights: [1, 0.9, 0.8], players: ['Erling', 'Salah'].map((name, i) => ({ player_code: i + 1, web_name: name, team_short_name: 'MCI', team: 'Manchester City', position: 'Forward', team_code: 43, now_cost: 10, status: 'a', weighted_score: 8, predicted_value: 0.8, GW10_predicted_points: 5 })), fixtures: { '10': [{ home_team: 43, away_team: 3, home_short_name: 'MCI', away_short_name: 'ARS' }, { home_team: 8, away_team: 43, home_short_name: 'CHE', away_short_name: 'MCI' }], '11': [] }, evaluation: {}, evaluation_context: {}, freshness: [], performance: [], limits: [], methodology: '' });
const saved = { bank: 0, players: [{ player_code: 1, purchase_price: 10 }], excluded_player_codes: [] };
const preview = { ...saved, players: [{ player_code: 2, purchase_price: 10 }] };
function Screen({ tick = 0 }: { tick?: number }) {
  const location = useLocation();
  const navigate = useNavigate();
  return <><span>{tick}</span><output aria-label="URL">{location.search}</output><button onClick={() => navigate('/players?q=Salah')}>Search Salah</button><button onClick={() => navigate(-1)}>Back</button><button onClick={() => navigate('/team')}>Team</button><Players snapshot={snapshot} squad={saved} previewSquad={preview} gw={10} onPlayer={() => {}}/></>;
}
afterEach(cleanup);
it('keeps rapid edits through parent updates and synchronises URL and history', async () => {
  const view = render(<MemoryRouter initialEntries={['/players']}><Screen/></MemoryRouter>);
  const input = screen.getByRole('searchbox', { name: 'Search players' });
  for (const value of ['E', 'Er', 'Erl', 'Erli', 'Erlin', 'Erling']) {
    fireEvent.change(input, { target: { value } });
    view.rerender(<MemoryRouter initialEntries={['/players']}><Screen tick={value.length}/></MemoryRouter>);
    expect(input).toHaveProperty('value', value);
  }
  await waitFor(() => expect(screen.getByLabelText('URL').textContent).toContain('q=Erling'));
  fireEvent.change(input, { target: { value: 'Salah' } });
  fireEvent.change(input, { target: { value: 'Sala' } });
  fireEvent.change(input, { target: { value: 'Erling' } });
  await waitFor(() => expect(screen.getByText('1 player')).toBeTruthy());
  fireEvent.click(screen.getByRole('button', { name: 'Search Salah' }));
  fireEvent.click(screen.getByRole('button', { name: 'Back' }));
  await waitFor(() => expect(input).toHaveProperty('value', 'Erling'));
});
it('filters owned holdings using the saved squad and labels hypothetical membership', () => {
  render(<MemoryRouter><Players snapshot={snapshot} squad={saved} previewSquad={preview} gw={10} onPlayer={() => {}}/></MemoryRouter>);
  expect(screen.getByText('In preview')).toBeTruthy();
  expect(screen.getByText('Leaving preview')).toBeTruthy();
  fireEvent.click(screen.getAllByRole('checkbox', { name: 'Owned only' })[0]);
  expect(screen.queryByText('Salah')).toBeNull();
  expect(screen.getByText('Erling')).toBeTruthy();
  expect(screen.getByText('1 active filter')).toBeTruthy();
  fireEvent.click(screen.getByRole('button', { name: 'Clear filters' }));
  expect(screen.getByText('Salah')).toBeTruthy();
});
it('distinguishes double fixtures, blanks and unknown fixtures', () => {
  render(<ForecastStrip player={snapshot.players[0]} snapshot={snapshot} gw={10}/>);
  expect(screen.getByText('ARS (H) · CHE (A)')).toBeTruthy();
  expect(screen.getByText('Blank')).toBeTruthy();
  expect(screen.getByText('Fixture unknown')).toBeTruthy();
});

it('retains a query when navigating away immediately after typing', () => {
  function Back() { const navigate = useNavigate(); return <button onClick={() => navigate(-1)}>Return to players</button>; }
  render(<MemoryRouter initialEntries={['/players']}><Routes><Route path="/players" element={<Screen/>}/><Route path="/team" element={<Back/>}/></Routes></MemoryRouter>);
  fireEvent.change(screen.getByRole('searchbox', { name: 'Search players' }), { target: { value: 'Erling' } });
  fireEvent.click(screen.getByRole('button', { name: 'Team' }));
  fireEvent.click(screen.getByRole('button', { name: 'Return to players' }));
  expect(screen.getByRole('searchbox', { name: 'Search players' })).toHaveProperty('value', 'Erling');
});

it('dismisses the desktop inspector with Escape and restores its opening control', () => {
  function Inspector() {
    const [open, setOpen] = useState(false);
    return <><button onClick={() => setOpen(true)}>Open Erling</button>{open && <PlayerDetails player={snapshot.players[0]} snapshot={snapshot} gw={10} owned={true} excluded={false} close={() => setOpen(false)} onExclude={() => {}}/>}</>;
  }
  render(<Inspector/>);
  const opener = screen.getByRole('button', { name: 'Open Erling' });
  opener.focus(); fireEvent.click(opener);
  fireEvent.keyDown(document, { key: 'Escape' });
  expect(screen.queryByRole('button', { name: 'Close player detail' })).toBeNull();
  expect(document.activeElement).toBe(opener);
});
it('makes exclusions searchable and their include actions identifiable', () => {
  render(<TeamEditor draft={{ ...saved, excluded_player_codes: [1, 2] }} snapshot={snapshot} update={() => {}} importSquad={() => {}} calculate={() => {}} busy={false}/>);
  fireEvent.click(screen.getByText('Excluded players (2)'));
  expect(screen.getByRole('button', { name: 'Include Erling (MCI) in suggestions' })).toBeTruthy();
  fireEvent.change(screen.getByRole('searchbox', { name: 'Find excluded player' }), { target: { value: 'Salah' } });
  expect(screen.queryByRole('button', { name: 'Include Erling (MCI) in suggestions' })).toBeNull();
  expect(screen.getByRole('button', { name: 'Include Salah (MCI) in suggestions' })).toBeTruthy();
});
it('summarises scored results without counting records missing a comparison', () => {
  render(<Model snapshot={{ ...snapshot, performance: [{ gameweek: 1, optimal_xi_captain_points: 60, fpl_average: 50 }, { gameweek: 2, optimal_xi_captain_points: 40, fpl_average: 45 }, { gameweek: 3, optimal_xi_captain_points: 80 }] }}/>);
  expect(screen.getByText('1 of 2')).toBeTruthy();
  expect(screen.getByText('+5 points')).toBeTruthy();
});
