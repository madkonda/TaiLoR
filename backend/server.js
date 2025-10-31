const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const { google } = require('googleapis');
require('dotenv').config();

// WebSocket functions - we'll use a simple approach for now
let createJob, updateJobStep;

// Simple job tracking without WebSocket for now
const activeJobs = new Map();

createJob = (jobId, filename, nestCoords, mouseCoords) => {
  const job = {
    id: jobId,
    filename: filename,
    nestCoords: nestCoords,
    mouseCoords: mouseCoords,
    status: 'pending',
    progress: 0,
    steps: [
      { name: 'upload', status: 'pending', message: 'Waiting for upload...', progress: 0 },
      { name: 'download', status: 'pending', message: 'Waiting for download...', progress: 0 },
      { name: 'extract', status: 'pending', message: 'Waiting for frame extraction...', progress: 0 },
      { name: 'segment', status: 'pending', message: 'Waiting for SAM2 segmentation...', progress: 0 },
      { name: 'complete', status: 'pending', message: 'Waiting for completion...', progress: 0 }
    ]
  };
  activeJobs.set(jobId, job);
  console.log(`📋 Job created: ${jobId} for ${filename}`);
  return job;
};

updateJobStep = (jobId, stepName, status, message, progress) => {
  const job = activeJobs.get(jobId);
  if (job) {
    const step = job.steps.find(s => s.name === stepName);
    if (step) {
      step.status = status;
      step.message = message;
      step.progress = progress;
    }
    
    // Update overall job progress
    const completedSteps = job.steps.filter(s => s.status === 'completed').length;
    const totalSteps = job.steps.length;
    job.progress = Math.round((completedSteps / totalSteps) * 100);
    job.status = status;
    
    console.log(`📊 Job ${jobId} - ${stepName}: ${status} - ${message} (${progress}%)`);
  }
};

const app = express();
const PORT = process.env.PORT || 3001;
const GOOGLE_DRIVE_FOLDER_ID = process.env.GOOGLE_DRIVE_FOLDER_ID;

// Middleware
app.use(cors());
app.use(express.json());

// Configure multer for temporary local storage
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadDir = './temp_uploads';
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
});

const upload = multer({
  storage: storage,
  limits: {
    fileSize: 5 * 1024 * 1024 * 1024 // 5GB limit
  },
  fileFilter: (req, file, cb) => {
    const allowedTypes = ['.mp4', '.avi', '.mov', '.mkv', '.webm'];
    const ext = path.extname(file.originalname).toLowerCase();
    if (allowedTypes.includes(ext)) {
      cb(null, true);
    } else {
      cb(new Error('Invalid file type. Only video files are allowed.'), false);
    }
  }
});

// Google Drive setup
async function getGoogleDriveClient() {
  try {
    // Use OAuth2 instead of service account
    const auth = new google.auth.OAuth2(
      process.env.GOOGLE_CLIENT_ID,
      process.env.GOOGLE_CLIENT_SECRET,
      process.env.GOOGLE_REDIRECT_URI
    );
    
    // For now, we'll use a simple approach with a refresh token
    // You'll need to get a refresh token from OAuth2 flow
    auth.setCredentials({
      refresh_token: process.env.GOOGLE_REFRESH_TOKEN
    });
    
    const drive = google.drive({ version: 'v3', auth });
    return drive;
  } catch (error) {
    console.error('Error setting up Google Drive client:', error);
    throw error;
  }
}

// Upload file to Google Drive
async function uploadToGoogleDrive(filePath, fileName) {
  try {
    console.log(`Uploading ${fileName} to Google Drive folder: ${GOOGLE_DRIVE_FOLDER_ID}`);
    
    const drive = await getGoogleDriveClient();
    
    // Determine MIME type based on file extension
    const ext = path.extname(fileName).toLowerCase();
    const mimeTypes = {
      '.mp4': 'video/mp4',
      '.avi': 'video/x-msvideo',
      '.mov': 'video/quicktime',
      '.mkv': 'video/x-matroska',
      '.webm': 'video/webm'
    };
    const mimeType = mimeTypes[ext] || 'video/mp4';
    
    console.log(`Using MIME type: ${mimeType}`);
    
    const fileMetadata = {
      name: fileName,
      parents: [GOOGLE_DRIVE_FOLDER_ID]
    };
    
    const media = {
      mimeType: mimeType,
      body: fs.createReadStream(filePath)
    };
    
    console.log('Creating file in Google Drive...');
    const response = await drive.files.create({
      resource: fileMetadata,
      media: media,
      fields: 'id,name,webViewLink'
    });
    
    console.log('File uploaded successfully:', response.data);
    
    return {
      id: response.data.id,
      name: response.data.name,
      webViewLink: response.data.webViewLink
    };
  } catch (error) {
    console.error('Error uploading to Google Drive:', error);
    throw error;
  }
}

