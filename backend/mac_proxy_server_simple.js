#!/usr/bin/env node
/**
 * Simple Mac Proxy Server
 * Works without Cloudflare Access - uses direct IP or localhost
 */

const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
const PORT = 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Try different Linux server URLs
const LINUX_SERVER_URLS = [
  'http://192.168.1.188:8080',  // Direct IP (if on same network)
  'http://localhost:8080',       // Local testing
  'https://mintpc.morsestudio.dev'  // Cloudflare (if Access is disabled)
];

let currentLinuxUrl = null;

// Test which URL works
const testLinuxConnection = async () => {
  for (const url of LINUX_SERVER_URLS) {
    try {
      console.log(`🔍 Testing connection to: ${url}`);
      const response = await axios.get(`${url}/health`, { timeout: 5000 });
      if (response.status === 200) {
        currentLinuxUrl = url;
        console.log(`✅ Connected to Linux server: ${url}`);
        return true;
      }
    } catch (error) {
      console.log(`❌ Failed to connect to: ${url} - ${error.message}`);
    }
  }
  return false;
};

// Health check
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'Mac Proxy Server is running',
    timestamp: new Date().toISOString(),
    linux_server: currentLinuxUrl || 'Not connected'
  });
});

// Proxy all requests to Linux Mint server
app.get('/api/list-files', async (req, res) => {
  if (!currentLinuxUrl) {
    return res.status(500).json({
      success: false,
      error: 'Linux server not connected',
      details: 'No working Linux server URL found'
    });
  }

  try {
    console.log('📁 Fetching files from Linux Mint...');
    const response = await axios.get(`${currentLinuxUrl}/list-files`, {
      timeout: 10000
    });
    
    console.log(`✅ Retrieved ${response.data.videos?.length || 0} videos, ${response.data.results?.length || 0} results`);
    res.json({
      success: true,
      data: response.data
    });
  } catch (error) {
    console.error('❌ Error fetching files from Linux Mint:', error.message);
    
    // Try to reconnect
    const reconnected = await testLinuxConnection();
    if (reconnected) {
      return res.status(500).json({
        success: false,
        error: 'Connection lost, please try again',
        details: 'Reconnected to Linux server'
      });
    }
    
    res.status(500).json({
      success: false,
      error: 'Failed to fetch files from Linux Mint',
      details: error.message
    });
  }
});

// Proxy video processing requests
app.post('/api/process-video', async (req, res) => {
  if (!currentLinuxUrl) {
    return res.status(500).json({
      success: false,
      error: 'Linux server not connected'
    });
  }

  try {
    const { video_path, nest_x, nest_y, mouse_x, mouse_y } = req.body;
    
    console.log(`🎬 Processing video: ${video_path}`);
    console.log(`📍 Coordinates - Nest: (${nest_x}, ${nest_y}), Mouse: (${mouse_x}, ${mouse_y})`);
    
    const response = await axios.post(`${currentLinuxUrl}/process-video`, {
      video_path,
      nest_x,
      nest_y,
      mouse_x,
      mouse_y
    }, {
      timeout: 30000
    });
    
    console.log(`✅ Processing started: ${response.data.message}`);
    res.json({
      success: true,
      data: response.data
    });
  } catch (error) {
    console.error('❌ Error processing video:', error.message);
    res.status(500).json({
      success: false,
      error: 'Failed to process video',
      details: error.message
    });
  }
});

// Error handling
app.use((error, req, res, next) => {
  console.error('❌ Server error:', error);
  res.status(500).json({
    success: false,
    error: 'Internal server error',
    details: error.message
  });
});

// Start server
const startServer = async () => {
  console.log(`🚀 Starting Mac Proxy Server on port ${PORT}...`);
  
  // Test Linux connection
  const connected = await testLinuxConnection();
  if (!connected) {
    console.log('⚠️  Warning: Could not connect to Linux server');
    console.log('   The server will start but file operations may fail');
  }
  
  app.listen(PORT, () => {
    console.log(`✅ Mac Proxy Server running on port ${PORT}`);
    console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
    console.log(`🐧 Linux server: ${currentLinuxUrl || 'Not connected'}`);
    console.log(`📁 File listing: http://localhost:${PORT}/api/list-files`);
  });
};

startServer();


