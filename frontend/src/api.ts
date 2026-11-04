import { z } from 'zod';
import { createClient } from '@supabase/supabase-js';
const url = import.meta.env.VITE_SUPABASE_URL;
const key = import.meta.env.VITE_SUPABASE_ANON_KEY;
export const authClient = url && key ? createClient(url, key) : null;
export const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '');
export class ApiError extends Error { constructor(message: string, public status: number) { super(message); } }
async function checkResponse(response: Response) {
  if (!response.ok) {
    let detail = 'The request failed. Try again.';
    try {
      const body: unknown = await response.json();
      if (typeof body === 'object' && body && 'detail' in body) detail = typeof body.detail === 'string' ? body.detail : JSON.stringify(body.detail);
    } catch { /* The host may return an HTML loading or error page. */ }
    throw new ApiError(detail, response.status);
  }
}
export async function request<T>(path: string, schema: z.ZodType<T>, token: string | null, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${apiBase}${path}`, { ...options, headers: { ...(options.body ? { 'Content-Type': 'application/json' } : {}), ...(token ? { Authorization: `Bearer ${token}` } : {}), ...options.headers } });
  await checkResponse(response);
  const body: unknown = await response.json();
  return schema.parse(body);
}
export async function download(format: 'json' | 'csv' | 'md', token: string | null, previewId?: string): Promise<void> {
  const response = await fetch(`${apiBase}/api/export?format=${format}${previewId ? `&preview_id=${encodeURIComponent(previewId)}` : ''}`, { headers: token ? { Authorization: `Bearer ${token}` } : {} });
  await checkResponse(response);
  const url = URL.createObjectURL(await response.blob());
  const link = document.createElement('a');
  link.href = url; link.download = `${previewId ? 'fpml-preview' : 'fpml'}.${format}`; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export async function workspaceRequest<T>(path: string, schema: z.ZodType<T>, token: string | null, signal?: AbortSignal): Promise<T> {
  for (let attempt = 0; ; attempt += 1) {
    try { return await request(path, schema, token, { signal }); }
    catch (error) {
      if (signal?.aborted || attempt >= 2 || (error instanceof ApiError && ![408, 429, 502, 503, 504].includes(error.status)) || error instanceof z.ZodError) throw error;
      await new Promise<void>((resolve, reject) => {
        const abort = () => { clearTimeout(timer); reject(new DOMException('Aborted', 'AbortError')); };
        const timer = setTimeout(() => { signal?.removeEventListener('abort', abort); resolve(); }, (attempt + 1) * 1000);
        signal?.addEventListener('abort', abort, { once: true });
      });
    }
  }
}
