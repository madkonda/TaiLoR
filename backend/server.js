const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const { google } = require('googleapis');
require('dotenv').config();

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
    fileSize: 500 * 1024 * 1024 // 500MB limit
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
    
    for (const file of req.files) {
      try {
        // Upload to Google Drive
        const driveResult = await uploadToGoogleDrive(file.path, file.originalname);
        
        uploadedFiles.push({
          filename: file.originalname,
          size: file.size,
          driveId: driveResult.id,
          driveLink: driveResult.webViewLink
        });
        
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
      files: uploadedFiles
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

// Error handling middleware
app.use((error, req, res, next) => {
  if (error instanceof multer.MulterError) {
    if (error.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({ error: 'File too large. Maximum size is 500MB.' });
    }
  }
  res.status(500).json({ error: error.message });
});

app.listen(PORT, () => {
  console.log(`🚀 TaiLOR Backend running on port ${PORT}`);
  console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
  console.log(`📁 Files will be uploaded to Google Drive folder: ${GOOGLE_DRIVE_FOLDER_ID}`);
});