export const IS_PROD = typeof window !== 'undefined' && window.location.hostname === 'tailor.morsestudio.dev';

// In production, talk directly to Cloudflare public API host (no /api prefix)
// In development, talk to local proxy on 3001 with /api prefix
// TEMPORARY: Use HTTP until SSL certificate is provisioned (normally should be HTTPS)
export const API_BASE = IS_PROD ? 'http://api.mintpc.morsestudio.dev' : 'http://localhost:3001';

export function apiUrl(pathWithoutApiPrefix: string): string {
  if (!pathWithoutApiPrefix.startsWith('/')) {
    // normalize
    pathWithoutApiPrefix = `/${pathWithoutApiPrefix}`;
  }
  // Always call backend endpoints under /api in both environments
  return `${API_BASE}/api${pathWithoutApiPrefix}`;
}




