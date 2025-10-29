import { useRef, useState } from 'react'

export default function Upload() {
  const fileInputRef = useRef<HTMLInputElement>(null)
  const [isDragOver, setIsDragOver] = useState(false)

  const handleDropzoneClick = () => {
    fileInputRef.current?.click()
  }

  const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files
    if (files && files.length > 0) {
      await uploadFiles(Array.from(files))
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

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragOver(false)
    const files = e.dataTransfer.files
    if (files && files.length > 0) {
      await uploadFiles(Array.from(files))
    }
  }

  const uploadFiles = async (files: File[]) => {
    try {
      // Check file sizes (max 5GB per file)
      const maxSize = 5 * 1024 * 1024 * 1024 // 5GB in bytes
      for (const file of files) {
        if (file.size > maxSize) {
          alert(`File ${file.name} is too large. Maximum size is 5GB.`)
          return
        }
      }

      // For production deployment, we'll show file information
      const isProduction = window.location.hostname === 'tailor.morsestudio.dev'
      
      if (isProduction) {
        const totalSizeMB = (files.reduce((sum, file) => sum + file.size, 0) / (1024 * 1024)).toFixed(2)
        const fileList = files.map(f => `• ${f.name} (${(f.size / (1024 * 1024)).toFixed(2)} MB)`).join('\n')
        
        alert(`🚀 Files Selected Successfully!\n\n📁 Files (${files.length}):\n${fileList}\n\n📊 Total Size: ${totalSizeMB} MB\n\n✅ All files are within the 5GB limit!\n\n📋 To upload these files:\n1. Make sure your Mac backend is running\n2. Use: http://localhost:5173\n3. Your automated system will handle the rest!`)
        return
      }

      // Local development - use backend
      const formData = new FormData()
      files.forEach(file => {
        formData.append('videos', file)
      })

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

  return (
    <section className="upload-page">
      <h1>Upload Mouse Behavior Videos</h1>
      <p className="lead">Upload your mouse behavior videos for SAM2 segmentation and behavior analysis</p>

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
    </section>
  )
}


