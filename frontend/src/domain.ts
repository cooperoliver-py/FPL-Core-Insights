import { z } from 'zod';

export const squadSchema = z.object({
  bank: z.number().finite().nonnegative(),
  players: z.array(z.object({ player_code: z.number().int().positive(), purchase_price: z.number().finite().nonnegative() })).length(15),
  excluded_player_codes: z.array(z.number().int().positive()).default([]),
});
export type Squad = z.infer<typeof squadSchema>;
export const playerSchema = z.object({
  player_code: z.number().int(), web_name: z.string(), first_name: z.string().default(''), second_name: z.string().default(''),
  team_short_name: z.string(), team: z.string(), position: z.string(), team_code: z.number(),
  now_cost: z.number(), status: z.string(), weighted_score: z.number(), predicted_value: z.number().nullable(),
  confidence: z.string().default('unknown'), drivers: z.string().default(''), news: z.string().nullable().optional(),
  recent_gameweek_points: z.string().nullable().optional(), recent_points_breakdown: z.string().nullable().optional(),
  recent_points_total: z.number().nullable().optional(), recent_points_average: z.number().nullable().optional(),
  recent_points_count: z.number().nullable().optional(), data_coverage: z.number().nullable().optional(),
}).catchall(z.unknown());
export type Player = z.infer<typeof playerSchema>;
const metricSchema = z.object({ mae: z.number().nullable(), rmse: z.number().nullable(), spearman: z.number().nullable() });
export const snapshotSchema = z.object({
  id: z.string(), schema_version: z.literal(1), season: z.string(), gameweeks: z.array(z.number().int()).min(1),
  generated_at: z.string(), deadline: z.string().nullable().optional(), weights: z.array(z.number()), players: z.array(playerSchema),
  evaluation: z.record(z.string(), metricSchema), evaluation_context: z.record(z.string(), z.unknown()),
  freshness: z.array(z.record(z.string(), z.unknown())), performance: z.array(z.record(z.string(), z.unknown())),
  limits: z.array(z.string()), methodology: z.string(),
}).catchall(z.unknown());
export type Snapshot = z.infer<typeof snapshotSchema>;
const lineupSchema = z.object({ starters: z.array(z.number()), bench: z.array(z.number()), captain: z.number(), vice_captain: z.number(), points: z.number() });
const squadAnalysisSchema = z.object({ players: z.array(z.number()), lineups: z.record(z.string(), lineupSchema), weighted_points: z.number() });
export const transferSchema = z.object({
  out_player_code: z.number(), in_player_code: z.number(), out: z.string(), in: z.string(),
  selling_price: z.number(), buy_price: z.number(), bank_after: z.number(), weighted_gain: z.number(),
});
export type Transfer = z.infer<typeof transferSchema>;
export const analysisSchema = z.object({
  snapshot_id: z.string(), team: squadSchema,
  budget: z.object({ bank: z.number(), selling_value: z.number(), available: z.number(), optimal_bank: z.number(), market_value: z.number() }),
  current: squadAnalysisSchema, optimal: squadAnalysisSchema, transfers: z.array(transferSchema), hold: z.boolean(),
});
export type Analysis = z.infer<typeof analysisSchema>;
export type SquadAnalysis = z.infer<typeof squadAnalysisSchema>;
export const savedTeamSchema = z.object({ revision: z.number().int(), saved_at: z.string(), squad: squadSchema });
export type SavedTeam = z.infer<typeof savedTeamSchema>;
export const workspaceSchema = z.object({ snapshot: snapshotSchema, team: savedTeamSchema.nullable(), analysis: analysisSchema.nullable(), auth: z.object({ mode: z.enum(['local', 'supabase']) }) });
export type Workspace = z.infer<typeof workspaceSchema>;
export const previewSchema = z.object({ id: z.string(), status: z.enum(['queued', 'running', 'completed', 'failed', 'interrupted']), analysis: analysisSchema.nullable().optional(), error: z.string().nullable().optional() });
export type Preview = z.infer<typeof previewSchema>;
export const saveSchema = z.object({ team: savedTeamSchema, analysis: analysisSchema });

export const positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward'];
export const positionShort: Record<string, string> = { Goalkeeper: 'GK', Defender: 'DEF', Midfielder: 'MID', Forward: 'FWD' };
export const number = (value: unknown, digits = 1): string => typeof value === 'number' && Number.isFinite(value) ? new Intl.NumberFormat(undefined, { minimumFractionDigits: digits, maximumFractionDigits: digits }).format(value) : '—';
export const money = (value: unknown): string => typeof value === 'number' && Number.isFinite(value) ? `£${number(value)}m` : '—';
export const points = (player: Player, gw: number): number | null => {
  const value = player[`GW${gw}_predicted_points`];
  return typeof value === 'number' && Number.isFinite(value) ? value : null;
};
export function fingerprint(squad: Squad): string {
  return JSON.stringify({ bank: squad.bank, players: [...squad.players].sort((a, b) => a.player_code - b.player_code), excluded_player_codes: [...squad.excluded_player_codes].sort((a, b) => a - b) });
}
export function applyTransfer(squad: Squad, transfer: Transfer): Squad {
  if (!squad.players.some(p => p.player_code === transfer.out_player_code)) throw new Error('The outgoing player is no longer in this preview. Recalculate first.');
  if (squad.players.some(p => p.player_code === transfer.in_player_code)) throw new Error('The incoming player is already in this team.');
  return { ...squad, bank: Math.round(transfer.bank_after * 10) / 10, players: squad.players.map(p => p.player_code === transfer.out_player_code ? { player_code: transfer.in_player_code, purchase_price: transfer.buy_price } : p) };
}
export function localTime(iso: string): string {
  const date = new Date(iso);
  return Number.isNaN(date.getTime()) ? 'Unavailable' : new Intl.DateTimeFormat(undefined, { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit', timeZoneName: 'short' }).format(date);
}
export function recordValue(value: unknown): string {
  if (value === null || value === undefined) return '—';
  if (typeof value === 'number') return number(value, Number.isInteger(value) ? 0 : 3);
  if (typeof value === 'string') return value;
  if (typeof value === 'boolean') return value ? 'Yes' : 'No';
  if (Array.isArray(value)) return value.map(recordValue).join(', ');
  if (typeof value === 'object') return Object.entries(value).map(([key, item]) => `${key.replaceAll('_', ' ')}: ${recordValue(item)}`).join('; ');
  return '—';
}

export function sellingPrice(purchase: number, current: number): number {
  const roundEven = (value: number) => {
    const lower = Math.floor(value);
    return value - lower === 0.5 ? lower + lower % 2 : Math.round(value);
  };
  const paid = roundEven(purchase * 10);
  const now = roundEven(current * 10);
  return (now <= paid ? now : paid + Math.floor((now - paid) / 2)) / 10;
}
