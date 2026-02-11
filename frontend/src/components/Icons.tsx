// Icon components for Tailor UI
import { CSSProperties } from 'react';

interface IconProps {
  size?: number;
  className?: string;
  style?: CSSProperties;
}

export const MouseIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M12 2C8.13 2 5 5.13 5 9c0 3.87 3.13 7 7 7s7-3.13 7-7c0-3.87-3.13-7-7-7z" />
    <path d="M12 8v4M8 12h8" strokeLinecap="round" />
  </svg>
);

export const VideoIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
  </svg>
);

export const FrameIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <rect x="3" y="3" width="18" height="18" rx="2" />
    <path d="M9 3v18M15 3v18M3 9h18M3 15h18" />
  </svg>
);

export const SegmentationIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <circle cx="12" cy="12" r="10" />
    <path d="M8 12h8M12 8v8" strokeLinecap="round" />
    <circle cx="8" cy="8" r="1.5" fill="currentColor" />
    <circle cx="16" cy="16" r="1.5" fill="currentColor" />
  </svg>
);

export const AnalysisIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M3 3v18h18" />
    <path d="M7 16l4-4 4 4 6-6" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M7 12h.01M11 8h.01M15 4h.01" strokeLinecap="round" />
  </svg>
);

export const PredictionIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M12 2L2 7l10 5 10-5-10-5z" />
    <path d="M2 17l10 5 10-5M2 12l10 5 10-5" />
  </svg>
);

export const UploadIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4" />
    <polyline points="17 8 12 3 7 8" />
    <line x1="12" y1="3" x2="12" y2="15" />
  </svg>
);

export const FolderIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z" />
  </svg>
);

export const CheckIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" className={className} style={style}>
    <polyline points="20 6 9 17 4 12" />
  </svg>
);

export const AlertIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <circle cx="12" cy="12" r="10" />
    <line x1="12" y1="8" x2="12" y2="12" />
    <line x1="12" y1="16" x2="12.01" y2="16" />
  </svg>
);

export const FlagIcon = ({ size = 24, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className} style={style}>
    <path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z" />
    <line x1="4" y1="22" x2="4" y2="15" />
  </svg>
);

export const LoadingSpinner = ({ size = 20, className = '', style }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" className={className} style={{ ...style, animation: 'spin 1s linear infinite' }}>
    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" opacity="0.25" />
    <path d="M12 2a10 10 0 0110 10" stroke="currentColor" strokeWidth="4" fill="none" strokeLinecap="round" />
  </svg>
);

