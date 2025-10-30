#!/bin/bash

echo "🚀 Setting up New TaiLOR System"
echo "================================"

# Install dependencies for Mac proxy server
echo "📦 Installing Mac proxy server dependencies..."
cd backend
npm install axios

# Make scripts executable
chmod +x linux_file_server.py
chmod +x mac_proxy_server.js

echo "✅ Setup complete!"
echo ""
echo "🔧 Next steps:"
echo "1. Copy linux_file_server.py to your Linux Mint machine"
echo "2. Install FastAPI on Linux Mint: pip install fastapi uvicorn"
echo "3. Start Linux server: python3 linux_file_server.py"
echo "4. Start Mac proxy: node mac_proxy_server.js"
echo "5. Deploy frontend: cd frontend && vercel --prod"
echo ""
echo "📋 Commands to run:"
echo "   Linux Mint: python3 /path/to/linux_file_server.py"
echo "   Mac: node backend/mac_proxy_server.js"
echo "   Frontend: cd frontend && vercel --prod"


