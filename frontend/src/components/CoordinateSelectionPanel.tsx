import { FC, useCallback, useEffect, useState } from 'react';
import { FrameSelector, Point } from './FrameSelector';
import { FrameFile } from '../hooks/useDrive';

interface CoordinateSelectionPanelProps {
  frameFiles: FrameFile[];
  accessToken: string;
  onConfirm: (
    nestPoint: Point | undefined,
    mousePoint: Point | undefined,
    selectedFrameIndex: number,
    nestBox?: [number, number, number, number],
    mouseBox?: [number, number, number, number]
  ) => void;
  onCancel: () => void;
  disabled?: boolean;
}

export const CoordinateSelectionPanel: FC<CoordinateSelectionPanelProps> = ({
  frameFiles,
  accessToken,
  onConfirm,
  onCancel,
  disabled
}) => {
  const [selectedFrameIndex, setSelectedFrameIndex] = useState(0);
  const [nestPoint, setNestPoint] = useState<Point | undefined>();
  const [mousePoint, setMousePoint] = useState<Point | undefined>();
  const [nestBox, setNestBox] = useState<[number, number, number, number] | undefined>();
  const [mouseBox, setMouseBox] = useState<[number, number, number, number] | undefined>();

  const hasPoints = nestPoint && mousePoint;
  const hasBoxes = nestBox && mouseBox;
  const canConfirm = (hasPoints || hasBoxes) && !disabled;

  const handleNestPointSelected = useCallback((point: Point) => {
    setNestPoint(point);
  }, []);

  const handleMousePointSelected = useCallback((point: Point) => {
    setMousePoint(point);
  }, []);

  const handleConfirm = useCallback(() => {
    // Allow either: both points OR both boxes
    if ((nestPoint && mousePoint) || (nestBox && mouseBox)) {
      onConfirm(nestPoint, mousePoint, selectedFrameIndex, nestBox, mouseBox);
    }
  }, [nestPoint, mousePoint, selectedFrameIndex, nestBox, mouseBox, onConfirm]);

  return (
    <div className="card">
      <div className="card-title">Select Coordinates for SAM2 Segmentation</div>
      <p className="muted">Select a frame and click to set nest and mouse point coordinates. These will be used for SAM2 segmentation across all frames.</p>

      <div className="stack" style={{ marginBottom: '16px' }}>
        <label htmlFor="frame-select">Select Frame:</label>
        <select
          id="frame-select"
          value={selectedFrameIndex}
          onChange={(e) => {
            setSelectedFrameIndex(Number(e.target.value));
            setNestPoint(undefined);
            setMousePoint(undefined);
          }}
          disabled={disabled}
        >
          {frameFiles.map((file, idx) => (
            <option key={idx} value={idx}>
              {file.name ? `${file.name}` : `Frame ${idx}`}
            </option>
          ))}
        </select>
      </div>

      {frameFiles[selectedFrameIndex] && (
        <FrameSelector
          fileId={frameFiles[selectedFrameIndex].id}
          frameIndex={selectedFrameIndex}
          accessToken={accessToken}
          onNestPointSelected={handleNestPointSelected}
          onMousePointSelected={handleMousePointSelected}
          nestPoint={nestPoint}
          mousePoint={mousePoint}
        />
      )}

      <div className="stack" style={{ marginTop: '16px' }}>
        <h4>Optional: Bounding Boxes</h4>
        <p className="muted">
          If you have precise bounding box coordinates (x1, y1, x2, y2) from offline analysis, you can paste them here.
          When provided, SAM2 will use boxes instead of the clicked points.
        </p>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
          <div>
            <label className="muted">Nest box [x1, y1, x2, y2]</label>
            <input
              className="form-input"
              placeholder="e.g. 328, 687, 769, 782"
              disabled={disabled}
              onChange={(e) => {
                const parts = e.target.value.split(',').map((v) => v.trim()).filter(Boolean);
                if (parts.length === 4) {
                  const nums = parts.map((v) => Number(v));
                  if (nums.every((n) => Number.isFinite(n))) {
                    setNestBox([nums[0], nums[1], nums[2], nums[3]]);
                    return;
                  }
                }
                setNestBox(undefined);
              }}
            />
          </div>
          <div>
            <label className="muted">Rat box [x1, y1, x2, y2]</label>
            <input
              className="form-input"
              placeholder="e.g. 610, 737, 825, 939"
              disabled={disabled}
              onChange={(e) => {
                const parts = e.target.value.split(',').map((v) => v.trim()).filter(Boolean);
                if (parts.length === 4) {
                  const nums = parts.map((v) => Number(v));
                  if (nums.every((n) => Number.isFinite(n))) {
                    setMouseBox([nums[0], nums[1], nums[2], nums[3]]);
                    return;
                  }
                }
                setMouseBox(undefined);
              }}
            />
          </div>
        </div>
      </div>

      <div className="flex-row" style={{ justifyContent: 'flex-end', gap: '12px', marginTop: '16px' }}>
        <button className="button secondary" onClick={onCancel} disabled={disabled}>
          Cancel
        </button>
        <button
          className="button primary"
          onClick={handleConfirm}
          disabled={!canConfirm}
        >
          Confirm & Run SAM2
        </button>
      </div>
    </div>
  );
};

