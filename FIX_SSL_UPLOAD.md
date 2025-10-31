# Fix SSL Upload Issue - api.mintpc.morsestudio.dev

## Current Problem
- SSL handshake failure when accessing `https://api.mintpc.morsestudio.dev`
- Uploads failing due to SSL certificate not provisioned yet

## Root Cause
Cloudflare Tunnel SSL certificate for `api.mintpc.morsestudio.dev` is still provisioning. This can take 5-30 minutes.

## Immediate Solutions

### Option 1: Wait for SSL Certificate (Recommended - 5-30 min)
1. Check Cloudflare Dashboard:
   - Go to Cloudflare Dashboard → `morsestudio.dev`
   - SSL/TLS → Edge Certificates
   - Look for `api.mintpc.morsestudio.dev`
   - Wait for status: "Active"

### Option 2: Verify Tunnel is Running
```bash
# Check if tunnel is running:
ps aux | grep "cloudflared tunnel"

# Check tunnel logs:
tail -f /tmp/cloudflared-tailor-api.log

# Restart tunnel if needed:
pkill -f "cloudflared tunnel"
cloudflared tunnel run tailor-api
```

### Option 3: Check Cloudflare SSL/TLS Settings
1. Cloudflare Dashboard → SSL/TLS
2. Encryption mode: Should be **"Full"** (not "Flexible")
3. Edge Certificates: Wait for certificate to appear

### Option 4: Verify DNS
```bash
# Check DNS resolution:
dig api.mintpc.morsestudio.dev

# Should point to Cloudflare IPs (104.x.x.x or 172.x.x.x)
```

## What I've Done
- ✅ Improved CORS configuration for better cross-origin support
- ✅ Tunnel is running (`tailor-api`)
- ✅ Backend is running on `localhost:3001`

## Next Steps
1. Wait 10-15 more minutes for SSL certificate
2. Check Cloudflare dashboard for certificate status
3. Try upload again

## If Still Not Working After 30 Minutes
1. Restart the tunnel:
   ```bash
   pkill -f "cloudflared tunnel"
   cloudflared tunnel run tailor-api
   ```

2. Check Cloudflare dashboard for any errors
3. Verify tunnel is correctly configured:
   ```bash
   cat ~/.cloudflared/config.yml
   ```

