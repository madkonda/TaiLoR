import { useRef } from 'react'

export default function TestUpload() {
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files
    if (files && files.length > 0) {
      console.log('Files selected:', files.length)
      console.log('File details:', Array.from(files).map(f => ({
        name: f.name,
        size: f.size,
        sizeMB: (f.size / (1024 * 1024)).toFixed(2) + ' MB',
        type: f.type
      })))
      
      // Check if any file is over 500MB
      const over500MB = Array.from(files).filter(f => f.size > 500 * 1024 * 1024)
      if (over500MB.length > 0) {
        console.log('Files over 500MB:', over500MB.map(f => f.name))
        alert(`Files over 500MB detected:\n${over500MB.map(f => `• ${f.name} (${(f.size / (1024 * 1024)).toFixed(2)} MB)`).join('\n')}`)
      } else {
        alert(`All files are under 500MB. Total files: ${files.length}`)
      }
    }
  }

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>File Upload Test</h1>
      <p>This is a simple test to check file size limits.</p>
      
      <input
        ref={fileInputRef}
        type="file"
        multiple
        accept=".mp4,.avi,.mov,.mkv,.webm"
        onChange={handleFileChange}
        style={{ 
          padding: '10px', 
          border: '2px dashed #ccc', 
          borderRadius: '5px',
          width: '100%',
          fontSize: '16px'
        }}
      />
      
      <div style={{ marginTop: '20px', fontSize: '14px', color: '#666' }}>
        <p>Check the browser console for detailed file information.</p>
        <p>This test will show if files over 500MB are detected.</p>
      </div>
    </div>
  )
}
