const host = typeof window !== 'undefined' ? window.location.hostname : '';
export const IS_PROD = !!host && (host === 'tailor.morsestudio.dev' || host.endsWith('.vercel.app'));

// In production, talk directly to Cloudflare public API host (no /api prefix)
// In development, talk to local proxy on 3001 with /api prefix
export const API_BASE = IS_PROD ? 'https://api.mintpc.morsestudio.dev' : 'http://localhost:3001';

export function apiUrl(pathWithoutApiPrefix: string): string {
  if (!pathWithoutApiPrefix.startsWith('/')) {
    // normalize
    pathWithoutApiPrefix = `/${pathWithoutApiPrefix}`;
  }
  // Always call backend endpoints under /api in both environments
  return `${API_BASE}/api${pathWithoutApiPrefix}`;
}




