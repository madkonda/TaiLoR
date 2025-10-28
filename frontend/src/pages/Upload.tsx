export default function Upload() {
  return (
    <section className="upload-page">
      <h1>Upload Mouse Behavior Videos</h1>
      <p className="lead">Upload your mouse behavior videos for SAM2 segmentation and behavior analysis</p>

      <div className="dropzone" role="button" tabIndex={0}>
        <div className="drop-icon">⬆️</div>
        <div className="drop-title">Drag & drop videos here</div>
        <div className="drop-sub">or click to select files</div>
        <div className="drop-note">Supports MP4, AVI, MOV, MKV, WebM (max 5 files)</div>
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
        <div className="feature-card">
          <div className="feature-icon">📦</div>
          <h3>Batch Processing</h3>
          <p>Upload multiple videos and process them together with queue-based scheduling for efficiency</p>
        </div>
      </div>
    </section>
  )
}


