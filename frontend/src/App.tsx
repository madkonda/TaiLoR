import { useCallback, useMemo, useState } from 'react';
import { GoogleAuthButton } from './components/GoogleAuthButton';
import { UploadPanel } from './components/UploadPanel';
import { FrameLog, LogEntry } from './components/FrameLog';
import { CoordinateSelectionPanel } from './components/CoordinateSelectionPanel';
import { Sidebar } from './components/Sidebar';
import { useGoogleAuth } from './hooks/useGoogleAuth';
import { FrameFile, useDrive } from './hooks/useDrive';
import { Point } from './components/FrameSelector';
import { PickerSelection } from './types';
import { MouseIcon, SegmentationIcon, AnalysisIcon, FolderIcon, CheckIcon, LoadingSpinner, FlagIcon } from './components/Icons';
import './styles/main.css';

const scopes = [
  'https://www.googleapis.com/auth/drive.file',
  'https://www.googleapis.com/auth/drive.readonly',
  'openid',
  'email',
  'profile'
];

interface ReviewStatsPayload {
  totalRows: number;
  predictedChangePoints: number;
  flaggedFrames: number;
  flaggedFramesPct: number;
  windowsCount: number;
  rowsCoveredByWindows: number;
  effectiveFps: number;
  frameStride: number;
  secondsWindow: number;
}

interface LatestResult {
  videoName: string;
  npzLink?: string;
  csvLink?: string;
  predictionLink?: string;
  flagCsvLink?: string;
  flagSummaryLink?: string;
  watchFolderLink?: string;
  watchFramesRequested?: number;
  watchFramesCopied?: number;
  reviewStats?: ReviewStatsPayload;
}

const timestamp = () => new Date().toLocaleTimeString();

const env = import.meta.env;

const googleConfig = {
  clientId: env.VITE_GOOGLE_CLIENT_ID || '',
  apiKey: env.VITE_GOOGLE_API_KEY || '',
  appId: env.VITE_GOOGLE_APP_ID || ''
};

const SAM2_API_URL = env.VITE_SAM2_API_URL || 'http://localhost:5000';

const TEMPLATE_OPTIONS = [
  { value: 'mouse_less_nest', label: 'Mouse • Reduced Nest Setup', analysisType: 'mouse', description: 'Mouse behavior analysis with minimal nest structure' },
  { value: 'mouse_nest', label: 'Mouse • Complete Nest Setup', analysisType: 'mouse', description: 'Full nest environment for comprehensive mouse analysis' },
  { value: 'rat1', label: 'Rat • Configuration 1', analysisType: 'rat', description: 'Rat behavior analysis template with nest interaction' },
  { value: 'rat2', label: 'Rat • Single Actor Setup', analysisType: 'rat_only', description: 'Isolated rat behavior without nest interaction' },
  { value: 'rat3', label: 'Rat • Configuration 3', analysisType: 'rat', description: 'Rat behavior analysis template variant 3' },
  { value: 'rat4', label: 'Rat • Configuration 4', analysisType: 'rat', description: 'Rat behavior analysis template variant 4' },
  { value: 'rat5', label: 'Rat • Configuration 5', analysisType: 'rat', description: 'Rat behavior analysis template variant 5' }
] as const;

