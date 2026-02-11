import { FC, useState } from 'react';
import { MouseIcon, VideoIcon, SegmentationIcon, AnalysisIcon, FlagIcon } from './Icons';

interface SidebarProps {
  currentSection: string;
  onSectionChange: (section: string) => void;
  user?: { name?: string; email?: string; picture?: string } | null;
}

export const Sidebar: FC<SidebarProps> = ({ currentSection, onSectionChange, user }) => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const menuItems = [
    { id: 'upload', label: 'Upload & Extract', icon: VideoIcon },
    { id: 'segmentation', label: 'Segmentation', icon: SegmentationIcon },
    { id: 'prediction', label: 'Prediction', icon: AnalysisIcon },
    { id: 'flags', label: 'Review Flags', icon: FlagIcon },
    { id: 'reference', label: 'Reference', icon: MouseIcon },
  ];

  return (
    <>
      <aside
        style={{
          width: isCollapsed ? '80px' : '280px',
          minHeight: '100vh',
          background: 'var(--bg-sidebar)',
          color: 'var(--text-primary)',
          display: 'flex',
          flexDirection: 'column',
          transition: 'width var(--transition-base)',
          position: 'fixed',
          left: 0,
          top: 0,
          zIndex: 1000,
          boxShadow: '4px 0 6px -1px rgb(0 0 0 / 0.1)',
          overflowY: 'auto'
        }}
      >
        {/* Logo & Header */}
        <div style={{
          padding: '1.5rem',
          borderBottom: '1px solid rgba(255,255,255,0.1)',
          display: 'flex',
          alignItems: 'center',
          gap: '1rem',
          minHeight: '80px'
        }}>
          {!isCollapsed && (
            <>
              <div style={{
                width: '48px',
                height: '48px',
                borderRadius: 'var(--radius-lg)',
                background: 'var(--accent-purple)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                flexShrink: 0
              }}>
                <MouseIcon size={28} style={{ color: 'white' }} />
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <h1 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 700, lineHeight: 1.2 }}>
                  Tailor
                </h1>
                <p style={{ margin: 0, fontSize: '0.75rem', opacity: 0.8, lineHeight: 1.2 }}>
                  Behavior Analysis
                </p>
              </div>
            </>
          )}
          {isCollapsed && (
            <div style={{
              width: '48px',
              height: '48px',
              borderRadius: 'var(--radius-lg)',
              background: 'var(--accent-purple)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '0 auto'
            }}>
              <MouseIcon size={28} style={{ color: 'white' }} />
            </div>
          )}
          <button
            onClick={() => setIsCollapsed(!isCollapsed)}
            style={{
              position: 'absolute',
              right: '0.5rem',
              top: '1.5rem',
              background: 'rgba(255,255,255,0.1)',
              border: 'none',
              color: 'white',
              width: '32px',
              height: '32px',
              borderRadius: 'var(--radius-md)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transition: 'background var(--transition-fast)'
            }}
            onMouseEnter={(e) => e.currentTarget.style.background = 'rgba(255,255,255,0.2)'}
            onMouseLeave={(e) => e.currentTarget.style.background = 'rgba(255,255,255,0.1)'}
          >
            {isCollapsed ? '→' : '←'}
          </button>
        </div>

        {/* User Profile */}
        {user && !isCollapsed && (
          <div style={{
            padding: '1.5rem',
            borderBottom: '1px solid rgba(255,255,255,0.1)',
            display: 'flex',
            alignItems: 'center',
            gap: '0.75rem'
          }}>
            {user.picture ? (
              <img
                src={user.picture}
                alt={user.name || ''}
                style={{
                  width: '48px',
                  height: '48px',
                  borderRadius: '50%',
                  border: '2px solid rgba(255,255,255,0.1)',
                  objectFit: 'cover'
                }}
              />
            ) : (
              <div style={{
                width: '48px',
                height: '48px',
                borderRadius: '50%',
                background: 'var(--accent-purple)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 700,
                fontSize: '1.125rem',
                color: 'white'
              }}>
                {user.name?.[0]?.toUpperCase() || user.email?.[0]?.toUpperCase() || 'U'}
              </div>
            )}
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: '1rem', fontWeight: 600, lineHeight: 1.3, color: 'var(--text-primary)', marginBottom: '0.125rem' }}>
                {user.name || 'User'}
              </div>
              <div style={{ fontSize: '0.8125rem', color: 'var(--text-tertiary)', lineHeight: 1.2 }}>
                {user.email?.split('@')[0] || 'User'}
              </div>
            </div>
          </div>
        )}

        {/* Navigation Menu */}
        <nav style={{ flex: 1, padding: '1rem 0' }}>
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = currentSection === item.id;
            
            return (
              <button
                key={item.id}
                onClick={() => {
                  onSectionChange(item.id);
                }}
                style={{
                  width: '100%',
                  padding: isCollapsed ? '0.75rem 1rem' : '0.75rem 1.5rem',
                  background: isActive ? 'rgba(139, 92, 246, 0.15)' : 'transparent',
                  border: 'none',
                  borderLeft: isActive ? '3px solid var(--accent-purple)' : '3px solid transparent',
                  color: isActive ? 'var(--text-primary)' : 'var(--text-secondary)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: isCollapsed ? '0' : '0.875rem',
                  cursor: 'pointer',
                  transition: 'all var(--transition-fast)',
                  textAlign: 'left',
                  justifyContent: isCollapsed ? 'center' : 'flex-start',
                  marginBottom: '0.25rem'
                }}
                onMouseEnter={(e) => {
                  if (!isActive) {
                    e.currentTarget.style.background = 'rgba(255,255,255,0.05)';
                    e.currentTarget.style.color = 'var(--text-primary)';
                  }
                }}
                onMouseLeave={(e) => {
                  if (!isActive) {
                    e.currentTarget.style.background = 'transparent';
                    e.currentTarget.style.color = 'var(--text-secondary)';
                  }
                }}
                title={isCollapsed ? item.label : undefined}
              >
                <Icon size={20} style={{ flexShrink: 0, opacity: isActive ? 1 : 0.8 }} />
                {!isCollapsed && (
                  <span style={{ fontSize: '0.9375rem', fontWeight: isActive ? 500 : 400 }}>
                    {item.label}
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        {/* Footer */}
        {!isCollapsed && (
          <div style={{
            padding: '1rem 1.5rem',
            borderTop: '1px solid rgba(255,255,255,0.1)',
            fontSize: '0.75rem',
            opacity: 0.6,
            textAlign: 'center'
          }}>
            Tailor Platform v1.0
          </div>
        )}
      </aside>
      
      {/* Spacer for sidebar */}
      <div style={{ width: isCollapsed ? '80px' : '280px', flexShrink: 0, transition: 'width var(--transition-base)' }} />
    </>
  );
};

