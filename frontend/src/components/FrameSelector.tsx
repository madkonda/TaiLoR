import { FC, useCallback, useEffect, useRef, useState } from 'react';
import { loadDriveImageAsBlob } from '../utils/imageLoader';

export interface Point {
  x: number;
  y: number;
}

interface FrameSelectorProps {
  fileId: string; // Changed from frameUrl to fileId
  frameIndex: number;
  accessToken: string;
  onNestPointSelected: (point: Point) => void;
  onMousePointSelected: (point: Point) => void;
  nestPoint?: Point;
  mousePoint?: Point;
}

export const FrameSelector: FC<FrameSelectorProps> = ({
  fileId,
  frameIndex,
  accessToken,
  onNestPointSelected,
  onMousePointSelected,
  nestPoint,
  mousePoint
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const imageRef = useRef<HTMLImageElement | null>(null);
  const [isSelecting, setIsSelecting] = useState<'nest' | 'mouse' | null>(null);
  const [scale, setScale] = useState<{ x: number; y: number }>({ x: 1, y: 1 });

  const loadImage = useCallback(async () => {
    try {
      // Load image as blob using fileId and accessToken to avoid CORS issues
      const objectUrl = await loadDriveImageAsBlob(fileId, accessToken);
      
      const img = new Image();
      img.onerror = () => {
        console.error('Failed to load image:', fileId);
        URL.revokeObjectURL(objectUrl);
      };
      img.onload = () => {
        imageRef.current = img;
        const canvas = canvasRef.current;
        if (!canvas) {
          URL.revokeObjectURL(objectUrl);
          return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
          URL.revokeObjectURL(objectUrl);
          return;
        }

        // Calculate display size (scale down if too large)
        const maxWidth = 800;
        const maxHeight = 600;
        let displayWidth = img.width;
        let displayHeight = img.height;
        
        if (img.width > maxWidth || img.height > maxHeight) {
          const scaleX = maxWidth / img.width;
          const scaleY = maxHeight / img.height;
          const displayScale = Math.min(scaleX, scaleY);
          displayWidth = img.width * displayScale;
          displayHeight = img.height * displayScale;
        }
        
        // Set canvas display size (CSS)
        canvas.style.width = `${displayWidth}px`;
        canvas.style.height = `${displayHeight}px`;
        
        // Set canvas actual size (for drawing)
        canvas.width = img.width;
        canvas.height = img.height;

        // Store scale for coordinate conversion
        setScale({
          x: img.width / displayWidth,
          y: img.height / displayHeight
        });

        // Draw image at full resolution
        ctx.drawImage(img, 0, 0);

        // Draw existing points
        if (nestPoint) {
          ctx.fillStyle = 'green';
          ctx.beginPath();
          ctx.arc(nestPoint.x, nestPoint.y, 8, 0, 2 * Math.PI);
          ctx.fill();
          ctx.strokeStyle = 'white';
          ctx.lineWidth = 2;
          ctx.stroke();
        }

        if (mousePoint) {
          ctx.fillStyle = 'red';
          ctx.beginPath();
          ctx.arc(mousePoint.x, mousePoint.y, 8, 0, 2 * Math.PI);
          ctx.fill();
          ctx.strokeStyle = 'white';
          ctx.lineWidth = 2;
          ctx.stroke();
        }
        
        // Clean up object URL after loading
        URL.revokeObjectURL(objectUrl);
      };
      img.src = objectUrl;
    } catch (error) {
      console.error('Error loading image:', error);
    }
  }, [fileId, accessToken, nestPoint, mousePoint]);

  useEffect(() => {
    let cancelled = false;
    
    loadImage().catch((error) => {
      if (!cancelled) {
        console.error('Failed to load image:', error);
      }
    });
    
    return () => {
      cancelled = true;
    };
  }, [loadImage]);

  const handleClick = useCallback(
    (event: React.MouseEvent<HTMLCanvasElement>) => {
      if (!isSelecting || !canvasRef.current) return;

      const canvas = canvasRef.current;
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      // Scale coordinates back to image coordinates
      const imgX = Math.round(x * scale.x);
      const imgY = Math.round(y * scale.y);

      const point: Point = { x: imgX, y: imgY };

      if (isSelecting === 'nest') {
        onNestPointSelected(point);
      } else if (isSelecting === 'mouse') {
        onMousePointSelected(point);
      }

      setIsSelecting(null);

      // Redraw with new point
      const ctx = canvas.getContext('2d');
      if (!ctx || !imageRef.current) return;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(imageRef.current, 0, 0);

      if (isSelecting === 'nest') {
        ctx.fillStyle = 'green';
        ctx.beginPath();
        ctx.arc(point.x, point.y, 8, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;
        ctx.stroke();
        if (mousePoint) {
          ctx.fillStyle = 'red';
          ctx.beginPath();
          ctx.arc(mousePoint.x, mousePoint.y, 8, 0, 2 * Math.PI);
          ctx.fill();
          ctx.strokeStyle = 'white';
          ctx.lineWidth = 2;
          ctx.stroke();
        }
      } else {
        if (nestPoint) {
          ctx.fillStyle = 'green';
          ctx.beginPath();
          ctx.arc(nestPoint.x, nestPoint.y, 8, 0, 2 * Math.PI);
          ctx.fill();
          ctx.strokeStyle = 'white';
          ctx.lineWidth = 2;
          ctx.stroke();
        }
        ctx.fillStyle = 'red';
        ctx.beginPath();
        ctx.arc(point.x, point.y, 8, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;
        ctx.stroke();
      }
    },
    [isSelecting, scale, onNestPointSelected, onMousePointSelected, nestPoint, mousePoint]
  );

  return (
    <div className="stack">
      <div className="flex-row" style={{ justifyContent: 'space-between', alignItems: 'center' }}>
        <h3 style={{ margin: 0 }}>Frame {frameIndex}</h3>
        <div className="flex-row" style={{ gap: 8 }}>
          <button
            className={`button ${isSelecting === 'nest' ? 'primary' : 'secondary'}`}
            onClick={() => setIsSelecting(isSelecting === 'nest' ? null : 'nest')}
          >
            {nestPoint ? 'Update Nest Point' : 'Select Nest Point'}
          </button>
          <button
            className={`button ${isSelecting === 'mouse' ? 'primary' : 'secondary'}`}
            onClick={() => setIsSelecting(isSelecting === 'mouse' ? null : 'mouse')}
          >
            {mousePoint ? 'Update Mouse Point' : 'Select Mouse Point'}
          </button>
        </div>
      </div>
      {isSelecting && (
        <p className="muted" style={{ fontSize: '0.85rem' }}>
          Click on the image to set the {isSelecting === 'nest' ? 'nest' : 'mouse'} point
        </p>
      )}
      <div style={{ border: '2px solid #e5e7eb', borderRadius: '8px', overflow: 'hidden', display: 'inline-block' }}>
        <canvas
          ref={canvasRef}
          onClick={handleClick}
          style={{
            cursor: isSelecting ? 'crosshair' : 'default',
            maxWidth: '100%',
            height: 'auto',
            display: 'block'
          }}
        />
      </div>
      {(nestPoint || mousePoint) && (
        <div className="stack" style={{ gap: 4 }}>
          {nestPoint && (
            <div className="badge">
              Nest: ({nestPoint.x}, {nestPoint.y})
            </div>
          )}
          {mousePoint && (
            <div className="badge">
              Mouse: ({mousePoint.x}, {mousePoint.y})
            </div>
          )}
        </div>
      )}
    </div>
  );
};

