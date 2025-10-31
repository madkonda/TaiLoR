import { useState } from 'react'
import ProcessingDashboard from '../components/ProcessingDashboard'
import NewLinuxFileBrowser from '../components/NewLinuxFileBrowser'
import { VERSION } from '../version'
import { apiUrl } from '../config'

// Google Drive Picker API key - add to .env in production
const GOOGLE_API_KEY = import.meta.env.VITE_GOOGLE_API_KEY || ''

interface ProcessingJob {
  id: string
  filename: string
  status: 'uploading' | 'processing' | 'completed' | 'failed'
  nestCoords?: [number, number]
  mouseCoords?: [number, number]
  progress?: number
}

export default function Upload() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [showCoordinateInput, setShowCoordinateInput] = useState(false)
  const [nestCoords, setNestCoords] = useState<[number, number]>([677, 881])
  const [mouseCoords, setMouseCoords] = useState<[number, number]>([766, 773])
  const [processingJobs, setProcessingJobs] = useState<ProcessingJob[]>([])

  const handleGoogleDrivePicker = () => {
    if (!GOOGLE_API_KEY) {
      // Silently return - button will be disabled if API key is not available
      return
    }

    // Use simpler approach - load picker on demand
    if (!window.gapi) {
      const script = document.createElement('script')
      script.src = 'https://apis.google.com/js/api.js'
      script.async = true
      script.defer = true
      script.onload = () => {
        if (window.gapi) {
          window.gapi.load('picker', { callback: showPicker })
        }
      }
      document.head.appendChild(script)
    } else {
      if (window.gapi.picker) {
        showPicker()
      } else {
        window.gapi.load('picker', { callback: showPicker })
      }
    }
  }

  const showPicker = () => {
    try {
      if (!window.google?.picker) {
        alert('Google Picker API not loaded. Please try again.')
        return
      }

      const googlePicker = window.google.picker
      const picker = new googlePicker.PickerBuilder()
        .setDeveloperKey(GOOGLE_API_KEY)
        .setCallback((data: any) => {
          if (data.action === googlePicker.Action.PICKED) {
            const file = data.docs[0]
            if (file) {
              processDriveFile(file.id, file.name)
            }
          }
        })
        .addView(googlePicker.ViewId.VIDEOS)
        .addView(googlePicker.ViewId.DOCS)
        .setSelectableMimeTypes('video/mp4,video/avi,video/mov,video/mkv,video/webm')
        .enableFeature(googlePicker.Feature.NAV_HIDDEN)
        .build()
      
      picker.setVisible(true)
    } catch (error) {
      console.error('Error showing picker:', error)
      alert('Error opening Google Drive Picker. Please upload files directly.')
    }
  }

  const processDriveFile = async (fileId: string, fileName: string) => {
    try {
      console.log(`📂 Processing Drive file: ${fileId} (${fileName})`)
      
      const response = await fetch(apiUrl('/process-drive-file'), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          fileId: fileId,
          fileName: fileName
        })
      })

      const result = await response.json()
      
      if (result.success) {
        alert(`✅ Successfully queued file from Google Drive!\n\nFile: ${result.file.filename}\nJob ID: ${result.jobId}`)
        console.log('Drive file queued:', result)
      } else {
        alert(`❌ Failed to process Drive file: ${result.error}`)
        console.error('Drive file processing failed:', result)
      }
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error'
      alert(`❌ Error processing Drive file: ${errorMessage}`)
      console.error('Drive file error:', error)
    }
  }

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (!files || files.length === 0) return;

    console.log('📤 Uploading files:', files.length, 'files');
    
    const maxSize = 5 * 1024 * 1024 * 1024;
    const oversizedFiles = Array.from(files).filter(file => file.size > maxSize);
    
    if (oversizedFiles.length > 0) {
      alert(`Some files are too large. Maximum size is 5GB per file.\n\nOversized files:\n${oversizedFiles.map(f => `• ${f.name} (${(f.size / (1024 * 1024 * 1024)).toFixed(2)} GB)`).join('\n')}`);
      return;
    }

    try {
      const formData = new FormData();
      Array.from(files).forEach(file => {
        formData.append('videos', file);
      });

      // Production uploads enabled
      const response = await fetch(apiUrl('/upload'), {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Server error: ${response.status} ${response.statusText} - ${errorText}`);
      }

      const result = await response.json();
      
      if (result.success) {
        alert(`✅ Successfully uploaded ${result.files.length} files!\n\nFiles uploaded:\n${result.files.map((f: any) => `• ${f.name}`).join('\n')}`);
        console.log('Upload successful:', result);
      } else {
        alert(`❌ Upload failed: ${result.error}`);
        console.error('Upload failed:', result);
      }
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      let userMessage = `❌ Upload error: ${errorMessage}`;
      
      // Provide helpful messages for common errors
      if (errorMessage.includes('Failed to fetch') || errorMessage.includes('network')) {
        userMessage = `❌ Network error: Cannot connect to backend API.\n\nThis might be:\n• Backend server is down\n• SSL certificate not ready (wait a few minutes)\n• Check: https://api.mintpc.morsestudio.dev/api/health`;
      } else if (errorMessage.includes('SSL') || errorMessage.includes('certificate')) {
        userMessage = `❌ SSL Error: The backend SSL certificate may still be provisioning.\n\nPlease wait 5-10 minutes and try again, or check Cloudflare dashboard for SSL certificate status.`;
      }
      
      alert(userMessage);
      console.error('Upload error:', error);
    }
  };

  const processVideoWithCoordinates = async () => {
    if (!selectedFile) return

    const jobId = `job_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
    
    // Add job to processing list
    const newJob: ProcessingJob = {
      id: jobId,
      filename: selectedFile.name,
      status: 'uploading',
      nestCoords,
      mouseCoords
    }
    
    setProcessingJobs(prev => [...prev, newJob])
    setShowCoordinateInput(false)

    try {
      // First upload the file
      const formData = new FormData()
      formData.append('videos', selectedFile)

      const uploadResponse = await fetch('http://localhost:3001/api/upload', {
        method: 'POST',
        body: formData
      })

      const uploadResult = await uploadResponse.json()
      
      if (!uploadResult.success) {
        throw new Error(uploadResult.error)
      }

      // Update job status
      setProcessingJobs(prev => 
        prev.map(job => 
          job.id === jobId 
            ? { ...job, status: 'processing' as const }
            : job
        )
      )

      // Get the uploaded file path (assuming it's saved locally)
      const videoPath = `./temp_uploads/${selectedFile.name}`

      // Start video processing
      const processResponse = await fetch('http://localhost:3001/api/process-video', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          videoPath,
          nestCoords,
          mouseCoords,
          jobId
        })
      })

      const processResult = await processResponse.json()
      
      if (processResult.success) {
        setProcessingJobs(prev => 
          prev.map(job => 
            job.id === jobId 
              ? { ...job, status: 'completed' as const }
              : job
          )
        )
        alert(`✅ Video processing completed!\n\nFile: ${selectedFile.name}\nJob ID: ${jobId}`)
      } else {
        throw new Error(processResult.error)
      }

    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error'
      setProcessingJobs(prev => 
        prev.map(job => 
          job.id === jobId 
            ? { ...job, status: 'failed' as const }
            : job
        )
      )
      alert(`❌ Video processing failed: ${errorMessage}`)
      console.error('Video processing error:', error)
    }

    setSelectedFile(null)
  }

  return (
    <section className="upload-page">
      <h1>🎬 Mouse Behavior Video Processing Dashboard</h1>
      <p className="lead">Process mouse behavior videos with SAM2 segmentation and behavior analysis (v{VERSION})</p>

      {/* File Upload Section */}
      <div style={{ 
        padding: '1.5rem', 
        backgroundColor: '#f8f9fa', 
        border: '2px solid #dee2e6', 
        borderRadius: '12px', 
        marginBottom: '2rem',
        textAlign: 'center'
      }}>
        <h3 style={{ margin: '0 0 1rem 0', color: '#495057' }}>📤 Upload Video Files</h3>
        <p style={{ margin: '0 0 1rem 0', color: '#6c757d' }}>
          Upload your mouse behavior videos or select from Google Drive to get started with SAM2 segmentation.
        </p>
        
        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          {/* Upload Button */}
          <div style={{
            border: '2px dashed #6c757d',
            borderRadius: '8px',
            padding: '2rem',
            cursor: 'pointer',
            transition: 'all 0.3s ease',
            backgroundColor: '#fff',
            flex: '1',
            minWidth: '250px'
          }}
          onClick={() => document.getElementById('fileInput')?.click()}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = '#007bff';
            e.currentTarget.style.backgroundColor = '#f8f9ff';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = '#6c757d';
            e.currentTarget.style.backgroundColor = '#fff';
          }}>
            <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>⬆️</div>
            <div style={{ fontSize: '1.2rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>
              Upload Video Files
            </div>
            <div style={{ fontSize: '0.9rem', color: '#6c757d' }}>
              MP4, AVI, MOV, MKV, WebM (max 5GB)
            </div>
            <input
              id="fileInput"
              type="file"
              multiple
              accept="video/mp4,video/avi,video/mov,video/mkv,video/webm"
              onChange={handleFileUpload}
              style={{ display: 'none' }}
            />
          </div>

          {/* Google Drive Picker Button - Only show if API key is configured */}
          {GOOGLE_API_KEY && (
            <div style={{
              border: '2px solid #4285f4',
              borderRadius: '8px',
              padding: '2rem',
              cursor: 'pointer',
              transition: 'all 0.3s ease',
              backgroundColor: '#fff',
              flex: '1',
              minWidth: '250px'
            }}
            onClick={handleGoogleDrivePicker}
            onMouseEnter={(e) => {
              e.currentTarget.style.borderColor = '#1a73e8';
              e.currentTarget.style.backgroundColor = '#f0f7ff';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.borderColor = '#4285f4';
              e.currentTarget.style.backgroundColor = '#fff';
            }}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>📁</div>
              <div style={{ fontSize: '1.2rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>
                Select from Google Drive
              </div>
              <div style={{ fontSize: '0.9rem', color: '#6c757d' }}>
                Choose videos from your Drive
              </div>
            </div>
          )}
        </div>
      </div>

      {/* File Browser Section */}
      <div style={{ 
        padding: '1.5rem', 
        backgroundColor: '#e3f2fd', 
        border: '2px solid #2196f3', 
        borderRadius: '12px', 
        marginBottom: '2rem',
        textAlign: 'center'
      }}>
        <h3 style={{ margin: '0 0 1rem 0', color: '#1976d2' }}>📁 Process Videos from Linux Mint</h3>
        <p style={{ margin: '0', color: '#424242' }}>
          The file browser below shows videos from your Linux Mint machine. 
          <strong> Click "🎬 Process" on any video</strong> to start SAM2 segmentation with custom coordinates.
        </p>
      </div>

      {/* Coordinate Input Modal */}
      {showCoordinateInput && selectedFile && (
        <div className="coordinate-modal" style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: 'white',
            padding: '2rem',
            borderRadius: '8px',
            maxWidth: '500px',
            width: '90%',
            maxHeight: '80vh',
            overflow: 'auto'
          }}>
            <h3>🎯 Set Mouse and Nest Coordinates</h3>
            <p>File: <strong>{selectedFile.name}</strong></p>
            
            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', marginBottom: '0.5rem' }}>
                🏠 Nest Coordinates (X, Y):
              </label>
              <div style={{ display: 'flex', gap: '0.5rem' }}>
                <input
                  type="number"
                  value={nestCoords[0]}
                  onChange={(e) => setNestCoords([parseInt(e.target.value) || 0, nestCoords[1]])}
                  placeholder="X"
                  style={{ padding: '0.5rem', border: '1px solid #ccc', borderRadius: '4px' }}
                />
                <input
                  type="number"
                  value={nestCoords[1]}
                  onChange={(e) => setNestCoords([nestCoords[0], parseInt(e.target.value) || 0])}
                  placeholder="Y"
                  style={{ padding: '0.5rem', border: '1px solid #ccc', borderRadius: '4px' }}
                />
              </div>
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', marginBottom: '0.5rem' }}>
                🐭 Mouse Coordinates (X, Y):
              </label>
              <div style={{ display: 'flex', gap: '0.5rem' }}>
                <input
                  type="number"
                  value={mouseCoords[0]}
                  onChange={(e) => setMouseCoords([parseInt(e.target.value) || 0, mouseCoords[1]])}
                  placeholder="X"
                  style={{ padding: '0.5rem', border: '1px solid #ccc', borderRadius: '4px' }}
                />
                <input
                  type="number"
                  value={mouseCoords[1]}
                  onChange={(e) => setMouseCoords([mouseCoords[0], parseInt(e.target.value) || 0])}
                  placeholder="Y"
                  style={{ padding: '0.5rem', border: '1px solid #ccc', borderRadius: '4px' }}
                />
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end' }}>
              <button
                onClick={() => {
                  setShowCoordinateInput(false)
                  setSelectedFile(null)
                }}
                style={{
                  padding: '0.5rem 1rem',
                  border: '1px solid #ccc',
                  borderRadius: '4px',
                  backgroundColor: 'white',
                  cursor: 'pointer'
                }}
              >
                Cancel
              </button>
              <button
                onClick={processVideoWithCoordinates}
                style={{
                  padding: '0.5rem 1rem',
                  border: 'none',
                  borderRadius: '4px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  cursor: 'pointer'
                }}
              >
                Start Processing
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Processing Jobs Status */}
      {processingJobs.length > 0 && (
        <div className="processing-jobs" style={{ marginTop: '2rem' }}>
          <h3>🔄 Processing Jobs</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            {processingJobs.map(job => (
              <div key={job.id} style={{
                padding: '1rem',
                border: '1px solid #ddd',
                borderRadius: '4px',
                backgroundColor: job.status === 'completed' ? '#d4edda' : 
                                job.status === 'failed' ? '#f8d7da' : '#fff3cd'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span><strong>{job.filename}</strong></span>
                  <span style={{
                    padding: '0.25rem 0.5rem',
                    borderRadius: '4px',
                    fontSize: '0.8rem',
                    backgroundColor: job.status === 'completed' ? '#28a745' : 
                                   job.status === 'failed' ? '#dc3545' : '#ffc107',
                    color: 'white'
                  }}>
                    {job.status.toUpperCase()}
                  </span>
                </div>
                {job.nestCoords && job.mouseCoords && (
                  <div style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.5rem' }}>
                    Nest: ({job.nestCoords[0]}, {job.nestCoords[1]}) | 
                    Mouse: ({job.mouseCoords[0]}, {job.mouseCoords[1]})
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="features">
        <div className="feature-card">
          <div className="feature-icon">🎥</div>
          <h3>SAM2 Segmentation</h3>
          <p>Advanced video segmentation using Segment Anything Model 2 for precise mouse and nest tracking</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon">✅</div>
          <h3>Behavior Analysis</h3>
          <p>Rule-based classification system for identifying mouse behaviors (IM, INB, IPI, ISI, OE, ONE)</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon">⚠️</div>
          <h3>Inconsistency Detection</h3>
          <p>Automatic flagging of frames requiring manual review for quality assurance</p>
        </div>
      </div>

        {/* Real-time Processing Dashboard */}
        <section className="processing-section" style={{ marginTop: '3rem' }}>
          <ProcessingDashboard />
        </section>

        {/* New Linux File Browser */}
        <section className="linux-file-browser-section" style={{ marginTop: '3rem' }}>
          <NewLinuxFileBrowser />
        </section>
    </section>
  )
}