// Upload endpoint
app.post('/api/upload', upload.array('videos', 5), async (req, res) => {
  try {
    if (!req.files || req.files.length === 0) {
      return res.status(400).json({ success: false, error: 'No files uploaded.' });
    }

    const uploadedFiles = [];
    const processingJobs = [];
    
    for (const file of req.files) {
      try {
        // Create processing job
        const jobId = `job_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
        const job = createJob(jobId, file.originalname, [677, 881], [766, 773]);
        
        // Update job status to uploading
        updateJobStep(jobId, 'upload', 'processing', 'Uploading to Google Drive...', 10);
        
        // Upload to Google Drive
        const driveResult = await uploadToGoogleDrive(file.path, file.originalname);
        
        uploadedFiles.push({
          filename: file.originalname,
          size: file.size,
          driveId: driveResult.id,
          driveLink: driveResult.webViewLink,
          jobId: jobId
        });
        
        processingJobs.push(jobId);
        
        // Update job status to completed upload
        updateJobStep(jobId, 'upload', 'completed', 'Uploaded to Google Drive successfully!', 20);
        updateJobStep(jobId, 'download', 'processing', 'Waiting for Linux Mint download...', 30);
        
        // Clean up local temp file
        fs.unlinkSync(file.path);
        
      } catch (error) {
        console.error(`Error uploading ${file.originalname}:`, error);
        // Clean up local temp file even on error
        if (fs.existsSync(file.path)) {
          fs.unlinkSync(file.path);
        }
        throw error;
      }
    }

    res.json({
      success: true,
      message: `Successfully uploaded ${uploadedFiles.length} files to Google Drive`,
      files: uploadedFiles,
      jobs: processingJobs
    });

  } catch (error) {
    console.error('Upload Error:', error.message);
    res.status(500).json({ 
      success: false, 
      error: `Failed to upload files: ${error.message}` 
    });
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'TaiLOR Backend is running',
    backend: 'Using Google Drive for file storage',
    timestamp: new Date().toISOString()
  });
});

// Get job status endpoint
app.get('/api/jobs', (req, res) => {
  const jobs = Array.from(activeJobs.values());
  console.log(`📊 Returning ${jobs.length} active jobs`);
  res.json({
    success: true,
    jobs: jobs
  });
});

// Store Linux Mint status
let linuxStatus = {
  videosDirectory: '/home/morsestudio/sam2/videos',
  resultsDirectory: '/home/morsestudio/sam2/results',
  videos: [],
  results: [],
  processing: [],
  completed: [],
  lastUpdate: new Date().toISOString()
};

// Get Linux Mint file status
app.get('/api/linux-status', async (req, res) => {
  try {
    res.json({
      success: true,
      status: linuxStatus
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

// Update Linux Mint status (called by Linux Mint)
app.post('/api/linux-status-update', express.json(), (req, res) => {
  try {
    const status = req.body;
    linuxStatus = {
      ...linuxStatus,
      ...status,
      lastUpdate: new Date().toISOString()
    };
    
    console.log(`🐧 Linux status updated: ${status.videos?.length || 0} videos, ${status.completed?.length || 0} completed`);
    
    res.json({
      success: true,
      message: 'Linux status updated'
    });
  } catch (error) {
    console.error('Error updating Linux status:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

// Get specific job status
app.get('/api/jobs/:jobId', (req, res) => {
  const jobId = req.params.jobId;
  const job = activeJobs.get(jobId);
  if (job) {
    res.json({
      success: true,
      job: job
    });
  } else {
    res.status(404).json({
      success: false,
      error: 'Job not found'
    });
  }
});

// Webhook endpoint for Linux Mint download notifications
app.post('/api/download-complete', express.json(), (req, res) => {
  try {
    const { filename, filepath, status, timestamp } = req.body;
    
    console.log(`📥 Download notification received:`);
    console.log(`   File: ${filename}`);
    console.log(`   Path: ${filepath}`);
    console.log(`   Status: ${status}`);
    console.log(`   Time: ${new Date(timestamp * 1000).toISOString()}`);
    
    // Here you can add any additional processing logic
    // For example, trigger SAM2 processing, update database, etc.
    
    res.json({ 
      success: true, 
      message: 'Download notification received',
      filename: filename 
    });
    
  } catch (error) {
    console.error('Error handling download notification:', error);
    res.status(500).json({ error: 'Failed to process download notification' });
  }
});

// Webhook endpoint for Linux Mint processing completion notifications
app.post('/api/processing-complete', express.json(), (req, res) => {
  try {
    const { filename, filepath, status, timestamp, type, jobId } = req.body;
    
    console.log(`🔬 Processing completion notification received:`);
    console.log(`   File: ${filename}`);
    console.log(`   Path: ${filepath}`);
    console.log(`   Status: ${status}`);
    console.log(`   Type: ${type}`);
    console.log(`   Job ID: ${jobId}`);
    console.log(`   Time: ${new Date(timestamp * 1000).toISOString()}`);
    
        if (jobId) {
          if (status === 'completed') {
            updateJobStep(jobId, 'segment', 'completed', 'SAM2 segmentation completed!', 90);
            updateJobStep(jobId, 'complete', 'completed', 'Processing complete! Results saved.', 100);
            console.log(`✅ Video processing completed successfully on Linux Mint: ${filename}`);
          } else if (status === 'failed') {
            updateJobStep(jobId, 'segment', 'failed', 'SAM2 segmentation failed', 0);
            console.log(`❌ Video processing failed on Linux Mint: ${filename}`);
          }
        } else {
          console.log(`⚠️ No jobId provided for processing notification: ${filename}`);
        }
    
    res.json({ 
      success: true, 
      message: 'Processing notification received',
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('Error handling processing notification:', error);
    res.status(500).json({ error: 'Failed to process processing notification' });
  }
});

// Video processing endpoint - now just tracks status since processing happens on Linux Mint
app.post('/api/process-video', express.json(), async (req, res) => {
  try {
    const { videoPath, nestCoords, mouseCoords, jobId } = req.body;
    
    console.log(`🎬 Video processing request received: ${videoPath}`);
    console.log(`🎯 Nest coordinates: ${nestCoords}`);
    console.log(`🐭 Mouse coordinates: ${mouseCoords}`);
    console.log(`📋 Job ID: ${jobId}`);
    
    // Validate input
    if (!videoPath || !nestCoords || !mouseCoords) {
      return res.status(400).json({ 
        success: false, 
        error: 'Missing required parameters: videoPath, nestCoords, mouseCoords' 
      });
    }
    
    // Since processing happens on Linux Mint, we just acknowledge the request
    // The actual processing will be handled by the Linux Mint download script
    console.log(`📤 Video will be processed on Linux Mint after download`);
    
    res.json({ 
      success: true, 
      message: 'Video processing request received. Processing will happen on Linux Mint.',
      jobId: jobId,
      status: 'queued_for_linux_processing'
    });
    
  } catch (error) {
    console.error('Error handling video processing request:', error);
    res.status(500).json({ 
      success: false, 
      error: 'Failed to handle video processing request',
      details: error.message 
    });
  }
});

// Get processing status endpoint
app.get('/api/processing-status/:jobId', (req, res) => {
  const { jobId } = req.params;
  
  // For now, return a simple status
  // In a real implementation, you'd track job status in a database
  res.json({
    jobId: jobId,
    status: 'processing', // or 'completed', 'failed'
    message: 'Video is being processed'
  });
});

// Process Google Drive file by file ID (from Google Picker)
app.post('/api/process-drive-file', express.json(), async (req, res) => {
  try {
    const { fileId, fileName } = req.body;
    
    if (!fileId) {
      return res.status(400).json({
        success: false,
        error: 'Missing required parameter: fileId'
      });
    }
    
    console.log(`🎬 Processing Google Drive file: ${fileId} (${fileName || 'unknown'})`);
    
    // Generate job ID
    const jobId = `job_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    const displayName = fileName || `drive_file_${fileId}`;
    
    // Create job
    createJob(jobId, displayName, [677, 881], [766, 773]);
    updateJobStep(jobId, 'upload', 'processing', 'Downloading from Google Drive...', 10);
    
    try {
      // Download file from Google Drive
      const drive = await getGoogleDriveClient();
      
      // Get file metadata
      const fileMetadata = await drive.files.get({
        fileId: fileId,
        fields: 'id,name,mimeType,size'
      });
      
      const driveFileName = fileMetadata.data.name || fileName || `video_${fileId}.mp4`;
      
      // Download file to temp location
      const tempDir = './temp_uploads';
      if (!fs.existsSync(tempDir)) {
        fs.mkdirSync(tempDir, { recursive: true });
      }
      
      const tempFilePath = path.join(tempDir, driveFileName);
      
      updateJobStep(jobId, 'upload', 'processing', `Downloading ${driveFileName}...`, 20);
      
      // Download file
      const fileStream = fs.createWriteStream(tempFilePath);
      const driveResponse = await drive.files.get({
        fileId: fileId,
        alt: 'media'
      }, { responseType: 'stream' });
      
      await new Promise((resolve, reject) => {
        driveResponse.data
          .on('end', resolve)
          .on('error', reject)
          .pipe(fileStream);
      });
      
      console.log(`✅ Downloaded file from Drive: ${driveFileName}`);
      
      // Upload to our Drive folder (for Linux Mint to process)
      updateJobStep(jobId, 'upload', 'processing', 'Uploading to processing folder...', 40);
      
      const driveResult = await uploadToGoogleDrive(tempFilePath, driveFileName);
      
      updateJobStep(jobId, 'upload', 'completed', 'File ready for processing!', 50);
      updateJobStep(jobId, 'download', 'processing', 'Waiting for Linux Mint download...', 60);
      
      // Clean up temp file
      if (fs.existsSync(tempFilePath)) {
        fs.unlinkSync(tempFilePath);
      }
      
      res.json({
        success: true,
        message: `File downloaded from Drive and queued for processing`,
        file: {
          filename: driveFileName,
          driveId: driveResult.id,
          driveLink: driveResult.webViewLink,
          jobId: jobId
        },
        jobId: jobId
      });
      
    } catch (error) {
      console.error(`Error processing Drive file ${fileId}:`, error);
      updateJobStep(jobId, 'upload', 'failed', `Error: ${error.message}`, 0);
      
      res.status(500).json({
        success: false,
        error: `Failed to process Drive file: ${error.message}`,
        jobId: jobId
      });
    }
    
  } catch (error) {
    console.error('Error handling Drive file request:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to handle Drive file request',
      details: error.message
    });
  }
});

// Process folder with SAM2 segmentation
app.post('/api/process-folder', express.json(), async (req, res) => {
  try {
    const { folderPath, coordinates } = req.body;
    
    if (!folderPath || !coordinates) {
      return res.status(400).json({
        success: false,
        error: 'Missing required parameters: folderPath and coordinates'
      });
    }
    
    console.log(`🎯 Processing folder request: ${folderPath}`);
    console.log(`📍 Coordinates - Nest: (${coordinates.nestX}, ${coordinates.nestY}), Mouse: (${coordinates.mouseX}, ${coordinates.mouseY})`);
    
    // Generate a unique job ID
    const jobId = `job_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    
    // Create a job for tracking
    createJob(jobId, folderPath, [coordinates.nestX, coordinates.nestY], [coordinates.mouseX, coordinates.mouseY]);
    
    // Send processing request to Linux Mint
    // This would typically be done via SSH or a webhook to the Linux Mint machine
    // For now, we'll simulate the request
    console.log(`📤 Sending processing request to Linux Mint for folder: ${folderPath}`);
    
    // Update job status
    updateJobStep(jobId, 'extract', 'processing', 'Starting frame extraction...', 10);
    updateJobStep(jobId, 'segment', 'pending', 'Waiting for frame extraction...', 0);
    
    res.json({
      success: true,
      message: 'Folder processing started on Linux Mint',
      jobId: jobId,
      folderPath: folderPath,
      coordinates: coordinates
    });
    
  } catch (error) {
    console.error('Error processing folder:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to process folder',
      details: error.message
    });
  }
});

// Error handling middleware
app.use((error, req, res, next) => {
  if (error instanceof multer.MulterError) {
    if (error.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({ error: 'File too large. Maximum size is 5GB.' });
    }
  }
  res.status(500).json({ error: error.message });
});

app.listen(PORT, () => {
  console.log(`🚀 TaiLOR Backend running on port ${PORT}`);
  console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
  console.log(`📁 Files will be uploaded to Google Drive folder: ${GOOGLE_DRIVE_FOLDER_ID}`);
});