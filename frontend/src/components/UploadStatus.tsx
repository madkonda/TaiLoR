import { useState, useEffect } from 'react'

interface UploadStatusProps {
  isUploading: boolean
  uploadProgress: number
  uploadedFiles: string[]
}

export default function UploadStatus({ isUploading, uploadProgress, uploadedFiles }: UploadStatusProps) {
  const [downloadStatus, setDownloadStatus] = useState<string>('')

  useEffect(() => {
    if (uploadedFiles.length > 0) {
      setDownloadStatus('Files uploaded to Google Drive. Downloading to Linux Mint...')
      
      // Simulate download status updates
      const timer = setTimeout(() => {
        setDownloadStatus('Files downloaded to Linux Mint. Ready for processing!')
      }, 5000)
      
      return () => clearTimeout(timer)
    }
  }, [uploadedFiles])

  if (!isUploading && uploadedFiles.length === 0) {
    return null
  }

  return (
    <div className="upload-status">
      {isUploading && (
        <div className="upload-progress">
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${uploadProgress}%` }}
            />
          </div>
          <p>Uploading to Google Drive... {uploadProgress}%</p>
        </div>
      )}
      
      {uploadedFiles.length > 0 && (
        <div className="download-status">
          <div className="status-icon">📥</div>
          <div className="status-text">
            <p><strong>Upload Complete!</strong></p>
            <p>Files: {uploadedFiles.join(', ')}</p>
            <p className="status-message">{downloadStatus}</p>
          </div>
        </div>
      )}
    </div>
  )
}
