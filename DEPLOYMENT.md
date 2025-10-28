## Deploying TaiLOR Frontend to Vercel

This repo contains a Vite React app in `frontend/`. Vercel is configured via `vercel.json` to build that subdirectory and serve it as a Single Page Application (SPA).

### One-time setup
1. Push this repository to GitHub/GitLab/Bitbucket.
2. In Vercel, import the project from your repo.
   - Root Directory: keep as repository root
   - Framework Preset: Other
   - Build Command: `npm run build` (Vercel reads this from `frontend/package.json`)
   - Output Directory: `frontend/dist`
   - Install Command: `npm install --prefix frontend`
3. Ensure `vercel.json` exists at repo root (already added).

Vercel will automatically:
- `cd frontend`, install dependencies, run `npm run build`, and serve `frontend/dist`.
- Apply SPA fallback so deep links route to `index.html`.

### Custom domain: `tailor.morsestudio.dev`
1. In Vercel > Project > Settings > Domains, add `tailor.morsestudio.dev`.
2. In your DNS provider for `morsestudio.dev`, create a CNAME:
   - Name/Host: `tailor`
   - Type: `CNAME`
   - Value: `cname.vercel-dns.com`
   - TTL: default
3. Wait for DNS to propagate (usually within minutes). Vercel will verify automatically.

### Local development
```bash
cd frontend
npm install
npm run dev
```

### Notes
- Routes are handled client-side via React Router. The SPA fallback in `vercel.json` ensures reloads work on deep links.

