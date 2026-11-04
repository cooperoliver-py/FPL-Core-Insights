import { afterEach, expect, it, vi } from 'vitest';
import { z } from 'zod';
import { ApiError, download, workspaceRequest } from './api';
afterEach(() => { vi.unstubAllGlobals(); vi.useRealTimers(); });
it('preserves actionable export errors', async () => {
  vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify({ detail: 'Forecast changed. Recalculate before exporting.' }), { status: 409 })));
  await expect(download('md', null, 'preview')).rejects.toThrow('Forecast changed. Recalculate before exporting.');
  expect(fetch).toHaveBeenCalledWith(expect.stringContaining('preview_id=preview'), expect.anything());
});
it('retries transient workspace reads but never retries expired login', async () => {
  vi.useFakeTimers();
  const fetcher = vi.fn().mockResolvedValueOnce(new Response('', { status: 503 })).mockResolvedValueOnce(new Response(JSON.stringify({ ready: true })));
  vi.stubGlobal('fetch', fetcher);
  const result = workspaceRequest('/api/workspace', z.object({ ready: z.boolean() }), null);
  await vi.runAllTimersAsync();
  await expect(result).resolves.toEqual({ ready: true });
  expect(fetcher).toHaveBeenCalledTimes(2);
  fetcher.mockReset().mockResolvedValue(new Response('{}', { status: 401 }));
  await expect(workspaceRequest('/api/workspace', z.unknown(), null)).rejects.toBeInstanceOf(ApiError);
  expect(fetcher).toHaveBeenCalledTimes(1);
});
