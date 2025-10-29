import { useRef, useState } from 'react'
import ProcessingDashboard from '../components/ProcessingDashboard'
import { VERSION } from '../version'

interface ProcessingJob {
  id: string
  filename: string
  status: 'uploading' | 'processing' | 'completed' | 'failed'
  nestCoords?: [number, number]
  mouseCoords?: [number, number]
  progress?: number
}

export default function Upload() {
  const fileInputRef = useRef<HTMLInputElement>(null)
  const [isDragOver, setIsDragOver] = useState(false)
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [showCoordinateInput, setShowCoordinateInput] = useState(false)
  const [nestCoords, setNestCoords] = useState<[number, number]>([677, 881])
  const [mouseCoords, setMouseCoords] = useState<[number, number]>([766, 773])
  const [processingJobs, setProcessingJobs] = useState<ProcessingJob[]>([])

  const handleDropzoneClick = () => {
    fileInputRef.current?.click()
  }

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files
    if (files && files.length > 0) {
      // Process files immediately without async/await to avoid any potential Vercel interference
      processFiles(Array.from(files))
    }
  }

  const processFiles = (files: File[]) => {
    console.log('Processing files:', files.length, 'files')
    
    // Check file sizes first before any processing
    const maxSize = 5 * 1024 * 1024 * 1024 // 5GB in bytes
    const oversizedFiles = files.filter(file => file.size > maxSize)
    
    console.log('File sizes:', files.map(f => `${f.name}: ${(f.size / (1024 * 1024)).toFixed(2)} MB`))
    
    if (oversizedFiles.length > 0) {
      alert(`Some files are too large. Maximum size is 5GB per file.\n\nOversized files:\n${oversizedFiles.map(f => `• ${f.name} (${(f.size / (1024 * 1024 * 1024)).toFixed(2)} GB)`).join('\n')}`)
      return
    }
    
    // For production deployment, show file information immediately
    const isProduction = window.location.hostname === 'tailor.morsestudio.dev'
    console.log('Is production:', isProduction)
    
    if (isProduction) {
      // Production - upload files and show real-time progress
      console.log('Production mode: Uploading files to backend')
      uploadFiles(files)
      return
    }

    // Local development - handle single file for processing
    if (files.length === 1) {
      setSelectedFile(files[0])
      setShowCoordinateInput(true)
    } else {
      // Multiple files - just upload
      console.log('Using local backend for upload')
      uploadFiles(files)
    }
  }

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragOver(true)
  }

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragOver(false)
  }

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragOver(false)
    const files = e.dataTransfer.files
    if (files && files.length > 0) {
      // Process files immediately without async/await
      processFiles(Array.from(files))
    }
  }

  const uploadFiles = async (files: File[]) => {
    // Use production or local backend based on environment
    try {
      const formData = new FormData()
      files.forEach(file => {
        formData.append('videos', file)
      })

      // For now, always use localhost backend since it's not deployed to production
      const backendUrl = 'http://localhost:3001'
      const response = await fetch(`${backendUrl}/api/upload`, {
        method: 'POST',
        body: formData
      })

      const result = await response.json()
      
      if (result.success) {
        alert(`Successfully uploaded ${result.files.length} files!`)
        console.log('Upload successful:', result)
      } else {
        alert(`Upload failed: ${result.error}`)
        console.error('Upload failed:', result)
      }
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error'
      alert(`Upload error: ${errorMessage}`)
      console.error('Upload error:', error)
    }
  }

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
      <h1>🎬 Upload Mouse Behavior Videos - Real-time Processing Dashboard</h1>
      <p className="lead">Upload your mouse behavior videos for SAM2 segmentation and behavior analysis (v{VERSION})</p>

      <div 
        className={`dropzone ${isDragOver ? 'drag-over' : ''}`}
        role="button" 
        tabIndex={0} 
        onClick={handleDropzoneClick}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <div className="drop-icon">⬆️</div>
        <div className="drop-title">Drag & drop videos here</div>
        <div className="drop-sub">or click to select files</div>
        <div className="drop-note">Supports MP4, AVI, MOV, MKV, WebM (max 5 files, 5GB each)</div>
        <div className="drop-note" style={{fontSize: '0.9em', marginTop: '10px', color: '#666'}}>
          💡 This is a file selection interface. For actual uploads, use the local version.
        </div>
        <input
          ref={fileInputRef}
          type="file"
          multiple
          accept=".mp4,.avi,.mov,.mkv,.webm"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />
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
    </section>
  )
}