function App() {
  const [currentSection, setCurrentSection] = useState('upload');
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [uploadedFrameFolderId, setUploadedFrameFolderId] = useState<string | null>(null);
  const [uploadedVideoFolderId, setUploadedVideoFolderId] = useState<string | null>(null);
  const [currentVideoName, setCurrentVideoName] = useState<string | null>(null);
  const [latestResult, setLatestResult] = useState<LatestResult | null>(null);
  const [frameFiles, setFrameFiles] = useState<FrameFile[]>([]);
  const [showCoordinateSelection, setShowCoordinateSelection] = useState(false);
  const [isProcessingSAM2, setIsProcessingSAM2] = useState(false);
  const [isRunningPrediction, setIsRunningPrediction] = useState(false);
  const [isGeneratingFlags, setIsGeneratingFlags] = useState(false);
  const [selectedTemplate, setSelectedTemplate] = useState<string>(TEMPLATE_OPTIONS[0]?.value ?? 'mouse_less_nest');
  const [flagsResult, setFlagsResult] = useState<LatestResult | null>(null);
  const [sam2JobId, setSam2JobId] = useState<string | null>(null);
  const [sam2JobStatus, setSam2JobStatus] = useState<string | null>(null);
  const [useLocalFrames, setUseLocalFrames] = useState(false);
  const [localFrameFolderName, setLocalFrameFolderName] = useState<string>('');
  
  const auth = useGoogleAuth({ clientId: googleConfig.clientId, scopes });
  const drive = useDrive({ accessToken: auth.accessToken, apiKey: googleConfig.apiKey, appId: googleConfig.appId });

  const selectedTemplateInfo = useMemo(
    () => TEMPLATE_OPTIONS.find((template) => template.value === selectedTemplate) ?? TEMPLATE_OPTIONS[0],
    [selectedTemplate]
  );

  const appendLog = useCallback((message: string, level: LogEntry['level'] = 'info') => {
    setLogs((previous) => [...previous, { message, level, timestamp: timestamp() }]);
  }, []);

  const ensureEnv = useCallback(() => {
    if (!googleConfig.clientId || !googleConfig.apiKey || !googleConfig.appId) {
      throw new Error('Missing Google API configuration. Please set VITE_GOOGLE_CLIENT_ID, VITE_GOOGLE_API_KEY, and VITE_GOOGLE_APP_ID.');
    }
  }, []);

  const handleUpload = useCallback(
    async (file: File, options: { fps: number; maxFrames: number }) => {
      ensureEnv();
      appendLog('Initializing Google Drive folder structure...');

      try {
        const folders = await drive.ensureStructure();
        appendLog(`Drive folders verified and ready.`, 'success');

        appendLog(`Uploading video file: ${file.name}...`);
        const uploaded = await drive.uploadVideo(file);
        appendLog(`Video successfully uploaded to Drive.`, 'success');

        appendLog(`Extracting frames at ${options.fps} fps (maximum ${options.maxFrames} frames)...`);
        let lastLoggedFrame = 0;

        const { videoFolderId, frameFolderId, videoName } = await drive.uploadFramesFromVideo(
          file,
          (progress) => {
            if (progress.stage === 'extract-frames' && progress.completedFrames && progress.totalFrames) {
              if (progress.completedFrames === progress.totalFrames || progress.completedFrames - lastLoggedFrame >= 5) {
                appendLog(`Frame extraction progress: ${progress.completedFrames} / ${progress.totalFrames} frames processed...`);
                lastLoggedFrame = progress.completedFrames;
              }
            }
          },
          { fps: options.fps, maxFrames: options.maxFrames }
        );

        setUploadedVideoFolderId(videoFolderId);
        setUploadedFrameFolderId(frameFolderId);
        setCurrentVideoName(videoName);
        setLatestResult(null);
        appendLog('Loading frames for coordinate annotation...');
        const files = await drive.getFrameFiles(frameFolderId, 200);
        setFrameFiles(files);
        setShowCoordinateSelection(true);
        setCurrentSection('segmentation'); // Auto-navigate to segmentation
        appendLog(`Successfully loaded ${files.length} frames ready for annotation.`, 'success');
      } catch (error) {
        const message = error instanceof Error ? error.message : 'Upload and frame extraction failed.';
        appendLog(message, 'error');
      }
    },
    [drive, appendLog, ensureEnv]
  );

  const handleCancelCoordinateSelection = useCallback(() => {
    setShowCoordinateSelection(false);
    setFrameFiles([]);
    appendLog('Coordinate annotation cancelled by user.');
  }, [appendLog]);

  const handleSAM2Process = useCallback(
    async (
      nestPoint: Point | undefined,
      mousePoint: Point | undefined,
      selectedFrameIndex: number,
      nestBox?: [number, number, number, number],
      mouseBox?: [number, number, number, number]
    ) => {
      // For local frames, need folder name + video_folder_id. For Drive, need frame_folder_id + video_folder_id
      if (useLocalFrames) {
        if (!localFrameFolderName || !uploadedVideoFolderId || !auth.accessToken) {
          appendLog('Missing required data for SAM2 segmentation. Please provide local frame folder name and select Drive video folder for NPZ upload.', 'error');
          return;
        }
      } else {
        if (!uploadedFrameFolderId || !uploadedVideoFolderId || !auth.accessToken) {
          appendLog('Missing required data for SAM2 segmentation. Please ensure frames are uploaded and coordinates are selected.', 'error');
          return;
        }
      }

      // Require either both points or both boxes
      const hasPoints = !!nestPoint && !!mousePoint;
      const hasBoxes = !!nestBox && !!mouseBox;
      if (!hasPoints && !hasBoxes) {
        appendLog('Please provide either both nest & rat points, or both bounding boxes before running SAM2.', 'error');
        return;
      }

      setIsProcessingSAM2(true);
      appendLog('Initializing SAM2 video segmentation model...', 'info');
      if (nestPoint && mousePoint) {
        appendLog(
          `Annotation frame: ${selectedFrameIndex}, Nest point: (${nestPoint.x}, ${nestPoint.y}), Subject point: (${mousePoint.x}, ${mousePoint.y})`,
          'info'
        );
      } else {
        appendLog(
          `Annotation frame: ${selectedFrameIndex}, using bounding boxes only (no explicit points).`,
          'info'
        );
      }

      try {
        const payload: any = {
          access_token: auth.accessToken,
          video_folder_id: uploadedVideoFolderId,
          ann_frame_idx: selectedFrameIndex,
          fixed_points_template: selectedTemplate,
          analysis_type: selectedTemplateInfo?.analysisType ?? 'mouse',
          run_prediction: false,
        };

        // Use local frames or Drive frames
        if (useLocalFrames) {
          payload.frame_folder_name = localFrameFolderName;
        } else {
          payload.frame_folder_id = uploadedFrameFolderId;
        }

        if (nestPoint && mousePoint) {
          payload.nest_point = { x: nestPoint.x, y: nestPoint.y };
          payload.mouse_point = { x: mousePoint.x, y: mousePoint.y };
        }

        if (nestBox && mouseBox) {
          payload.nest_box = nestBox;
          payload.mouse_box = mouseBox;
        }

        const response = await fetch(`${SAM2_API_URL}/process-sam2`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (!response.ok) {
          const errorData = await response.json().catch(() => ({}));
          throw new Error(errorData.error || `Server error: ${response.status} ${response.statusText}`);
        }

        const startPayload = await response.json();
        const jobId = startPayload.job_id as string | undefined;
        if (!jobId) {
          throw new Error('Server did not return a job_id for SAM2 processing.');
        }

        setSam2JobId(jobId);
        setSam2JobStatus('queued');
        appendLog(`SAM2 job queued with ID: ${jobId}`, 'info');

        // Poll backend for job completion
        const pollIntervalMs = 5000;
        const maxPollMinutes = 60; // safety cap
        const maxPolls = (maxPollMinutes * 60 * 1000) / pollIntervalMs;
        let polls = 0;

        const pollJob = async () => {
          polls += 1;
          try {
            const statusResponse = await fetch(`${SAM2_API_URL}/jobs/${jobId}`);
            if (!statusResponse.ok) {
              const errorData = await statusResponse.json().catch(() => ({}));
              throw new Error(errorData.error || `Status check failed: ${statusResponse.status}`);
            }

            const job = await statusResponse.json();
            const status = job.status as string | undefined;
            const progress = job.progress as { stage?: string } | undefined;
            setSam2JobStatus(status || null);

            if (progress?.stage) {
              appendLog(`SAM2 job status: ${status ?? 'unknown'} (${progress.stage})`, 'info');
            } else if (status) {
              appendLog(`SAM2 job status: ${status}`, 'info');
            }

            if (status === 'completed') {
              const result = job.result as any;
              appendLog(`SAM2 segmentation completed successfully. Processed ${result?.num_frames_processed || 0} frames across the video sequence.`, 'success');
              appendLog('Mask archive (NPZ file) has been generated and saved to Drive.', 'success');
              setLatestResult({
                videoName: currentVideoName ?? 'video',
                npzLink: result?.npz_drive_link,
              });
              setShowCoordinateSelection(false);
              setCurrentSection('prediction'); // Auto-navigate to prediction
              setIsProcessingSAM2(false);
              return;
            }

            if (status === 'failed') {
              const errorMessage = job.error || 'SAM2 job failed.';
              appendLog(errorMessage, 'error');
              setIsProcessingSAM2(false);
              return;
            }

            if (polls >= maxPolls) {
              appendLog('SAM2 job polling timed out. Please check the backend logs.', 'error');
              setIsProcessingSAM2(false);
              return;
            }

            // Continue polling
            setTimeout(pollJob, pollIntervalMs);
          } catch (err) {
            const message = err instanceof Error ? err.message : 'SAM2 job status check failed.';
            appendLog(message, 'error');
            setIsProcessingSAM2(false);
          }
        };

        // Start first poll
        setTimeout(pollJob, pollIntervalMs);
      } catch (error) {
        const message = error instanceof Error ? error.message : 'SAM2 segmentation processing failed.';
        appendLog(message, 'error');
      } finally {
        // NOTE: we keep isProcessingSAM2 true while polling;
        // it will be turned off when the job completes/fails or times out.
      }
    },
    [uploadedFrameFolderId, uploadedVideoFolderId, auth.accessToken, selectedTemplate, selectedTemplateInfo, currentVideoName, appendLog]
  );

  const handleRunPredictionFromDrive = useCallback(async () => {
    if (!auth.accessToken) {
      appendLog('Authentication required. Please sign in with Google first.', 'error');
      return;
    }

    setIsRunningPrediction(true);
    appendLog('Opening file selector to choose NPZ file...', 'info');

    try {
      await drive.openPicker('results', async (selection) => {
        if (selection.length === 0) return;
        const selectedItem = selection[0];
        try {
          // Only accept NPZ files for prediction
          const fileInfo = await drive.getFileInfo(selectedItem.id, 'id,name,mimeType,parents');
          
          if (!selectedItem.name?.toLowerCase().endsWith('.npz')) {
            throw new Error('Please select an NPZ file (output from SAM2 segmentation).');
          }

          const npzFileId = selectedItem.id;
          let videoName = selectedItem.name.replace('.npz', '');

          const parentId = fileInfo?.parents?.[0];
          if (!parentId) {
            throw new Error('Could not determine video folder from NPZ file location.');
          }

          const videoFolderId = parentId;
          const parentInfo = await drive.getFileInfo(videoFolderId, 'name');
          videoName = parentInfo?.name || videoName;

          appendLog(`Selected NPZ file: ${selectedItem.name}`, 'success');

          appendLog(`Running geometric feature extraction with template: ${selectedTemplateInfo?.label || selectedTemplate}...`, 'info');
          appendLog('Computing behavioral features from segmentation masks...', 'info');
          
          const response = await fetch(`${SAM2_API_URL}/run-prediction`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              access_token: auth.accessToken,
              npz_file_id: npzFileId,
              video_folder_id: videoFolderId,
              fixed_points_template: selectedTemplate,
              analysis_type: selectedTemplateInfo?.analysisType ?? 'mouse'
            })
          });

          if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `Server error: ${response.status}`);
          }

          const result = await response.json();
          appendLog('Feature extraction completed successfully.', 'success');
          appendLog('Behavioral prediction model executed. Results ready for analysis.', 'success');

          setLatestResult({
            videoName: videoName || result.video_name || 'video',
            npzLink: result.npz_drive_link,
            csvLink: result.csv_drive_link,
            predictionLink: result.prediction_drive_link,
          });

        } catch (error) {
          const message = error instanceof Error ? error.message : 'Feature extraction and prediction failed.';
          appendLog(message, 'error');
        } finally {
          setIsRunningPrediction(false);
        }
      });
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to open file selector.';
      appendLog(message, 'error');
      setIsRunningPrediction(false);
    }
  }, [auth.accessToken, drive, selectedTemplate, selectedTemplateInfo, appendLog]);

  // Reference Images Component
  const ReferenceImagesSection = () => (
    <div className="card" style={{ background: 'white' }}>
      <div className="card-header">
        <div className="card-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <MouseIcon size={24} />
          Reference Images & Examples
        </div>
        <p className="card-subtitle">
          Reference images for coordinate annotation and setup guidelines
        </p>
      </div>
      <div className="card-body">
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '1.5rem',
          marginTop: '1rem'
        }}>
          {/* Placeholder for reference images - user can add actual images here */}
          <div style={{
            padding: '2rem',
            background: 'var(--bg-secondary)',
            borderRadius: 'var(--radius-lg)',
            border: '2px dashed var(--border-medium)',
            textAlign: 'center'
          }}>
            <MouseIcon size={48} style={{ color: 'var(--text-tertiary)', marginBottom: '1rem', opacity: 0.5 }} />
            <p style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Example 1: Mouse Nest Setup</p>
            <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
              Reference image showing proper nest and mouse coordinate placement
            </p>
          </div>
          
          <div style={{
            padding: '2rem',
            background: 'var(--bg-secondary)',
            borderRadius: 'var(--radius-lg)',
            border: '2px dashed var(--border-medium)',
            textAlign: 'center'
          }}>
            <SegmentationIcon size={48} style={{ color: 'var(--text-tertiary)', marginBottom: '1rem', opacity: 0.5 }} />
            <p style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Example 2: Segmentation Result</p>
            <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
              Example of SAM2 segmentation mask overlay on behavioral video frame
            </p>
          </div>

          <div style={{
            padding: '2rem',
            background: 'var(--bg-secondary)',
            borderRadius: 'var(--radius-lg)',
            border: '2px dashed var(--border-medium)',
            textAlign: 'center'
          }}>
            <AnalysisIcon size={48} style={{ color: 'var(--text-tertiary)', marginBottom: '1rem', opacity: 0.5 }} />
            <p style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Example 3: Feature Analysis</p>
            <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
              Sample output showing geometric features and behavioral predictions
            </p>
          </div>
        </div>
        
        <div style={{ marginTop: '2rem', padding: '1.5rem', background: 'var(--info-light)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--info)' }}>
          <p style={{ margin: 0, fontSize: '0.9375rem', color: 'var(--primary-900)', lineHeight: 1.6 }}>
            <strong>Note:</strong> To add your own reference images, place them in the <code>frontend/public/reference-images/</code> directory 
            and update this component to display them. These images help guide users on proper coordinate placement and expected results.
          </p>
        </div>
      </div>
    </div>
  );

  return (
    <div style={{ 
      minHeight: '100vh', 
      background: 'var(--bg-primary)',
      display: 'flex',
      color: 'var(--text-primary)'
    }}>
      {/* Sidebar */}
      {auth.isAuthenticated && (
        <Sidebar 
          currentSection={currentSection} 
          onSectionChange={setCurrentSection}
          user={auth.user}
        />
      )}

      {/* Main Content Area */}
      <div style={{ 
        flex: 1, 
        display: 'flex', 
        flexDirection: 'column',
        marginLeft: auth.isAuthenticated ? 0 : 0,
        background: 'var(--bg-primary)'
      }}>
        {/* Top Header Bar */}
        {auth.isAuthenticated && (
          <header style={{
            background: 'var(--bg-secondary)',
            padding: '1.5rem 2rem',
            borderBottom: '1px solid var(--border-light)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            position: 'sticky',
            top: 0,
            zIndex: 100
          }}>
            <div>
              <h2 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 600, color: 'var(--text-primary)' }}>
                {currentSection === 'upload' && 'Upload & Extract'}
                {currentSection === 'segmentation' && 'Segmentation'}
                {currentSection === 'prediction' && 'Prediction'}
                {currentSection === 'flags' && 'Review Flags'}
                {currentSection === 'reference' && 'Reference'}
              </h2>
              <p style={{ margin: '0.25rem 0 0 0', fontSize: '0.875rem', color: 'var(--text-tertiary)' }}>
                {currentSection === 'upload' && 'Upload videos and extract frames'}
                {currentSection === 'segmentation' && 'Run SAM2 segmentation'}
                {currentSection === 'prediction' && 'Generate predictions'}
                {currentSection === 'flags' && 'Flag frames for review'}
                {currentSection === 'reference' && 'View examples'}
              </p>
            </div>
            <button
              onClick={auth.signOut}
              className="btn btn-secondary"
            >
              Sign Out
            </button>
          </header>
        )}

        {/* Main Content */}
        <main style={{ 
          flex: 1, 
          padding: '2rem',
          overflowY: 'auto',
          background: 'var(--bg-primary)'
        }}>
          {!auth.isAuthenticated ? (
            <div className="auth-layout">
              <div className="auth-hero">
                <div className="auth-hero-overlay">
                  <div className="auth-badge">
                    <MouseIcon size={28} style={{ color: 'white' }} />
                  </div>
                  <h1>Tailor</h1>
                  <p>Precision segmentation and behavioral analytics for lab rodents.</p>
                  <ul>
                    <li>Streamline Drive uploads and frame extraction in one workflow.</li>
                    <li>Annotate once, propagate masks with SAM2 across hundreds of frames.</li>
                    <li>Generate geometric features and decision-tree predictions instantly.</li>
                  </ul>
                </div>
              </div>
              <div className="auth-panel card">
                <div className="auth-panel-header">
                  <h2>Welcome back</h2>
                  <p>Sign in with your lab account to continue.</p>
                </div>
                <GoogleAuthButton onSignIn={auth.signIn} isReady={auth.isReady} />
                <div className="auth-panel-footer">
                  <span>Securely connects to Google Drive &amp; Picker APIs.</span>
                </div>
              </div>
            </div>
          ) : (
            <>
              {/* Upload Section */}
              {currentSection === 'upload' && (
                <section className="card" style={{ marginBottom: '2rem' }}>
                  <div className="card-body">
                    <UploadPanel disabled={!auth.isAuthenticated} onUpload={handleUpload} />
                  </div>
                </section>
              )}

              {/* Segmentation Section */}
              {currentSection === 'segmentation' && (
                <>
                  <section className="card" style={{ marginBottom: '2rem' }}>
                    <div className="card-header">
                      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem', flex: 1 }}>
                        <div style={{
                          width: '48px',
                          height: '48px',
                          borderRadius: 'var(--radius-lg)',
                          background: 'linear-gradient(135deg, var(--accent-teal) 0%, #0d9488 100%)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          flexShrink: 0,
                          boxShadow: 'var(--shadow-md)'
                        }}>
                          <SegmentationIcon size={24} style={{ color: 'white' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <div className="card-title" style={{ marginBottom: '0.5rem' }}>
                            SAM2 Video Segmentation
                          </div>
                          <p className="card-subtitle" style={{ margin: 0 }}>
                            Select annotation points on key frames to guide the SAM2 model in segmenting subjects and objects 
                            across the entire video sequence. The model propagates segmentation masks frame-by-frame for comprehensive analysis.
                          </p>
                        </div>
                      </div>
                      {isProcessingSAM2 && (
                        <div className="status-indicator" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.5rem 1rem', background: 'var(--warning-light)', borderRadius: 'var(--radius-md)' }}>
                          <span className="status-dot processing"></span>
                          <span style={{ fontSize: '0.875rem', fontWeight: 600, color: 'var(--warning)' }}>Processing Segmentation...</span>
                        </div>
                      )}
                    </div>
                    <div className="card-body">
                      {!showCoordinateSelection ? (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                          <div style={{
                            padding: '1.5rem',
                            background: 'var(--bg-secondary)',
                            borderRadius: 'var(--radius-lg)',
                            border: '1px solid var(--border-light)'
                          }}>
                            <p style={{ marginBottom: '1rem', color: 'var(--text-secondary)', lineHeight: 1.6 }}>
                              Choose an existing video dataset from your Drive workspace, use local frames already on the VM, or proceed with frames extracted in Step 1. 
                              You'll then annotate key coordinates on a representative frame to guide the segmentation process.
                            </p>
                            
                            <div style={{ marginBottom: '1rem', padding: '1rem', background: 'var(--bg-primary)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem', cursor: 'pointer' }}>
                                <input
                                  type="checkbox"
                                  checked={useLocalFrames}
                                  onChange={(e) => {
                                    setUseLocalFrames(e.target.checked);
                                    if (!e.target.checked) {
                                      setLocalFrameFolderName('');
                                    }
                                  }}
                                  style={{ cursor: 'pointer' }}
                                />
                                <span style={{ fontWeight: 600 }}>Use local frames (already on VM)</span>
                              </label>
                              {useLocalFrames && (
                                <div style={{ marginTop: '0.75rem' }}>
                                  <label className="form-label" style={{ fontSize: '0.875rem', marginBottom: '0.25rem', display: 'block' }}>
                                    Frame folder name (e.g., "12-1_2_frames")
                                  </label>
                                  <input
                                    className="form-input"
                                    type="text"
                                    value={localFrameFolderName}
                                    onChange={(e) => setLocalFrameFolderName(e.target.value)}
                                    placeholder="12-1_2_frames"
                                    style={{ width: '100%', marginBottom: '0.5rem' }}
                                  />
                                  <div className="form-help" style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>
                                    Frames should be in: backend VM path …/videos/{'{folder_name}'}/
                                  </div>
                                  <div style={{ marginTop: '0.75rem', padding: '0.75rem', background: 'var(--info-light)', borderRadius: 'var(--radius-md)', fontSize: '0.875rem' }}>
                                    <strong>Note:</strong> You still need to select the Drive video folder below to specify where the NPZ file should be uploaded.
                                  </div>
                                </div>
                              )}
                            </div>

                            {!useLocalFrames && (
                              <button
                                className="btn btn-primary btn-lg"
                                onClick={async () => {
                                try {
                                  await drive.openPicker('results', async (selection) => {
                                    if (selection.length === 0) return;
                                    const selectedItem = selection[0];
                                    try {
                                      const resolved = await drive.resolveVideoFolder(selectedItem.id);
                                      setUploadedVideoFolderId(resolved.videoFolderId);
                                      setUploadedFrameFolderId(resolved.frameFolderId);
                                      setCurrentVideoName(resolved.videoName);
                                      setLatestResult(null);
                                      appendLog('Loading frames for coordinate annotation...');
                                      const files = await drive.getFrameFiles(resolved.frameFolderId, 200);
                                      if (files.length === 0) {
                                        appendLog('No frames found in the selected video folder. Please ensure frames have been extracted.', 'error');
                                        return;
                                      }
                                      setFrameFiles(files);
                                      setShowCoordinateSelection(true);
                                      appendLog(`Successfully loaded ${files.length} frames for annotation.`, 'success');
                                    } catch (error) {
                                      const message = error instanceof Error ? error.message : 'Failed to resolve selected folder structure.';
                                      appendLog(message, 'error');
                                    }
                                  });
                                } catch (error) {
                                  const message = error instanceof Error ? error.message : 'Failed to open file selector.';
                                  appendLog(message, 'error');
                                }
                              }}
                              disabled={isProcessingSAM2 || !auth.isAuthenticated}
                              style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
                            >
                              <FolderIcon size={20} />
                              Browse Video Datasets from Drive
                            </button>
                            )}

                            {useLocalFrames && (
                              <>
                                <button
                                  className="btn btn-primary btn-lg"
                                  onClick={async () => {
                                    try {
                                      await drive.openPicker('results', async (selection) => {
                                        if (selection.length === 0) return;
                                        const selectedItem = selection[0];
                                        try {
                                          const resolved = await drive.resolveVideoFolder(selectedItem.id);
                                          setUploadedVideoFolderId(resolved.videoFolderId);
                                          setCurrentVideoName(resolved.videoName);
                                          setLatestResult(null);
                                          appendLog(`Selected Drive video folder: ${resolved.videoName} (NPZ will be uploaded here)`, 'success');
                                          appendLog(`Using local frames from: ${localFrameFolderName}`, 'info');
                                          setShowCoordinateSelection(true);
                                        } catch (error) {
                                          const message = error instanceof Error ? error.message : 'Failed to resolve selected folder structure.';
                                          appendLog(message, 'error');
                                        }
                                      });
                                    } catch (error) {
                                      const message = error instanceof Error ? error.message : 'Failed to open file selector.';
                                      appendLog(message, 'error');
                                    }
                                  }}
                                  disabled={isProcessingSAM2 || !auth.isAuthenticated || !localFrameFolderName.trim()}
                                  style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem', marginTop: '0.5rem' }}
                                >
                                  <FolderIcon size={20} />
                                  Select Drive Video Folder (for NPZ upload)
                                </button>
                              </>
                            )}
                          </div>
                        </div>
                      ) : (
                        <div style={{
                          padding: '1.5rem',
                          background: 'linear-gradient(135deg, var(--primary-50) 0%, var(--accent-teal) 0.05)',
                          borderRadius: 'var(--radius-lg)',
                          border: '2px solid var(--accent-teal)'
                        }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
                            <CheckIcon size={20} style={{ color: 'var(--accent-teal)' }} />
                            <p style={{ margin: 0, fontWeight: 600, color: 'var(--text-primary)' }}>
                              Annotation Interface Active
                            </p>
                          </div>
                          <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap' }}>
                            <div>
                              <span style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>Dataset:</span>
                              <strong style={{ marginLeft: '0.5rem', color: 'var(--text-primary)' }}>
                                {currentVideoName || 'video dataset'}
                              </strong>
                            </div>
                            <div>
                              <span style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>Available Frames:</span>
                              <strong style={{ marginLeft: '0.5rem', color: 'var(--text-primary)' }}>
                                {frameFiles.length}
                              </strong>
                            </div>
                          </div>
                        </div>
                      )}
                    </div>
                  </section>

                  {showCoordinateSelection && !useLocalFrames && frameFiles.length > 0 && auth.accessToken && (
                    <section className="card" style={{
                      border: '2px solid var(--accent-teal)',
                      boxShadow: '0 0 0 1px rgba(20, 184, 166, 0.2)'
                    }}>
                      <div style={{ paddingBottom: '1rem', borderBottom: '2px solid var(--border-light)', marginBottom: '1.5rem' }}>
                        <h3 style={{ margin: 0, fontSize: '1.25rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                          <SegmentationIcon size={24} style={{ color: 'var(--accent-teal)' }} />
                          Coordinate Annotation Interface
                        </h3>
                        <p style={{ margin: '0.5rem 0 0 0', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                          Select a frame and click to mark nest and subject coordinates. These points guide the SAM2 model's segmentation across all frames.
                        </p>
                      </div>
                      <CoordinateSelectionPanel
                        frameFiles={frameFiles}
                        accessToken={auth.accessToken}
                        onConfirm={handleSAM2Process}
                        onCancel={handleCancelCoordinateSelection}
                        disabled={isProcessingSAM2 || !auth.isAuthenticated}
                      />
                    </section>
                  )}

                  {showCoordinateSelection && useLocalFrames && auth.accessToken && (
                    <section className="card" style={{
                      border: '2px solid var(--accent-teal)',
                      boxShadow: '0 0 0 1px rgba(20, 184, 166, 0.2)'
                    }}>
                      <div style={{ paddingBottom: '1rem', borderBottom: '2px solid var(--border-light)', marginBottom: '1.5rem' }}>
                        <h3 style={{ margin: 0, fontSize: '1.25rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                          <SegmentationIcon size={24} style={{ color: 'var(--accent-teal)' }} />
                          Local Frames Configuration
                        </h3>
                        <p style={{ margin: '0.5rem 0 0 0', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                          Provide bounding boxes or points for SAM2 segmentation. Frame index defaults to 0.
                        </p>
                      </div>
                      <CoordinateSelectionPanel
                        frameFiles={[]}
                        accessToken={auth.accessToken}
                        onConfirm={handleSAM2Process}
                        onCancel={handleCancelCoordinateSelection}
                        disabled={isProcessingSAM2 || !auth.isAuthenticated}
                      />
                    </section>
                  )}
                </>
              )}

              {/* Prediction Section */}
              {currentSection === 'prediction' && (
                <section className="card" style={{ marginBottom: '2rem' }}>
                  <div className="card-header">
                    <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem', flex: 1 }}>
                      <div style={{
                        width: '48px',
                        height: '48px',
                        borderRadius: 'var(--radius-lg)',
                        background: 'linear-gradient(135deg, var(--accent-purple) 0%, #7c3aed 100%)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flexShrink: 0,
                        boxShadow: 'var(--shadow-md)'
                      }}>
                        <AnalysisIcon size={24} style={{ color: 'white' }} />
                      </div>
                      <div style={{ flex: 1 }}>
                        <div className="card-title" style={{ marginBottom: '0.5rem' }}>
                          Feature Extraction & Behavioral Prediction
                        </div>
                        <p className="card-subtitle" style={{ margin: 0 }}>
                          Extract geometric and temporal features from segmentation masks, then run behavioral prediction models 
                          to classify activities and generate comprehensive analysis reports.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div className="card-body">
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
                      <div className="form-group">
                        <label className="form-label" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '1rem', fontWeight: 600 }}>
                          <AnalysisIcon size={20} />
                          Analysis Template & Model Configuration
                        </label>
                        <select
                          className="form-select"
                          value={selectedTemplate}
                          onChange={(e) => setSelectedTemplate(e.target.value)}
                          disabled={isProcessingSAM2 || isRunningPrediction}
                          style={{ fontSize: '0.9375rem', padding: '0.75rem 1rem' }}
                        >
                          {TEMPLATE_OPTIONS.map((option) => (
                            <option key={option.value} value={option.value}>
                              {option.label}
                            </option>
                          ))}
                        </select>
                        <div className="form-help" style={{ marginTop: '0.5rem', fontSize: '0.875rem', lineHeight: 1.6 }}>
                          {selectedTemplateInfo?.description || 'Select the appropriate template based on your experimental setup and analysis requirements.'}
                        </div>
                      </div>

                      <button
                        className="btn btn-primary btn-lg"
                        onClick={handleRunPredictionFromDrive}
                        disabled={!auth.isAuthenticated || isRunningPrediction || isProcessingSAM2}
                        style={{
                          width: '100%',
                          justifyContent: 'center',
                          padding: '1rem 2rem',
                          fontSize: '1rem',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.75rem'
                        }}
                      >
                        {isRunningPrediction ? (
                          <>
                            <LoadingSpinner size={20} />
                            Processing Features & Running Predictions...
                          </>
                        ) : (
                          <>
                            <AnalysisIcon size={24} />
                            Select NPZ Archive & Run Analysis
                          </>
                        )}
                      </button>

                      {latestResult && (
                        <div style={{
                          padding: '2rem',
                          background: 'linear-gradient(135deg, var(--success-light) 0%, #d1fae5 100%)',
                          borderRadius: 'var(--radius-xl)',
                          border: '2px solid var(--success)',
                          boxShadow: 'var(--shadow-lg)'
                        }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
                            <div style={{
                              width: '48px',
                              height: '48px',
                              borderRadius: '50%',
                              background: 'var(--success)',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              flexShrink: 0
                            }}>
                              <CheckIcon size={24} style={{ color: 'white' }} />
                            </div>
                            <div>
                              <h4 style={{ margin: 0, fontSize: '1.25rem', fontWeight: 700, color: '#065f46' }}>
                                Analysis Complete
                              </h4>
                              <p style={{ margin: '0.25rem 0 0 0', fontSize: '0.875rem', color: '#047857' }}>
                                Results available for dataset: <strong>{latestResult.videoName}</strong>
                              </p>
                            </div>
                          </div>
                          
                          <div style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                            gap: '1rem',
                            marginTop: '1.5rem'
                          }}>
                            {latestResult.npzLink && (
                              <a
                                href={latestResult.npzLink}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="btn btn-outline"
                                style={{
                                  display: 'flex',
                                  flexDirection: 'column',
                                  alignItems: 'center',
                                  gap: '0.5rem',
                                  padding: '1rem',
                                  textAlign: 'center',
                                  borderColor: 'var(--success)',
                                  color: '#065f46'
                                }}
                              >
                                <span style={{ fontSize: '1.5rem' }}>📦</span>
                                <span style={{ fontWeight: 600 }}>Segmentation Masks</span>
                                <span style={{ fontSize: '0.75rem', opacity: 0.8 }}>NPZ Archive</span>
                              </a>
                            )}
                            {latestResult.csvLink && (
                              <a
                                href={latestResult.csvLink}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="btn btn-outline"
                                style={{
                                  display: 'flex',
                                  flexDirection: 'column',
                                  alignItems: 'center',
                                  gap: '0.5rem',
                                  padding: '1rem',
                                  textAlign: 'center',
                                  borderColor: 'var(--success)',
                                  color: '#065f46'
                                }}
                              >
                                <span style={{ fontSize: '1.5rem' }}>📊</span>
                                <span style={{ fontWeight: 600 }}>Geometric Features</span>
                                <span style={{ fontSize: '0.75rem', opacity: 0.8 }}>CSV Data</span>
                              </a>
                            )}
                            {latestResult.predictionLink && (
                              <a
                                href={latestResult.predictionLink}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="btn btn-success"
                                style={{
                                  display: 'flex',
                                  flexDirection: 'column',
                                  alignItems: 'center',
                                  gap: '0.5rem',
                                  padding: '1rem',
                                  textAlign: 'center',
                                  background: 'var(--success)',
                                  color: 'white'
                                }}
                              >
                                <span style={{ fontSize: '1.5rem' }}>🎯</span>
                                <span style={{ fontWeight: 600 }}>Behavioral Predictions</span>
                                <span style={{ fontSize: '0.75rem', opacity: 0.9 }}>Activity Classification</span>
                              </a>
                            )}
                          </div>
                        </div>
                      )}

                      {!latestResult && (
                        <div style={{
                          padding: '2rem',
                          background: 'var(--bg-secondary)',
                          borderRadius: 'var(--radius-lg)',
                          textAlign: 'center',
                          border: '1px dashed var(--border-medium)'
                        }}>
                          <AnalysisIcon size={48} style={{ color: 'var(--text-tertiary)', marginBottom: '1rem', opacity: 0.5 }} />
                          <p style={{ margin: 0, color: 'var(--text-secondary)', fontSize: '0.9375rem', lineHeight: 1.6 }}>
                            Complete SAM2 segmentation first to generate mask archives (NPZ files). 
                            Then run feature extraction and behavioral prediction analysis on the results.
                          </p>
                        </div>
                      )}
                    </div>
                  </div>
                </section>
              )}

              {/* Review Flags Section */}
              {currentSection === 'flags' && (
                <section className="card" style={{ marginBottom: '2rem' }}>
                  <div className="card-header">
                    <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem', flex: 1 }}>
                      <div style={{
                        width: '48px',
                        height: '48px',
                        borderRadius: 'var(--radius-lg)',
                        background: 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flexShrink: 0,
                        boxShadow: 'var(--shadow-md)'
                      }}>
                        <FlagIcon size={24} style={{ color: 'white' }} />
                      </div>
                      <div style={{ flex: 1 }}>
                        <div className="card-title" style={{ marginBottom: '0.5rem' }}>
                          Review Flags & Watch List
                        </div>
                        <p className="card-subtitle" style={{ margin: 0 }}>
                          Generate review flags from prediction CSVs to identify frames around behavior changes. 
                          Flagged frames are copied to the <code>watch/</code> folder for manual review.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div className="card-body">
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
                      <div className="form-group">
                        <label className="form-label" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '1rem', fontWeight: 600 }}>
                          <FlagIcon size={20} />
                          Window Configuration
                        </label>
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
                          <div>
                            <label className="form-label" style={{ fontSize: '0.875rem' }}>Video FPS</label>
                            <input
                              className="form-input"
                              type="number"
                              min={1}
                              max={120}
                              step={1}
                              defaultValue={30}
                              id="flags-fps-video"
                              placeholder="30"
                            />
                            <div className="form-help" style={{ fontSize: '0.75rem' }}>Source video frame rate</div>
                          </div>
                          <div>
                            <label className="form-label" style={{ fontSize: '0.875rem' }}>Frame Stride</label>
                            <input
                              className="form-input"
                              type="number"
                              min={1}
                              max={100}
                              step={1}
                              defaultValue={10}
                              id="flags-frame-stride"
                              placeholder="10"
                            />
                            <div className="form-help" style={{ fontSize: '0.75rem' }}>Every Nth frame extracted</div>
                          </div>
                          <div>
                            <label className="form-label" style={{ fontSize: '0.875rem' }}>Window (seconds)</label>
                            <input
                              className="form-input"
                              type="number"
                              min={0.5}
                              max={10}
                              step={0.5}
                              defaultValue={3.0}
                              id="flags-seconds-window"
                              placeholder="3.0"
                            />
                            <div className="form-help" style={{ fontSize: '0.75rem' }}>Window around changes</div>
                          </div>
                        </div>
                      </div>

                      <button
                        className="btn btn-primary btn-lg"
                        onClick={async () => {
                          if (!auth.accessToken) {
                            appendLog('Authentication required. Please sign in with Google first.', 'error');
                            return;
                          }

                          setIsGeneratingFlags(true);
                          appendLog('Opening file selector to choose prediction CSV...', 'info');

                          try {
                            await drive.openPicker('results', async (selection) => {
                              if (selection.length === 0) return;
                              const selectedItem = selection[0];
                              
                              if (!selectedItem.name?.toLowerCase().endsWith('output.csv')) {
                                appendLog('Please select a prediction CSV file (ending in "output.csv").', 'error');
                                setIsGeneratingFlags(false);
                                return;
                              }

                              try {
                                const fpsVideo = parseFloat((document.getElementById('flags-fps-video') as HTMLInputElement)?.value || '30');
                                const frameStride = parseInt((document.getElementById('flags-frame-stride') as HTMLInputElement)?.value || '10');
                                const secondsWindow = parseFloat((document.getElementById('flags-seconds-window') as HTMLInputElement)?.value || '3.0');

                                appendLog(`Selected prediction CSV: ${selectedItem.name}`, 'success');
                                appendLog(`Generating review flags (window: ${secondsWindow}s, FPS: ${fpsVideo}, stride: ${frameStride})...`, 'info');

                                const response = await fetch(`${SAM2_API_URL}/generate-review-flags`, {
                                  method: 'POST',
                                  headers: { 'Content-Type': 'application/json' },
                                  body: JSON.stringify({
                                    access_token: auth.accessToken,
                                    prediction_csv_file_id: selectedItem.id,
                                    fps_video: fpsVideo,
                                    frame_stride: frameStride,
                                    seconds_window: secondsWindow,
                                  })
                                });

                                if (!response.ok) {
                                  const errorData = await response.json().catch(() => ({}));
                                  throw new Error(errorData.error || `Server error: ${response.status}`);
                                }

                                const result = await response.json();
                                appendLog('Review flags generated successfully.', 'success');
                                appendLog(`Flagged ${result.review_stats.flagged_frames} frames (${result.review_stats.flagged_frames_pct}%) in ${result.review_stats.windows_count} windows.`, 'success');
                                appendLog(`Copied ${result.watch_frames_copied} frames to watch/ folder.`, 'success');

                                const reviewStatsPayload: ReviewStatsPayload = {
                                  totalRows: result.review_stats.total_rows,
                                  predictedChangePoints: result.review_stats.predicted_change_points,
                                  flaggedFrames: result.review_stats.flagged_frames,
                                  flaggedFramesPct: result.review_stats.flagged_frames_pct,
                                  windowsCount: result.review_stats.windows_count,
                                  rowsCoveredByWindows: result.review_stats.rows_covered_by_windows,
                                  effectiveFps: result.review_stats.effective_fps,
                                  frameStride: result.review_stats.frame_stride,
                                  secondsWindow: result.review_stats.seconds_window,
                                };

                                setFlagsResult({
                                  videoName: result.video_name || 'video',
                                  flagCsvLink: result.flag_csv_drive_link,
                                  flagSummaryLink: result.flag_summary_drive_link,
                                  watchFolderLink: result.watch_folder_link,
                                  watchFramesRequested: result.watch_frames_requested,
                                  watchFramesCopied: result.watch_frames_copied,
                                  reviewStats: reviewStatsPayload,
                                });
                              } catch (error) {
                                const message = error instanceof Error ? error.message : 'Review flag generation failed.';
                                appendLog(message, 'error');
                              } finally {
                                setIsGeneratingFlags(false);
                              }
                            });
                          } catch (error) {
                            const message = error instanceof Error ? error.message : 'Failed to open file selector.';
                            appendLog(message, 'error');
                            setIsGeneratingFlags(false);
                          }
                        }}
                        disabled={!auth.isAuthenticated || isGeneratingFlags}
                        style={{
                          width: '100%',
                          justifyContent: 'center',
                          padding: '1rem 2rem',
                          fontSize: '1rem',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.75rem'
                        }}
                      >
                        {isGeneratingFlags ? (
                          <>
                            <LoadingSpinner size={20} />
                            Generating Review Flags...
                          </>
                        ) : (
                          <>
                            <FlagIcon size={24} />
                            Select Prediction CSV & Generate Flags
                          </>
                        )}
                      </button>

                      {flagsResult && flagsResult.reviewStats && (
                        <div style={{
                          padding: '2rem',
                          background: 'linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(217, 119, 6, 0.05) 100%)',
                          borderRadius: 'var(--radius-xl)',
                          border: '2px solid var(--warning)',
                          boxShadow: 'var(--shadow-lg)'
                        }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
                            <div style={{
                              width: '48px',
                              height: '48px',
                              borderRadius: '50%',
                              background: 'var(--warning)',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              flexShrink: 0
                            }}>
                              <CheckIcon size={24} style={{ color: 'white' }} />
                            </div>
                            <div>
                              <h4 style={{ margin: 0, fontSize: '1.25rem', fontWeight: 700, color: 'var(--text-primary)' }}>
                                Review Flags Generated
                              </h4>
                              <p style={{ margin: '0.25rem 0 0 0', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                                Dataset: <strong>{flagsResult.videoName}</strong>
                              </p>
                            </div>
                          </div>

                          <div style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
                            gap: '1rem',
                            marginBottom: '1.5rem',
                            fontSize: '0.9rem'
                          }}>
                            <div>
                              <span className="text-muted" style={{ fontSize: '0.8125rem' }}>Effective FPS</span>
                              <div style={{ fontWeight: 600, marginTop: '0.25rem' }}>{flagsResult.reviewStats.effectiveFps} fps</div>
                            </div>
                            <div>
                              <span className="text-muted" style={{ fontSize: '0.8125rem' }}>Predicted Changes</span>
                              <div style={{ fontWeight: 600, marginTop: '0.25rem' }}>{flagsResult.reviewStats.predictedChangePoints}</div>
                            </div>
                            <div>
                              <span className="text-muted" style={{ fontSize: '0.8125rem' }}>Flagged Frames</span>
                              <div style={{ fontWeight: 600, marginTop: '0.25rem' }}>
                                {flagsResult.reviewStats.flaggedFrames} ({flagsResult.reviewStats.flaggedFramesPct}%)
                              </div>
                            </div>
                            <div>
                              <span className="text-muted" style={{ fontSize: '0.8125rem' }}>Merged Windows</span>
                              <div style={{ fontWeight: 600, marginTop: '0.25rem' }}>{flagsResult.reviewStats.windowsCount}</div>
                            </div>
                          </div>

                          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.75rem', marginBottom: '1rem' }}>
                            {flagsResult.flagCsvLink && (
                              <a className="btn btn-outline" href={flagsResult.flagCsvLink} target="_blank" rel="noopener noreferrer">
                                Open Flags CSV
                              </a>
                            )}
                            {flagsResult.flagSummaryLink && (
                              <a className="btn btn-outline" href={flagsResult.flagSummaryLink} target="_blank" rel="noopener noreferrer">
                                View Summary
                              </a>
                            )}
                            {flagsResult.watchFolderLink && (
                              <a className="btn btn-primary" href={flagsResult.watchFolderLink} target="_blank" rel="noopener noreferrer">
                                Open Watch Folder
                              </a>
                            )}
                          </div>

                          {(flagsResult.watchFramesCopied !== undefined || flagsResult.watchFramesRequested !== undefined) && (
                            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', margin: 0 }}>
                              Copied <strong>{flagsResult.watchFramesCopied ?? 0}</strong> of <strong>{flagsResult.watchFramesRequested ?? 0}</strong> flagged frames into <code>watch/</code> folder.
                            </p>
                          )}
                        </div>
                      )}

                      {!flagsResult && (
                        <div style={{
                          padding: '2rem',
                          background: 'var(--bg-secondary)',
                          borderRadius: 'var(--radius-lg)',
                          textAlign: 'center',
                          border: '1px dashed var(--border-medium)'
                        }}>
                          <FlagIcon size={48} style={{ color: 'var(--text-tertiary)', marginBottom: '1rem', opacity: 0.5 }} />
                          <p style={{ margin: 0, color: 'var(--text-secondary)', fontSize: '0.9375rem', lineHeight: 1.6 }}>
                            Generate review flags from a prediction CSV file (ending in <code>output.csv</code>). 
                            The system will identify frames around predicted behavior changes and copy them to the <code>watch/</code> folder for review.
                          </p>
                        </div>
                      )}
                    </div>
                  </div>
                </section>
              )}

              {/* Reference Images Section */}
              {currentSection === 'reference' && (
                <ReferenceImagesSection />
              )}

            {/* Activity Log - Always visible */}
            <section className="card" style={{ marginTop: '2rem' }}>
                <div className="card-header">
                  <div className="card-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
                    </svg>
                    Processing Activity Log
                  </div>
                </div>
                <div className="card-body" style={{ maxHeight: '400px', overflowY: 'auto', padding: '1rem' }}>
                  <FrameLog entries={logs} />
                </div>
              </section>
            </>
          )}
        </main>
      </div>
    </div>
  );
}

export default App;
