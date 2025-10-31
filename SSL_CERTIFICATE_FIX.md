# Fix SSL Certificate for Uploads

## Current Status
- ✅ Backend is running (`localhost:3001`)
- ✅ Tunnel is running (`tailor-api`)
- ✅ HTTP works: `http://api.mintpc.morsestudio.dev/api/health` ✅
- ❌ HTTPS fails: SSL certificate still provisioning

## The Problem
Cloudflare is still provisioning the SSL certificate for `api.mintpc.morsestudio.dev`. This typically takes **5-30 minutes** after creating the tunnel.

## Solutions

### Option 1: Wait for SSL Certificate (RECOMMENDED)
The SSL certificate should auto-provision within 15-30 minutes.

**Check status:**
1. Go to Cloudflare Dashboard
2. Select `morsestudio.dev` domain
3. SSL/TLS → Edge Certificates
4. Look for `api.mintpc.morsestudio.dev`
5. Wait for status: **"Active"**

### Option 2: Force Certificate Provisioning
Sometimes restarting the tunnel helps:

```bash
# Stop tunnel
pkill -f "cloudflared tunnel"

# Start tunnel again
cd /Users/madhukonda/TaiLOR
cloudflared tunnel run tailor-api
```

### Option 3: Verify Tunnel Configuration
```bash
# Check tunnel config
cat ~/.cloudflared/config.yml

# Should show:
# tunnel: fc278834-7354-46ad-a84a-06070c8d8e43
# ingress:
#   - hostname: api.mintpc.morsestudio.dev
#     service: http://localhost:3001
```

### Option 4: Check Cloudflare SSL/TLS Settings
1. Cloudflare Dashboard → SSL/TLS
2. **Encryption mode**: Must be **"Full"** (not "Flexible")
3. If it's "Flexible", change it to "Full"
4. Wait 5 minutes and try again

### Option 5: Verify DNS
```bash
# Check DNS
dig api.mintpc.morsestudio.dev

# Should show Cloudflare IPs (104.x.x.x or 172.x.x.x)
```

## What's Working
- ✅ Backend server responding
- ✅ Tunnel connected
- ✅ HTTP endpoint works
- ⏳ HTTPS SSL certificate provisioning (waiting...)

## Next Steps
1. **Wait 10-15 more minutes**
2. Check Cloudflare dashboard for certificate status
3. Try upload again

## Once SSL Works
The frontend will automatically use HTTPS and uploads will work immediately.

