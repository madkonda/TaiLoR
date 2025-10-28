const express = require('express');
const multer = require('multer');
const SftpClient = require('ssh2-sftp-client');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Configure multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadDir = './uploads';
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    const timestamp = Date.now();
    const originalName = file.originalname;
    const ext = path.extname(originalName);
    const name = path.basename(originalName, ext);
    cb(null, `${name}_${timestamp}${ext}`);
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

// SFTP Configuration
const sftpConfig = {
  host: process.env.SFTP_HOST || '192.168.86.23',
  username: process.env.SFTP_USERNAME || 'morsestudio',
  password: process.env.SFTP_PASSWORD || 'morsestudio',
  port: process.env.SFTP_PORT || 22
};

const remotePath = process.env.REMOTE_PATH || '/home/morsestudio/sam2/notebooks/uploads';

// Upload endpoint
app.post('/api/upload', upload.array('videos', 5), async (req, res) => {
  try {
    if (!req.files || req.files.length === 0) {
      return res.status(400).json({ error: 'No files uploaded' });
    }

    console.log(`Received ${req.files.length} files for upload`);

    // Upload files to Linux Mint PC via SFTP
    const sftp = new SftpClient();
    
    try {
      await sftp.connect(sftpConfig);
      console.log('Connected to SFTP server');

      // Ensure remote directory exists
      try {
        await sftp.mkdir(remotePath, true);
        console.log(`Remote directory ensured: ${remotePath}`);
      } catch (err) {
        console.log('Remote directory already exists or error creating:', err.message);
      }

      const uploadResults = [];

      for (const file of req.files) {
        const localPath = file.path;
        const remoteFilePath = `${remotePath}/${file.filename}`;
        
        console.log(`Uploading ${file.originalname} to ${remoteFilePath}`);
        
        await sftp.put(localPath, remoteFilePath);
        
        uploadResults.push({
          originalName: file.originalname,
          filename: file.filename,
          remotePath: remoteFilePath,
          size: file.size,
          uploadedAt: new Date().toISOString()
        });

        // Clean up local file
        fs.unlinkSync(localPath);
        console.log(`Cleaned up local file: ${localPath}`);
      }

      await sftp.end();
      console.log('SFTP connection closed');

      res.json({
        success: true,
        message: `Successfully uploaded ${uploadResults.length} files`,
        files: uploadResults
      });

    } catch (sftpError) {
      console.error('SFTP Error:', sftpError);
      res.status(500).json({ 
        error: 'Failed to upload files to server',
        details: sftpError.message 
      });
    }

  } catch (error) {
    console.error('Upload Error:', error);
    res.status(500).json({ 
      error: 'Upload failed',
      details: error.message 
    });
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ 
    status: 'OK', 
    message: 'TaiLOR Backend is running',
    timestamp: new Date().toISOString()
  });
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
  console.log(`📁 Uploads will be saved to: ${remotePath}`);
  console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
  console.log(`🖥️  Linux Mint PC: ${sftpConfig.host}:${sftpConfig.port}`);
});