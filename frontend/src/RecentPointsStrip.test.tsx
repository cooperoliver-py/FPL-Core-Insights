// @vitest-environment jsdom
import { afterEach, expect, it } from 'vitest';
import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { RecentPointsStrip, PlayerDetails } from './components';
import Players from './Players';
import { snapshotSchema } from './domain';

const snapshot = snapshotSchema.parse({ id: 'test', schema_version: 1, season: '2026-2027', gameweeks: [10, 11, 12, 13, 14], generated_at: '2026-11-05T08:00:00Z', weights: [1, .9, .8, .7, .6], players: [{ player_code: 1, web_name: 'Gabriel', team_short_name: 'ARS', team: 'Arsenal', position: 'Defender', team_code: 3, now_cost: 8, status: 'a', weighted_score: 25, predicted_value: 3, recent_points_total: 17, recent_points_average: 8.5, recent_points_count: 2, recent_gameweeks: [{ gameweek: 5, points: 0, team_code: 43 }, { gameweek: 6, points: 17, team_code: 3 }, { gameweek: 7, points: null, team_code: 3 }, { gameweek: 8, points: 0, team_code: 3 }] }], recent_fixtures: { '5': [{ home_team: 43, away_team: 7, home_short_name: 'MCI', away_short_name: 'AVL' }], '6': [{ home_team: 3, away_team: 8, home_short_name: 'ARS', away_short_name: 'CHE' }, { home_team: 7, away_team: 3, home_short_name: 'AVL', away_short_name: 'ARS' }], '8': [] }, evaluation: {}, evaluation_context: {}, freshness: [], performance: [], limits: [], methodology: '' });
afterEach(cleanup);
it('shows five matching boxes with historical opponents, doubles, blanks and missing records', () => {
  render(<RecentPointsStrip player={snapshot.players[0]} snapshot={snapshot}/>);
  const strip = screen.getByLabelText('Gabriel recent points');
  expect(strip.className).toBe('forecast-strip');
  expect(strip.children).toHaveLength(5);
  expect(screen.getAllByLabelText('0 points')).toHaveLength(2);
  expect(screen.getByText('AVL (H)')).toBeTruthy();
  expect(screen.getByText('CHE (H) · AVL (A)')).toBeTruthy();
  expect(screen.getByText('Blank')).toBeTruthy();
  expect(screen.getAllByLabelText('No recorded points')).toHaveLength(2);
});
it('renders legacy points in the same calendar window without guessing opponents', () => {
  render(<RecentPointsStrip player={{ ...snapshot.players[0], recent_gameweeks: undefined, recent_points_breakdown: 'GW4: 99, GW5: 1, GW7: 0, GW9: -1', recent_gameweek_points: 'GW1: 100' }} snapshot={snapshot}/>);
  expect(screen.queryByText('GW4')).toBeNull();
  expect(screen.getByText('-1')).toBeTruthy();
  expect(screen.getByText('0')).toBeTruthy();
  expect(screen.getAllByText('Fixture unknown')).toHaveLength(5);
});
it('shows only completed calendar Gameweeks early in the season', () => {
  const view = render(<RecentPointsStrip player={snapshot.players[0]} snapshot={{ ...snapshot, gameweeks: [2, 3] }}/>);
  expect(screen.getByLabelText('Gabriel recent points').children).toHaveLength(1);
  expect(screen.getByText('GW1')).toBeTruthy();
  view.rerender(<RecentPointsStrip player={snapshot.players[0]} snapshot={{ ...snapshot, gameweeks: [1, 2] }}/>);
  expect(screen.getByText('No completed Gameweeks yet.')).toBeTruthy();
});
it('uses the strip in player details while retaining the aggregate statistics', () => {
  render(<PlayerDetails player={snapshot.players[0]} snapshot={snapshot} gw={10} owned={false} excluded={false} onExclude={() => {}} close={() => {}}/>);
  expect(screen.getByLabelText('Gabriel recent points')).toBeTruthy();
  expect(screen.getByText('Total')).toBeTruthy();
  expect(screen.getByText('Average')).toBeTruthy();
  expect(screen.getByText('Recorded')).toBeTruthy();
});
it('uses the same strip in the recent-form player ledger', () => {
  render(<MemoryRouter><Players snapshot={snapshot} squad={null} gw={10} onPlayer={() => {}}/></MemoryRouter>);
  fireEvent.click(screen.getByRole('button', { name: 'Recent form' }));
  expect(screen.getByLabelText('Gabriel recent points')).toBeTruthy();
  expect(screen.getByText('CHE (H) · AVL (A)')).toBeTruthy();
});
