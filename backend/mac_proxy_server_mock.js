#!/usr/bin/env node
/**
 * Mock Mac Proxy Server for Testing
 * Provides mock data while we fix the Linux connection
 */

const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Mock data (empty to avoid misleading UI)
const mockFiles = {
  videos: [],
  results: [],
  timestamp: new Date().toISOString()
};

// Health check
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'Mock Mac Proxy Server is running',
    timestamp: new Date().toISOString(),
    linux_server: 'Mock data (Linux connection in progress)'
  });
});

// Mock file listing
app.get('/api/list-files', (req, res) => {
  console.log('📁 Returning mock files from Linux Mint...');
  res.json({
    success: true,
    data: mockFiles
  });
});

// Minimal jobs endpoint to satisfy frontend polling
app.get('/api/jobs', (req, res) => {
  res.json({ jobs: [] });
});

// Mock file upload endpoint
app.post('/api/upload', (req, res) => {
  console.log('📤 Mock file upload received');
  res.json({
    success: true,
    message: 'Mock upload successful',
    files: [
      {
        name: 'uploaded_video.mp4',
        size: 45444319,
        path: '/home/morsestudio/sam2/videos/uploaded_video.mp4'
      }
    ]
  });
});

// Mock video processing
app.post('/api/process-video', (req, res) => {
  try {
    const { video_path, nest_x, nest_y, mouse_x, mouse_y } = req.body;
    
    console.log(`🎬 Mock processing video: ${video_path}`);
    console.log(`📍 Coordinates - Nest: (${nest_x}, ${nest_y}), Mouse: (${mouse_x}, ${mouse_y})`);
    
    // Return immediate response (no setTimeout for mock)
    res.json({
      success: true,
      data: {
        message: "Mock processing started",
        video_path: video_path,
        coordinates: { nest: [nest_x, nest_y], mouse: [mouse_x, mouse_y] },
        process_id: Math.floor(Math.random() * 10000)
      }
    });
  } catch (error) {
    console.error('❌ Error in mock processing:', error);
    res.status(500).json({
      success: false,
      error: 'Mock processing failed',
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
app.listen(PORT, () => {
  console.log(`🚀 Mock Mac Proxy Server running on port ${PORT}`);
  console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
  console.log(`📁 File listing: http://localhost:${PORT}/api/list-files`);
  console.log(`🎬 Mock data: ${mockFiles.videos.length} videos, ${mockFiles.results.length} results`);
});
