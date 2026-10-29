import { describe, expect, it } from 'vitest';
import { applyTransfer, fingerprint, number, squadSchema, sellingPrice } from './domain';
const squad = { bank: 1, players: Array.from({ length: 15 }, (_, i) => ({ player_code: i + 1, purchase_price: 5 })), excluded_player_codes: [99] };
describe('team preview boundaries', () => {
  it('matches engine sale rounding for fractional imported purchase prices', () => {
    expect(sellingPrice(5.05, 5.1)).toBe(5);
    expect(sellingPrice(5.15, 5.3)).toBe(5.2);
    expect(sellingPrice(5, 5.3)).toBe(5.1);
  });
  it('records the buy price and bank without changing owned purchase prices or the original squad', () => {
    const next = applyTransfer(squad, { out_player_code: 1, in_player_code: 50, out: 'Out', in: 'In', selling_price: 5, buy_price: 5.3, bank_after: 0.7, weighted_gain: 2 });
    expect(next.bank).toBe(0.7); expect(next.players[0]).toEqual({ player_code: 50, purchase_price: 5.3 });
    expect(next.players[1]).toEqual(squad.players[1]); expect(squad.players[0].player_code).toBe(1);
  });
  it('rejects a stale transfer when the outgoing player has already left', () => {
    expect(() => applyTransfer(squad, { out_player_code: 55, in_player_code: 50, out: '', in: '', selling_price: 5, buy_price: 5, bank_after: 1, weighted_gain: 2 })).toThrow('no longer');
  });
  it('treats ordering as irrelevant when checking unsaved changes', () => {
    expect(fingerprint(squad)).toBe(fingerprint({ ...squad, players: [...squad.players].reverse() }));
    expect(fingerprint(squad)).not.toBe(fingerprint({ ...squad, bank: 2 }));
  });
  it('distinguishes unknown scores from zero and rejects unsafe imported prices', () => {
    expect(number(null)).toBe('—'); expect(number(0)).not.toBe('—');
    expect(squadSchema.safeParse({ ...squad, bank: -1 }).success).toBe(false);
    expect(squadSchema.safeParse({ ...squad, players: [{ player_code: 1, purchase_price: Infinity }] }).success).toBe(false);
  });
});
