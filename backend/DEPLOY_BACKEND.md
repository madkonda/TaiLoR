# Backend Deployment Guide

## Current Status
✅ Backend works locally - upload tested successfully with `/Users/madhukonda/sam2/mouse_nest/1min.mp4`
✅ Upload endpoint: `http://localhost:3001/api/upload`
✅ Health check: `http://localhost:3001/api/health`

## Problem
Production frontend at `tailor.morsestudio.dev` tries to call `https://api.mintpc.morsestudio.dev/api/upload` but this domain doesn't resolve.

## Solution: Deploy Backend

### Option 1: Deploy on Same Server as mintpc.morsestudio.dev
1. SSH into your server (where mintpc.morsestudio.dev is hosted)
2. Install Node.js 18+
3. Clone this repo
4. `cd backend && npm install`
5. Copy `.env` with your Google Drive credentials
6. Start with PM2: `pm2 start server.js --name tailor-backend`
7. Configure Nginx using `nginx.api.mintpc.morsestudio.dev.conf`
8. Add DNS record: `api.mintpc.morsestudio.dev` → your server IP
9. Get SSL cert: `certbot certonly -d api.mintpc.morsestudio.dev`

### Option 2: Use Cloudflare Tunnel (Quick Setup)
1. Install cloudflared on your Mac/server
2. Create named tunnel: `cloudflared tunnel create tailor-api`
3. Route DNS: `cloudflared tunnel route dns tailor-api api.mintpc.morsestudio.dev`
4. Run: `cloudflared tunnel run tailor-api --url http://localhost:3001`

### Option 3: Deploy to Railway/Render/Fly.io
1. Connect GitHub repo
2. Set Root Directory to `backend`
3. Add environment variables from `.env`
4. Deploy - they provide HTTPS URL
5. Update frontend config to use that URL

## Quick Test (Local Backend)
Backend is currently running locally. To test:
```bash
curl -X POST http://localhost:3001/api/upload -F "videos=@/Users/madhukonda/sam2/mouse_nest/1min.mp4"
```

## Next Steps
Choose one deployment option above and execute. Once `api.mintpc.morsestudio.dev` is accessible, uploads from production will work.

