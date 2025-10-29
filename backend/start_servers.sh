#!/bin/bash

# TaiLOR Complete System Startup Script
# Starts both the main server and WebSocket server

echo "🚀 Starting TaiLOR Complete System..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if we're in the backend directory
if [ ! -f "package.json" ]; then
    echo "❌ Please run this script from the backend directory"
    exit 1
fi

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start WebSocket server in background
echo "🔌 Starting WebSocket server on port 3002..."
node websocket_server.js &
WEBSOCKET_PID=$!

# Wait a moment for WebSocket server to start
sleep 2

# Start main server
echo "🌐 Starting main server on port 3001..."
node server.js &
MAIN_PID=$!

# Function to cleanup on exit
cleanup() {
    echo "🛑 Shutting down servers..."
    kill $WEBSOCKET_PID 2>/dev/null
    kill $MAIN_PID 2>/dev/null
    exit 0
}

# Trap Ctrl+C
trap cleanup SIGINT

echo "✅ TaiLOR system is running!"
echo "📊 Main server: http://localhost:3001"
echo "🔌 WebSocket server: ws://localhost:3002"
echo "🌐 Frontend: http://localhost:5173 (or https://tailor.morsestudio.dev)"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for both processes
wait
