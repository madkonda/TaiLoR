# SSL Certificate Issue - api.mintpc.morsestudio.dev

## Problem
Getting `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` or SSL handshake failures when accessing `https://api.mintpc.morsestudio.dev`

## Cause
Cloudflare is still provisioning the SSL certificate for the tunnel domain. This can take **5-15 minutes** after the tunnel is first created.

## Solutions

### 1. Wait for SSL Certificate Provisioning (Recommended)
- Cloudflare automatically provisions SSL certificates for tunnel domains
- Usually takes 5-15 minutes
- Check status in Cloudflare Dashboard > SSL/TLS > Edge Certificates

### 2. Verify Tunnel is Running
```bash
# On your Mac:
ps aux | grep "cloudflared tunnel"

# Check tunnel logs:
tail -f /tmp/cloudflared-tailor-api.log
```

### 3. Restart Tunnel (if needed)
```bash
pkill -f "cloudflared tunnel"
cloudflared tunnel run tailor-api
```

### 4. Check Cloudflare Dashboard
1. Go to Cloudflare Dashboard
2. Select your domain (`morsestudio.dev`)
3. Go to **SSL/TLS** > **Edge Certificates**
4. Look for `api.mintpc.morsestudio.dev` in the certificate list
5. Wait for status to show "Active"

### 5. Verify Backend is Running Locally
```bash
curl http://localhost:3001/api/health
# Should return: {"status":"ok","message":"Backend is running"}
```

## Current Status
- ✅ Tunnel is running: `tailor-api`
- ✅ Backend is running on `localhost:3001`
- ⏳ SSL certificate provisioning (waiting...)

## If SSL Still Doesn't Work After 15 Minutes
1. Check Cloudflare SSL/TLS encryption mode is set to **"Full"** (not "Flexible")
2. Verify DNS CNAME record: `api.mintpc` → `fc278834-7354-46ad-a84a-06070c8d8e43.cfargotunnel.com`
3. Try restarting the tunnel
4. Check for any firewall or network issues

