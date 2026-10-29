import { z } from 'zod';
import { createClient } from '@supabase/supabase-js';
const url = import.meta.env.VITE_SUPABASE_URL;
const key = import.meta.env.VITE_SUPABASE_ANON_KEY;
export const authClient = url && key ? createClient(url, key) : null;
export const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '');
export class ApiError extends Error { constructor(message: string, public status: number) { super(message); } }
export async function request<T>(path: string, schema: z.ZodType<T>, token: string | null, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${apiBase}${path}`, { ...options, headers: { ...(options.body ? { 'Content-Type': 'application/json' } : {}), ...(token ? { Authorization: `Bearer ${token}` } : {}), ...options.headers } });
  if (!response.ok) {
    let detail = 'The request failed. Try again.';
    try {
      const body: unknown = await response.json();
      if (typeof body === 'object' && body && 'detail' in body) detail = typeof body.detail === 'string' ? body.detail : JSON.stringify(body.detail);
    } catch { /* The host may return an HTML loading or error page. */ }
    throw new ApiError(detail, response.status);
  }
  const body: unknown = await response.json();
  return schema.parse(body);
}
export async function download(format: 'json' | 'csv' | 'md', token: string | null): Promise<void> {
  const response = await fetch(`${apiBase}/api/export?format=${format}`, { headers: token ? { Authorization: `Bearer ${token}` } : {} });
  if (!response.ok) throw new Error('Download failed. Check the connection and try again.');
  const url = URL.createObjectURL(await response.blob());
  const link = document.createElement('a');
  link.href = url; link.download = `fpml.${format}`; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
