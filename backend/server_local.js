const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Create uploads directory
const UPLOAD_DIR = './uploads';
if (!fs.existsSync(UPLOAD_DIR)) {
  fs.mkdirSync(UPLOAD_DIR, { recursive: true });
}

// Configure multer for file storage
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, UPLOAD_DIR);
  },
  filename: (req, file, cb) => {
    // Add timestamp to avoid filename conflicts
    const timestamp = Date.now();
    const ext = path.extname(file.originalname);
    const name = path.basename(file.originalname, ext);
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

// Upload endpoint
app.post('/api/upload', upload.array('videos', 5), async (req, res) => {
  try {
    if (!req.files || req.files.length === 0) {
      return res.status(400).json({ success: false, error: 'No files uploaded.' });
    }

    const uploadedFiles = [];
    
    for (const file of req.files) {
      uploadedFiles.push({
        filename: file.originalname,
        savedAs: file.filename,
        size: file.size,
        path: file.path,
        url: `http://localhost:${PORT}/uploads/${file.filename}`
      });
    }

    console.log(`✅ Successfully uploaded ${uploadedFiles.length} files to local storage`);
    console.log('Files saved to:', UPLOAD_DIR);

    res.json({
      success: true,
      message: `Successfully uploaded ${uploadedFiles.length} files to local storage`,
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

// Serve uploaded files
app.use('/uploads', express.static(UPLOAD_DIR));

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'TaiLOR Backend is running',
    backend: 'Using local file storage',
    uploadDir: UPLOAD_DIR,
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
  console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
  console.log(`📁 Files will be saved to: ${UPLOAD_DIR}`);
  console.log(`🌐 Access files at: http://localhost:${PORT}/uploads/`);
});
