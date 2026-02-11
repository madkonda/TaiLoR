import { FC } from 'react';

export interface LogEntry {
  message: string;
  level?: 'info' | 'success' | 'error';
  timestamp: string;
}

const colorForLevel = (level: LogEntry['level']) => {
  switch (level) {
    case 'success':
      return '#22c55e';
    case 'error':
      return '#ef4444';
    default:
      return '#38bdf8';
  }
};

export const FrameLog: FC<{ entries: LogEntry[] }> = ({ entries }) => (
  <div className="card">
    <div className="card-title">Activity log</div>
    <div className="log-panel">
      {entries.length === 0 ? (
        <span className="muted">No activity yet. Upload a video to see progress updates.</span>
      ) : (
        entries.map((entry, index) => (
          <div className="log-line" key={`${entry.timestamp}-${index}`}>
            <span style={{ color: colorForLevel(entry.level) }}>●</span>
            <div>
              <div>{entry.message}</div>
              <small style={{ color: '#94a3b8' }}>{entry.timestamp}</small>
            </div>
          </div>
        ))
      )}
    </div>
  </div>
);





