import { ChangeEvent, FC, useMemo, useState } from 'react';
import { UploadIcon, VideoIcon, FrameIcon } from './Icons';

interface UploadPanelProps {
  disabled?: boolean;
  onUpload: (file: File, options: { fps: number; maxFrames: number }) => Promise<void>;
}

export const UploadPanel: FC<UploadPanelProps> = ({ disabled, onUpload }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [fps, setFps] = useState(1);
  const [maxFrames, setMaxFrames] = useState(300);
  const [isUploading, setIsUploading] = useState(false);

  const isReady = useMemo(() => Boolean(selectedFile) && !disabled && !isUploading, [selectedFile, disabled, isUploading]);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    setSelectedFile(file ?? null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      return;
    }

    setIsUploading(true);

    const safeFps = Math.max(0.1, fps);
    const safeMaxFrames = Math.max(1, maxFrames);

    try {
      await onUpload(selectedFile, { fps: safeFps, maxFrames: safeMaxFrames });
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Upload failed. Please check the activity log for details.';
      window.alert(message);
    } finally {
      setIsUploading(false);
    }
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{
        padding: '1.5rem',
        border: '2px dashed var(--border-medium)',
        borderRadius: 'var(--radius-lg)',
        background: 'var(--bg-secondary)',
        transition: 'all var(--transition-base)',
        cursor: disabled || isUploading ? 'not-allowed' : 'pointer',
        opacity: disabled ? 0.6 : 1
      }}
      onDragOver={(e) => {
        e.preventDefault();
        if (!disabled && !isUploading) {
          e.currentTarget.style.borderColor = 'var(--accent-purple)';
          e.currentTarget.style.background = 'var(--bg-tertiary)';
        }
      }}
      onDragLeave={(e) => {
        e.currentTarget.style.borderColor = 'var(--border-medium)';
        e.currentTarget.style.background = 'var(--bg-secondary)';
      }}
      onDrop={(e) => {
        e.preventDefault();
        if (!disabled && !isUploading) {
          e.currentTarget.style.borderColor = 'var(--border-medium)';
          e.currentTarget.style.background = 'var(--bg-secondary)';
          const file = e.dataTransfer.files[0];
          if (file && file.type.startsWith('video/')) {
            setSelectedFile(file);
          }
        }
      }}
      onClick={() => {
        if (!disabled && !isUploading && !selectedFile) {
          document.getElementById('video-input')?.click();
        }
      }}
      >
        <input
          id="video-input"
          type="file"
          accept="video/*"
          disabled={disabled || isUploading}
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />
        {!selectedFile ? (
          <div style={{ textAlign: 'center', padding: '2rem 1rem' }}>
            <div style={{ marginBottom: '1rem', display: 'flex', justifyContent: 'center' }}>
              <VideoIcon size={48} className="icon" style={{ color: 'var(--accent-purple)' }} />
            </div>
            <p style={{ fontSize: '1rem', fontWeight: 600, color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
              Upload Behavioral Video
            </p>
            <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', marginBottom: '1rem' }}>
              Drag and drop a video file here, or click to browse
            </p>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-tertiary)' }}>
              Supports MP4, MOV, AVI, and other video formats
            </p>
          </div>
        ) : (
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', padding: '1rem', background: 'var(--bg-tertiary)', borderRadius: 'var(--radius-md)' }}>
            <div style={{ 
              width: '48px', 
              height: '48px', 
              borderRadius: 'var(--radius-md)', 
              background: 'rgba(139, 92, 246, 0.2)', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center',
              flexShrink: 0
            }}>
              <VideoIcon size={24} style={{ color: 'var(--accent-purple)' }} />
            </div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <p style={{ fontWeight: 600, color: 'var(--text-primary)', marginBottom: '0.25rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                {selectedFile.name}
              </p>
              <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                {formatFileSize(selectedFile.size)} • {selectedFile.type || 'Video file'}
              </p>
            </div>
            <button
              onClick={(e) => {
                e.stopPropagation();
                setSelectedFile(null);
              }}
              className="btn btn-ghost btn-sm"
              disabled={isUploading}
            >
              Remove
            </button>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1" style={{ gap: '1rem' }}>
        <div className="form-group">
          <label className="form-label" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FrameIcon size={18} />
            Frame Extraction Rate
          </label>
          <input
            className="form-input"
            type="number"
            min={0.2}
            max={10}
            step={0.1}
            value={fps}
            disabled={isUploading}
            onChange={(event) => setFps(Number(event.target.value))}
            placeholder="1.0"
          />
          <div className="form-help">
            Frames per second to extract from the video. Lower values reduce processing time but may miss rapid movements.
          </div>
        </div>

        <div className="form-group">
          <label className="form-label" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FrameIcon size={18} />
            Maximum Frames
          </label>
          <input
            className="form-input"
            type="number"
            min={1}
            max={1200}
            step={1}
            value={maxFrames}
            disabled={isUploading}
            onChange={(event) => setMaxFrames(Number(event.target.value))}
            placeholder="300"
          />
          <div className="form-help">
            Maximum number of frames to extract. This helps manage processing time and storage requirements.
          </div>
        </div>
      </div>

      <button
        className="btn btn-primary btn-lg"
        disabled={!isReady}
        onClick={handleUpload}
        style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
      >
        {isUploading ? (
          <>
            <span className="spinner"></span>
            Processing Video & Extracting Frames...
          </>
        ) : (
          <>
            <UploadIcon size={20} />
            Upload & Extract Frames
          </>
        )}
      </button>

      {selectedFile && !isUploading && (
        <div style={{
          padding: '0.75rem 1rem',
          background: 'rgba(59, 130, 246, 0.1)',
          borderRadius: 'var(--radius-md)',
          border: '1px solid var(--accent-blue)',
          fontSize: '0.875rem'
        }}>
          <strong style={{ color: 'var(--accent-blue)' }}>Ready to upload:</strong>
          <span style={{ color: 'var(--text-secondary)', marginLeft: '0.5rem' }}>
            {selectedFile.name} ({formatFileSize(selectedFile.size)})
          </span>
        </div>
      )}
    </div>
  );
};
