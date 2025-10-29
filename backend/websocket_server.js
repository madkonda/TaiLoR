const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: ["http://localhost:5173", "https://tailor.morsestudio.dev"],
    methods: ["GET", "POST"]
  }
});

// Store active processing jobs
const processingJobs = new Map();

// WebSocket connection handling
io.on('connection', (socket) => {
  console.log(`🔌 Client connected: ${socket.id}`);
  
  // Send current processing jobs to new client
  socket.emit('current_jobs', Array.from(processingJobs.values()));
  
  // Handle job status requests
  socket.on('get_job_status', (jobId) => {
    const job = processingJobs.get(jobId);
    if (job) {
      socket.emit('job_status', job);
    }
  });
  
  socket.on('disconnect', () => {
    console.log(`🔌 Client disconnected: ${socket.id}`);
  });
});

// Broadcast job updates to all connected clients
function broadcastJobUpdate(jobId, update) {
  const job = processingJobs.get(jobId);
  if (job) {
    Object.assign(job, update);
    job.lastUpdated = new Date().toISOString();
    processingJobs.set(jobId, job);
    
    io.emit('job_update', job);
    console.log(`📡 Broadcasted job update: ${jobId} - ${update.status}`);
  }
}

// Create new processing job
function createJob(jobId, filename, nestCoords, mouseCoords) {
  const job = {
    id: jobId,
    filename,
    nestCoords,
    mouseCoords,
    status: 'uploading',
    progress: 0,
    currentStep: 'Uploading to Google Drive...',
    startTime: new Date().toISOString(),
    lastUpdated: new Date().toISOString(),
    steps: [
      { name: 'upload', status: 'pending', message: 'Uploading to Google Drive...' },
      { name: 'download', status: 'pending', message: 'Downloading to Linux Mint...' },
      { name: 'extract', status: 'pending', message: 'Extracting frames with FFmpeg...' },
      { name: 'segment', status: 'pending', message: 'Running SAM2 segmentation...' },
      { name: 'complete', status: 'pending', message: 'Processing complete!' }
    ]
  };
  
  processingJobs.set(jobId, job);
  io.emit('job_created', job);
  console.log(`📋 Created new job: ${jobId} - ${filename}`);
  return job;
}

// Update job step
function updateJobStep(jobId, stepName, status, message, progress = null) {
  const job = processingJobs.get(jobId);
  if (job) {
    const step = job.steps.find(s => s.name === stepName);
    if (step) {
      step.status = status;
      step.message = message;
      step.completedAt = status === 'completed' ? new Date().toISOString() : null;
    }
    
    if (progress !== null) {
      job.progress = progress;
    }
    
    job.currentStep = message;
    job.status = status === 'completed' && stepName === 'complete' ? 'completed' : 'processing';
    
    broadcastJobUpdate(jobId, {});
  }
}

// API endpoints for job management
app.use(express.json());

// Get all jobs
app.get('/api/jobs', (req, res) => {
  res.json(Array.from(processingJobs.values()));
});

// Get specific job
app.get('/api/jobs/:jobId', (req, res) => {
  const job = processingJobs.get(req.params.jobId);
  if (job) {
    res.json(job);
  } else {
    res.status(404).json({ error: 'Job not found' });
  }
});

// Delete completed job
app.delete('/api/jobs/:jobId', (req, res) => {
  const job = processingJobs.get(req.params.jobId);
  if (job && job.status === 'completed') {
    processingJobs.delete(req.params.jobId);
    io.emit('job_deleted', req.params.jobId);
    res.json({ success: true });
  } else {
    res.status(400).json({ error: 'Job not found or not completed' });
  }
});

// Health check
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'WebSocket server is running',
    activeJobs: processingJobs.size,
    connectedClients: io.engine.clientsCount
  });
});

const PORT = process.env.WEBSOCKET_PORT || 3002;

server.listen(PORT, () => {
  console.log(`🚀 WebSocket server running on port ${PORT}`);
  console.log(`🔌 WebSocket endpoint: ws://localhost:${PORT}`);
  console.log(`📊 Active jobs: ${processingJobs.size}`);
});

// Export functions for use in main server
module.exports = {
  createJob,
  updateJobStep,
  broadcastJobUpdate,
  processingJobs
};
