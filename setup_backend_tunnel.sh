#!/bin/bash
# Setup Cloudflare Tunnel for Backend API

echo "🔧 Setting up Cloudflare Tunnel for api.mintpc.morsestudio.dev"

# Check if tunnel already exists
TUNNEL_NAME="tailor-api"
if cloudflared tunnel list | grep -q "$TUNNEL_NAME"; then
    echo "✅ Tunnel $TUNNEL_NAME already exists"
else
    echo "📦 Creating new tunnel: $TUNNEL_NAME"
    cloudflared tunnel create $TUNNEL_NAME
fi

# Route DNS
echo "🌐 Routing DNS..."
cloudflared tunnel route dns $TUNNEL_NAME api.mintpc.morsestudio.dev

# Create config file
TUNNEL_DIR="$HOME/.cloudflared"
mkdir -p "$TUNNEL_DIR"

cat > "$TUNNEL_DIR/config.yml" <<EOF
tunnel: $TUNNEL_NAME
credentials-file: $TUNNEL_DIR/$TUNNEL_NAME.json

ingress:
  - hostname: api.mintpc.morsestudio.dev
    service: http://localhost:3001
  - service: http_status:404
EOF

echo "✅ Config created at $TUNNEL_DIR/config.yml"
echo ""
echo "🚀 Start tunnel with: cloudflared tunnel run $TUNNEL_NAME"
echo "   Or run as service: cloudflared service install"
echo "   Then: cloudflared service start"

