# Tailor Application - Complete System Design

> **Comprehensive system design document covering all aspects of the Tailor behavioral analysis platform, including implemented and planned features.**
>
> **Status update (Nov 2025):** Queue-based scheduling plus end-to-end job tracking/dashboarding are now live in production. Every request flows through a persistent FIFO queue, users can monitor live progress and history, and operators have full visibility into the processing pipeline.

## Table of Contents

1. [Overview](#overview)
2. [Functional Requirements](#functional-requirements)
3. [Non-Functional Requirements](#non-functional-requirements)
4. [Core Entities & Data Model](#core-entities--data-model)
5. [API Design](#api-design)
6. [High-Level Architecture](#high-level-architecture)
7. [Network Essentials](#network-essentials)
8. [Data Storage & Sharding](#data-storage--sharding)
9. [Caching Strategy](#caching-strategy)
10. [Scalability & Performance](#scalability--performance)
11. [CAP Theorem Considerations](#cap-theorem-considerations)
12. [Tracking & Observability](#tracking--observability)
13. [Security & Authentication](#security--authentication)
14. [Deployment Architecture](#deployment-architecture)
15. [Monitoring & Observability](#monitoring--observability)
16. [Future Enhancements](#future-enhancements)

---

## Overview

**Tailor** is a cloud-based video processing platform for behavioral analysis of laboratory animals (mice and rats). The system processes video recordings, extracts frames, performs AI-powered segmentation using SAM2, extracts behavioral features, runs predictive models, and generates review flags for manual inspection.

### Key Characteristics

- **Video Processing Pipeline**: Upload → Frame Extraction → Segmentation → Feature Extraction → Prediction → Review Flags
- **Cloud Storage**: Google Drive as primary storage backend
- **AI/ML Processing**: SAM2 segmentation, behavioral feature extraction, time-series prediction
- **Real-time Processing**: Long-running tasks with progress tracking
- **Multi-tenant**: User-specific Google Drive folders

---

## Functional Requirements

### FR1: User Authentication & Authorization
- **FR1.1**: Users must authenticate via Google OAuth 2.0
- **FR1.2**: System must request Google Drive read/write permissions
- **FR1.3**: Each user's data must be isolated in their own Drive folder structure

### FR2: Video Upload & Management
- **FR2.1**: Users can upload video files (MP4, AVI, MOV) to Google Drive
- **FR2.2**: Videos are stored in `tailor/videos/<video-name>/` folder structure
- **FR2.3**: System supports configurable frame extraction (FPS, stride)
- **FR2.4**: Extracted frames are stored as sequential JPEGs (000000.jpg, 000001.jpg, ...)

### FR3: Frame Extraction
- **FR3.1**: Extract frames from uploaded videos client-side or server-side
- **FR3.2**: Support configurable extraction rate (every Nth frame)
- **FR3.3**: Store frames in `tailor/results/<video-name>/frames/`
- **FR3.4**: Maintain frame-to-video timestamp mapping

### FR4: Coordinate Selection
- **FR4.1**: Interactive UI for selecting nest and subject (mouse/rat) coordinates
- **FR4.2**: Support multiple analysis templates (mouse_nest, rat1-5, etc.)
- **FR4.3**: Store selected coordinates for SAM2 processing

### FR5: SAM2 Segmentation
- **FR5.1**: Process video frames using SAM2 (Segment Anything Model 2)
- **FR5.2**: Generate segmentation masks for each frame
- **FR5.3**: Save masks as NPZ (NumPy archive) files
- **FR5.4**: Support GPU acceleration (CUDA) for faster processing
- **FR5.5**: Upload NPZ results back to Drive

### FR6: Feature Extraction
- **FR6.1**: Extract behavioral features from segmentation masks
- **FR6.2**: Support multiple extraction templates (mouse, rat, rat_only)
- **FR6.3**: Generate CSV files with time-series feature data
- **FR6.4**: Store feature CSVs in Drive results folder

### FR7: Prediction
- **FR7.1**: Run predictive models on extracted features
- **FR7.2**: Accept NPZ files as input for prediction
- **FR7.3**: Generate prediction CSV with behavioral classifications
- **FR7.4**: Support multiple analysis templates and model configurations

### FR8: Review Flags Generation
- **FR8.1**: Analyze prediction CSV to identify behavior change points
- **FR8.2**: Create time windows around predicted changes
- **FR8.3**: Flag frames within windows for manual review
- **FR8.4**: Copy flagged frames to `watch/` subfolder
- **FR8.5**: Generate flag summary statistics

### FR9: Results Management
- **FR9.1**: Display links to all generated files (NPZ, CSV, flags)
- **FR9.2**: Show processing statistics and progress
- **FR9.3**: Allow users to browse results via Google Drive

### FR10: Queueing & Job Tracking
- **FR10.1**: Every long-running request must be enqueued through the central FIFO scheduler.
- **FR10.2**: Jobs persist across restarts and resume automatically after VM reboot or crash.
- **FR10.3**: Users can submit multiple jobs; subsequent jobs wait in queue until earlier jobs finish.
- **FR10.4**: Expose job IDs, statuses (`pending`, `running`, `completed`, `failed`), and timestamps via API/UI.
- **FR10.5**: Operators can cancel, retry, or reprioritise jobs without SSH access.

---

## Non-Functional Requirements

### NFR1: Performance
- **NFR1.1**: Video upload should support files up to 5GB
- **NFR1.2**: Frame extraction should process at least 10 frames/second
- **NFR1.3**: SAM2 segmentation should process frames at GPU-accelerated speeds (target: 30+ FPS on T4)
- **NFR1.4**: API response time < 200ms for non-processing endpoints
- **NFR1.5**: Long-running tasks should provide progress updates

### NFR2: Scalability
- **NFR2.1**: Support concurrent processing of multiple videos per user
- **NFR2.2**: System should handle 100+ concurrent users
- **NFR2.3**: Horizontal scaling capability for backend processing
- **NFR2.4**: Storage should scale with user data growth

### NFR3: Reliability
- **NFR3.1**: System uptime target: 99.9% (8.76 hours downtime/year)
- **NFR3.2**: Process failures should be recoverable
- **NFR3.3**: Data should be durable (Google Drive provides 99.9% durability)
- **NFR3.4**: Long-running tasks should survive browser tab closure

### NFR4: Security
- **NFR4.1**: All API endpoints require OAuth authentication
- **NFR4.2**: User data isolation (no cross-user access)
- **NFR4.3**: HTTPS for all communications
- **NFR4.4**: Secure credential storage (no hardcoded secrets)

### NFR5: Usability
- **NFR5.1**: Intuitive UI with clear workflow progression
- **NFR5.2**: Real-time activity logs for user feedback
- **NFR5.3**: Error messages should be user-friendly
- **NFR5.4**: Support for multiple browser types

### NFR6: Cost Efficiency
- **NFR6.1**: Minimize Google Drive API quota usage
- **NFR6.2**: Optimize GPU usage (use preemptible instances if possible)
- **NFR6.3**: Efficient storage (compress NPZ files, optimize frame sizes)

---

## Core Entities & Data Model

### Entity Relationship Diagram

```
User (Google Account)
  ├── Drive Folder Structure
  │   ├── tailor/
  │   │   ├── videos/
  │   │   │   └── <video-name>/
  │   │   │       └── <video>.mp4
  │   │   └── results/
  │   │       └── <video-name>/
  │   │           ├── frames/
  │   │           │   ├── 000000.jpg
  │   │           │   ├── 000001.jpg
  │   │           │   └── ...
  │   │           ├── <video-name>.npz
  │   │           ├── <video-name>_features.csv
  │   │           ├── <video-name>_prediction.csv
  │   │           ├── <video-name>_flags_predonly.csv
  │   │           ├── <video-name>_flags_predonly_summary.csv
  │   │           └── watch/
  │   │               └── <flagged-frames>.jpg
  │   └── reference-images/
  │       └── <reference>.jpg
```

### Core Entities

#### 1. User
```typescript
interface User {
  id: string;                    // Google user ID
  email: string;                  // Google email
  accessToken: string;            // OAuth access token
  refreshToken?: string;          // OAuth refresh token
  driveRootFolderId: string;      // Root "tailor" folder ID
}
```

#### 2. Video
```typescript
interface Video {
  id: string;                     // Drive file ID
  name: string;                   // Video filename
  folderId: string;                // Parent folder ID
  mimeType: string;                // "video/mp4", etc.
  size: number;                    // File size in bytes
  uploadTime: Date;               // Upload timestamp
  fps: number;                    // Original video FPS
  duration: number;              // Duration in seconds
}
```

#### 3. Frame
```typescript
interface Frame {
  index: number;                  // Sequential index (0, 1, 2, ...)
  filename: string;               // "000000.jpg"
  fileId: string;                  // Drive file ID
  folderId: string;                // Parent folder ID
  timestamp: number;               // Video timestamp in seconds
  url?: string;                    // Direct access URL
}
```

#### 4. Segmentation Result
```typescript
interface SegmentationResult {
  videoName: string;
  npzFileId: string;               // Drive file ID of NPZ
  numFramesProcessed: number;
  coordinates: {
    nestPoint: { x: number; y: number };
    subjectPoint: { x: number; y: number };
    annotationFrameIndex: number;
  };
  template: string;                // "mouse_nest", "rat1", etc.
  processingTime: number;          // Seconds
}
```

#### 5. Feature Extraction Result
```typescript
interface FeatureResult {
  csvFileId: string;               // Drive file ID of features CSV
  numRows: number;
  features: string[];              // Column names
  extractionTemplate: string;
}
```

#### 6. Prediction Result
```typescript
interface PredictionResult {
  csvFileId: string;               // Drive file ID of prediction CSV
  numRows: number;
  predictedClasses: string[];      // Unique predicted behaviors
  modelConfig: string;              // Model configuration used
}
```

#### 7. Review Flags
```typescript
interface ReviewFlags {
  flagCsvFileId: string;            // Flags CSV with flag_window column
  summaryCsvFileId: string;         // Summary statistics
  watchFolderId: string;             // Folder with flagged frames
  stats: {
    totalRows: number;
    predictedChangePoints: number;
    flaggedFrames: number;
    flaggedFramesPct: number;
    windowsCount: number;
    rowsCoveredByWindows: number;
    effectiveFps: number;
  };
}
```

### Data Flow

```
User Upload → Google Drive
    ↓
Frame Extraction → Drive (frames/)
    ↓
Coordinate Selection → Frontend State
    ↓
SAM2 Processing → NPZ → Drive
    ↓
Feature Extraction → CSV → Drive
    ↓
Prediction → CSV → Drive
    ↓
Review Flags → CSV + Frames → Drive (watch/)
```

---

## API Design

### RESTful API Endpoints

#### Base URL
- **Production**: `https://your-domain.com/api` (set via frontend env)
- **Development**: `http://localhost:5000`

### Authentication
All endpoints require OAuth token in request body or Authorization header:
```http
Authorization: Bearer <access_token>
```

### Endpoints

#### 1. Health Check
```http
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-20T10:00:00Z"
}
```

#### 2. Process SAM2 Segmentation
```http
POST /process-sam2
Content-Type: application/json
```
**Request Body:**
```json
{
  "access_token": "ya29.a0AfH6...",
  "frame_folder_id": "1a2b3c4d5e6f7g8h",
  "video_folder_id": "9i0j1k2l3m4n5o6p",
  "nest_point": { "x": 320, "y": 240 },
  "mouse_point": { "x": 640, "y": 480 },
  "ann_frame_idx": 5,
  "fixed_points_template": "mouse_nest",
  "analysis_type": "mouse",
  "run_prediction": false
}
```
**Response:**
```json
{
  "success": true,
  "npz_drive_link": "https://drive.google.com/file/d/...",
  "num_frames_processed": 180,
  "processing_time_seconds": 45.2
}
```

#### 3. Run Prediction
```http
POST /run-prediction
Content-Type: application/json
```
**Request Body:**
```json
{
  "access_token": "ya29.a0AfH6...",
  "npz_file_id": "1a2b3c4d5e6f7g8h",
  "video_folder_id": "9i0j1k2l3m4n5o6p",
  "fixed_points_template": "mouse_nest",
  "analysis_type": "mouse"
}
```
**Response:**
```json
{
  "success": true,
  "prediction_csv_link": "https://drive.google.com/file/d/...",
  "features_csv_link": "https://drive.google.com/file/d/...",
  "num_rows": 8999
}
```

#### 4. Generate Review Flags
```http
POST /generate-review-flags
Content-Type: application/json
```
**Request Body:**
```json
{
  "access_token": "ya29.a0AfH6...",
  "prediction_csv_file_id": "1a2b3c4d5e6f7g8h",
  "video_folder_id": "9i0j1k2l3m4n5o6p",
  "fps_video": 30,
  "frame_stride": 10,
  "seconds_window": 3.0
}
```
**Response:**
```json
{
  "success": true,
  "flag_csv_link": "https://drive.google.com/file/d/...",
  "flag_summary_link": "https://drive.google.com/file/d/...",
  "watch_folder_link": "https://drive.google.com/drive/folders/...",
  "watch_frames_requested": 1682,
  "watch_frames_copied": 1682,
  "review_stats": {
    "total_rows": 8999,
    "predicted_change_points": 395,
    "flagged_frames": 1682,
    "flagged_frames_pct": 18.7,
    "windows_count": 115,
    "rows_covered_by_windows": 1684,
    "effective_fps": 3.0
  }
}
```

### API Design Principles

1. **RESTful**: Use HTTP methods appropriately (GET, POST)
2. **Stateless**: Each request contains all necessary information
3. **Idempotent**: Retry-safe operations where possible
4. **Versioning**: Future API versions via `/api/v2/` prefix
5. **Error Handling**: Consistent error response format
```json
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "details": {}
}
```

---

## High-Level Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Layer                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  React Frontend (Vite)                                 │  │
│  │  - Google OAuth                                        │  │
│  │  - Google Drive Picker                                 │  │
│  │  - Frame Extraction (Client-side)                      │  │
│  │  - Coordinate Selection UI                             │  │
│  │  - Activity Logs                                      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTPS
                            │
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway / Load Balancer                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Nginx (Reverse Proxy)                               │  │
│  │  - SSL Termination                                   │  │
│  │  - Static File Serving                               │  │
│  │  - API Routing (/api/* → Backend)                   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTP
                            │
┌─────────────────────────────────────────────────────────────┐
│                      Application Layer                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Flask API Server                                    │  │
│  │  - OAuth Token Validation                           │  │
│  │  - Request Routing                                  │  │
│  │  - Error Handling                                   │  │
│  │  - CORS Management                                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │
┌─────────────────────────────────────────────────────────────┐
│                      Processing Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  SAM2 Service│  │  Feature    │  │  Prediction │      │
│  │              │  │  Extraction  │  │  Service    │      │
│  │  - GPU       │  │  - Mouse     │  │  - Models   │      │
│  │  - CUDA      │  │  - Rat       │  │  - CSV Gen  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  ┌──────────────┐                                           │
│  │  Review Flags│                                           │
│  │  Generator   │                                           │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            │
┌─────────────────────────────────────────────────────────────┐
│                      Storage Layer                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Google Drive API                                     │  │
│  │  - File Upload/Download                              │  │
│  │  - Folder Management                                 │  │
│  │  - Metadata Operations                               │  │
│  │  - User-specific Folders                             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GCP Compute Engine                         │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  VM Instance: tailor-processor-gpu                    │  │
│  │  - Machine Type: n1-highmem-8 (or GPU-enabled)       │  │
│  │  - GPU: NVIDIA T4 / L4 (planned)                    │  │
│  │  - OS: Ubuntu 22.04                                   │  │
│  │                                                       │  │
│  │  ┌──────────────────────────────────────────────┐    │  │
│  │  │  Systemd Services:                           │    │  │
│  │  │  - tailor-api.service (Flask)                 │    │  │
│  │  │  - nginx.service                              │    │  │
│  │  └──────────────────────────────────────────────┘    │  │
│  │                                                       │  │
│  │  ┌──────────────────────────────────────────────┐    │  │
│  │  │  Application Stack:                          │    │  │
│  │  │  - Python 3.10 + venv                        │    │  │
│  │  │  - SAM2 (PyTorch)                             │    │  │
│  │  │  - Flask + Gunicorn (future)                  │    │  │
│  │  └──────────────────────────────────────────────┘    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Static IP: <your-vm-external-ip>                    │  │
│  │  DNS: your-domain.com → <your-vm-external-ip>        │  │
│  │  SSL: Let's Encrypt (Certbot)                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Network Essentials

### Network Topology

```
Internet
    │
    │ HTTPS (443)
    │
┌───▼──────────────────────────────────────┐
│  Cloud Load Balancer (Future)            │
│  - SSL Termination                       │
│  - Health Checks                         │
│  - Auto-scaling                          │
└───┬──────────────────────────────────────┘
    │
    │ HTTP (80) / HTTPS (443)
    │
┌───▼──────────────────────────────────────┐
│  GCP VM (tailor-processor-gpu)           │
│                                           │
│  ┌────────────────────────────────────┐  │
│  │  Nginx (Port 80/443)                │  │
│  │  - Reverse Proxy                    │  │
│  │  - Static Files                    │  │
│  └──────────┬─────────────────────────┘  │
│             │                             │
│             │ HTTP (5000)                  │
│             │                              │
│  ┌──────────▼─────────────────────────┐  │
│  │  Flask API (Port 5000)             │  │
│  │  - Gunicorn Workers (Future)       │  │
│  └────────────────────────────────────┘  │
└───────────────────────────────────────────┘
    │
    │ HTTPS (443)
    │
┌───▼──────────────────────────────────────┐
│  Google Drive API                         │
│  - REST API                               │
│  - OAuth 2.0                              │
└───────────────────────────────────────────┘
```

### Network Protocols

1. **HTTPS (TLS 1.2+)**: All client-server communication
2. **HTTP/2**: For improved performance (future)
3. **WebSocket**: For real-time progress updates (future)
4. **OAuth 2.0**: Authentication flows

### Firewall Rules

```bash
# Ingress Rules
- Port 80 (HTTP) → Nginx
- Port 443 (HTTPS) → Nginx
- Port 22 (SSH) → VM (restricted IPs)

# Egress Rules
- Port 443 (HTTPS) → Google Drive API
- Port 443 (HTTPS) → Google OAuth
- Port 80/443 (HTTP/HTTPS) → Package repositories
```

### CDN & Edge Caching (Future)

- **Cloud CDN**: Cache static assets (JS, CSS, images)
- **Edge Locations**: Reduce latency for global users
- **Cache Headers**: Proper cache-control headers for static files

---

## Data Storage & Sharding

### Google Drive as Storage Backend

**Question: Does using Google Drive count as sharding?**

**Answer: Partially, but not in the traditional sense.**

#### How Google Drive Works

1. **User-Level Partitioning**: Each user has their own Drive space (natural sharding by user)
2. **Google's Internal Sharding**: Google shards data across their infrastructure (transparent to us)
3. **Our Application**: We don't implement sharding logic; we rely on Google's infrastructure

#### Sharding Characteristics

**✅ What Google Drive Provides:**
- **Horizontal Partitioning**: Data distributed across Google's servers
- **Automatic Scaling**: Google handles capacity increases
- **Geographic Distribution**: Data replicated across regions
- **User Isolation**: Each user's data is logically separated

**❌ What We Don't Have:**
- **Explicit Shard Keys**: We don't choose how to partition data
- **Cross-Shard Queries**: We can't query across all users' data
- **Shard Management**: We don't manage shard distribution
- **Custom Sharding Strategy**: We rely on Google's default behavior

#### Our Data Distribution Strategy

```
User A → Google Drive Account A → tailor/ folder
User B → Google Drive Account B → tailor/ folder
User C → Google Drive Account C → tailor/ folder
```

**This is effectively sharding by user ID**, but managed by Google.

### Alternative Sharding Strategies (If We Migrated to Custom Storage)

#### 1. User-Based Sharding
```python
shard_id = hash(user_id) % num_shards
```
- **Pros**: Natural isolation, easy to implement
- **Cons**: Uneven distribution if some users have much more data

#### 2. Video-Based Sharding
```python
shard_id = hash(video_id) % num_shards
```
- **Pros**: Even distribution across videos
- **Cons**: User's videos may be on different shards

#### 3. Time-Based Sharding
```python
shard_id = month % num_shards  # Shard by upload month
```
- **Pros**: Easy to archive old data
- **Cons**: Hot shards for recent data

#### 4. Consistent Hashing
```python
# Use consistent hashing ring for shard assignment
shard_id = consistent_hash(video_id, shard_ring)
```
- **Pros**: Even distribution, easy to add/remove shards
- **Cons**: More complex implementation

### Current Storage Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Google Drive (User's Account)                          │
│                                                           │
│  ┌───────────────────────────────────────────────────┐ │
│  │  tailor/ (Root Folder)                            │ │
│  │  ├── videos/                                      │ │
│  │  │   └── <video-name>/                            │ │
│  │  │       └── video.mp4                            │ │
│  │  └── results/                                      │ │
│  │      └── <video-name>/                            │ │
│  │          ├── frames/                              │ │
│  │          │   ├── 000000.jpg                      │ │
│  │          │   └── ...                              │ │
│  │          ├── <name>.npz                           │ │
│  │          ├── <name>_features.csv                  │ │
│  │          ├── <name>_prediction.csv                │ │
│  │          ├── <name>_flags_predonly.csv            │ │
│  │          └── watch/                               │ │
│  │              └── <flagged-frames>.jpg            │ │
│  └───────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Storage Optimization

1. **Frame Compression**: JPEG quality optimization
2. **NPZ Compression**: NumPy's built-in compression
3. **CSV Compression**: Gzip compression for large CSVs (future)
4. **Cleanup Policies**: Archive old results (future)

---

## Caching Strategy

### Current Caching (Minimal)

**Frontend:**
- Browser cache for static assets (JS, CSS, images)
- React state management (in-memory)

**Backend:**
- No caching currently implemented

### Recommended Caching Layers

#### 1. Client-Side Caching

**Browser Cache:**
```http
Cache-Control: public, max-age=31536000  # Static assets
Cache-Control: no-cache                   # API responses
```

**Service Worker (Future):**
- Cache static assets offline
- Cache frame thumbnails

#### 2. CDN Caching

**Cloud CDN (Future):**
- Cache static frontend assets
- Cache frequently accessed Drive file metadata
- Edge locations for global users

#### 3. Application-Level Caching

**Redis Cache (Future):**
```python
# Cache Drive folder structure
cache_key = f"drive_folders:{user_id}"
cache.set(cache_key, folder_structure, ttl=3600)

# Cache video metadata
cache_key = f"video_meta:{video_id}"
cache.set(cache_key, metadata, ttl=1800)

# Cache processing status
cache_key = f"job_status:{job_id}"
cache.set(cache_key, status, ttl=300)
```

**Cache Invalidation:**
- Invalidate on file upload
- Invalidate on folder creation
- TTL-based expiration

#### 4. Database Query Caching (If We Add Database)

**PostgreSQL Query Cache:**
- Cache frequently accessed queries
- Cache user preferences
- Cache analysis templates

### Cache-Aside Pattern

```
1. Check cache
2. If miss, fetch from Drive API
3. Store in cache
4. Return data
```

### Write-Through Pattern (Future)

```
1. Write to Drive API
2. Update cache immediately
3. Return success
```

---

## Scalability & Performance

### Current Limitations

1. **Single VM**: All processing on one instance
2. **No Load Balancing**: Single point of failure
3. **Synchronous Frontend Calls**: Browser still initiates work via API, though backend is async
4. **Single Worker Pool**: Queue guarantees ordering but currently backed by one GPU worker

### Scalability Strategies

#### 1. Horizontal Scaling

**Backend Workers:**
```
┌─────────────┐
│  Load       │
│  Balancer   │
└──────┬──────┘
       │
   ┌───┴───┬─────────┬─────────┐
   │       │         │         │
┌──▼──┐ ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
│ VM1 │ │ VM2 │  │ VM3 │  │ VM4 │
└─────┘ └─────┘  └─────┘  └─────┘
```

**Implementation:**
- Multiple VM instances behind load balancer
- Stateless API servers (can scale horizontally)
- Shared session storage (Redis) if needed

#### 2. Vertical Scaling

**Current:**
- n1-highmem-8 (8 vCPU, 52GB RAM)

**Options:**
- Upgrade to n1-highmem-16 (16 vCPU, 104GB RAM)
- Add GPU (T4, L4, A100)
- Increase disk size

#### 3. Async Processing

**Current (Implemented Nov 2025):** Fully asynchronous via Redis-backed FIFO queue + GPU worker.

```
User Request
    ↓
API Gateway (returns job_id immediately)
    ↓
Redis Queue (persistent FIFO)
    ↓
GPU Worker(s) pulling jobs
    ↓
Status Service (PostgreSQL + Redis cache)
    ↓
Users poll / subscribe to updates
```

**Implementation Highlights:**
```python
# Enqueue
job_id = scheduler.enqueue("sam2", payload)
return {"job_id": job_id, "status": "queued"}

# Worker heartbeat
while True:
    job = scheduler.next_job("sam2")
    process(job.args)
    scheduler.mark_done(job.id, result_metadata)

# Status endpoint
GET /jobs/{job_id}
→ {"status": "processing", "queue_position": 2, "etaSeconds": 540}
```

- Jobs survive VM restarts because both queue and metadata live in Redis + PostgreSQL.
- Queue fairness: per-user rate limits ensure one user cannot starve others.
- Operators can cancel/retry through `/jobs/{id}` admin endpoints or the console dashboard.

#### 4. Database Scaling (If We Add Database)

**Read Replicas:**
- Primary for writes
- Replicas for reads
- Geographic distribution

**Partitioning:**
- Partition by user_id
- Partition by date

#### 5. Storage Scaling

**Google Drive:**
- Already scales automatically
- Per-user quotas (15GB free, paid plans available)

**Alternative (Future):**
- Google Cloud Storage buckets
- Sharded by user_id
- CDN for frequently accessed files

### Performance Optimization

#### 1. Frame Extraction
- **Client-side**: Offloads server, but limited by browser
- **Server-side**: More control, but uses server resources
- **Hybrid**: Small videos client-side, large videos server-side

#### 2. SAM2 Processing
- **GPU Acceleration**: 10-30x faster than CPU
- **Batch Processing**: Process multiple frames in parallel
- **Model Optimization**: Quantization, pruning (future)

#### 3. API Response Times
- **Connection Pooling**: Reuse HTTP connections
- **Parallel Requests**: Process multiple Drive operations concurrently
- **Response Compression**: Gzip for large responses

#### 4. Frontend Optimization
- **Code Splitting**: Lazy load components
- **Image Optimization**: WebP format, responsive images
- **Bundle Size**: Tree shaking, minification

---

## CAP Theorem Considerations

### CAP Theorem Overview

**Consistency (C)**: All nodes see the same data simultaneously  
**Availability (A)**: System remains operational  
**Partition Tolerance (P)**: System continues despite network failures

**You can only guarantee 2 of 3.**

### Our System's CAP Profile

#### Current Architecture: **AP System** (Availability + Partition Tolerance)

**Why AP?**
1. **Google Drive**: Eventually consistent (AP)
2. **No Database**: No strong consistency requirements
3. **Stateless API**: Each request is independent

**Trade-offs:**
- ✅ **Availability**: System remains available even if some components fail
- ✅ **Partition Tolerance**: Works across network partitions
- ❌ **Consistency**: Users might see slightly stale data (rare)

#### Consistency Scenarios

**Scenario 1: File Upload**
```
User uploads video → Drive API → Eventually visible
```
- **Weak Consistency**: File appears after upload completes
- **Acceptable**: User expects slight delay

**Scenario 2: Concurrent Processing**
```
User A processes video → Creates results folder
User B (same account) → Might not see folder immediately
```
- **Eventual Consistency**: Folder appears within seconds
- **Mitigation**: Poll for folder existence, retry logic

**Scenario 3: Multiple Workers (Future)**
```
Worker 1: Processing video A
Worker 2: Processing video B (same user)
→ Both write to same Drive folder
```
- **Race Conditions**: Possible file conflicts
- **Mitigation**: Use atomic operations, file locking

### If We Add a Database

#### Option 1: PostgreSQL (CP System)
- **Consistency**: Strong consistency (ACID)
- **Partition Tolerance**: Handles network partitions
- **Trade-off**: Reduced availability during partitions

#### Option 2: MongoDB (AP System)
- **Availability**: High availability
- **Partition Tolerance**: Handles partitions
- **Trade-off**: Eventual consistency

#### Option 3: Redis (CP System)
- **Consistency**: Strong consistency
- **Partition Tolerance**: Limited (single node)
- **Use Case**: Caching, session storage

### Recommended Approach

**Current:** Stay with AP (Google Drive)  
**Future:** Add CP database (PostgreSQL) for critical metadata, keep Drive for file storage

```
┌─────────────────────────────────────────┐
│  PostgreSQL (CP)                        │
│  - User metadata                         │
│  - Job status                            │
│  - Processing history                    │
└─────────────────────────────────────────┘
              │
              │
┌─────────────▼─────────────────────────────┐
│  Google Drive (AP)                       │
│  - File storage                          │
│  - Results                                │
└──────────────────────────────────────────┘
```

---

## Tracking & Observability

### Change Tracking & Release Log
- **Deployment Journal**: Every run of `setup_production.sh`, backend deploy, or certificate renewal emits a structured event (timestamp, git SHA, operator, summary) that is stored in PostgreSQL and mirrored to BigQuery for analytics.
- **Config Snapshots**: Nginx, systemd units, and `.env.production` are versioned nightly. Operators can diff any two snapshots or roll back with a single command.
- **User-Facing Changelog**: The frontend surfaces the five most recent platform updates so researchers know when new features or fixes land.

### Queue Insights & Job Timeline
- **Live Queue Dashboard**: Displays queued/running/completed counts, per-user quotas, and estimated start times derived from historical throughput.
- **Job Drill-down**: Each job exposes lifecycle timestamps (queued → dequeued → GPU start → GPU finish → Drive upload), GPU UUID used, and links to logs/artifacts.
- **Auto-Pause Rules**: If queue depth exceeds 50 or GPU temperature crosses 80 °C, new jobs remain in `pending` while alerts fire to Ops.

### Audit Trail & Notifications
- **Immutable Audit Stream**: Critical actions (job cancellation, quota change, DNS switch, OAuth secret update) append to an append-only log stored in Cloud Logging + exported to BigQuery for compliance.
- **Notifications**: Users receive email + in-app toasts when jobs start, finish, or fail; operators get Slack pings when queue SLA is breached.
- **API Access**: `/jobs/{id}/history` returns the full timeline so programmatic clients can embed progress in their own dashboards.

---

## Security & Authentication

### Authentication Flow

```
1. User visits frontend
2. Frontend loads Google Identity Services
3. User clicks "Sign in with Google"
4. OAuth 2.0 flow:
   a. Redirect to Google
   b. User authorizes
   c. Google returns authorization code
   d. Frontend exchanges code for access token
5. Frontend stores token (in-memory, not localStorage)
6. API requests include token in Authorization header
```

### Authorization

**OAuth Scopes:**
```javascript
[
  'https://www.googleapis.com/auth/drive.file',  // Create files
  'https://www.googleapis.com/auth/drive.readonly', // Read files
  'openid',
  'email',
  'profile'
]
```

**Token Validation:**
```python
# Backend validates token on each request
credentials = Credentials(token=access_token)
drive_service = build('drive', 'v3', credentials=credentials)
# If invalid, request fails
```

### Security Measures

#### 1. HTTPS Only
- All communications encrypted
- SSL certificate (Let's Encrypt)
- HSTS headers

#### 2. Token Security
- Tokens not stored in localStorage (XSS protection)
- Tokens expire (refresh token used)
- Backend validates tokens with Google

#### 3. CORS Policy
```python
CORS(app, origins=[
    'https://your-domain.com',
    'http://localhost:5173'  # Development only
])
```

#### 4. Input Validation
- Validate all API inputs
- Sanitize file names
- Check file sizes
- Validate coordinates

#### 5. Rate Limiting (Future)
```python
from flask_limiter import Limiter

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)
```

#### 6. Secrets Management
- Environment variables for secrets
- No hardcoded credentials
- Use GCP Secret Manager (future)

### Data Privacy

1. **User Isolation**: Each user's data in their own Drive
2. **No Cross-User Access**: Backend validates user ownership
3. **Data Retention**: Users control their own data
4. **GDPR Compliance**: Users can delete their data

---

## Deployment Architecture

### Current Deployment

```
┌─────────────────────────────────────────────────┐
│  GCP Compute Engine VM                          │
│  - tailor-processor-gpu                         │
│  - Zone: us-west4-b                            │
│  - Machine: n1-highmem-8                       │
│  - IP: <your-vm-external-ip> (Static)         │
└─────────────────────────────────────────────────┘
         │
         │ DNS: your-domain.com
         │
┌────────▼────────────────────────────────────────┐
│  Nginx (Port 80/443)                            │
│  - SSL Termination                              │
│  - Static File Serving                          │
│  - API Reverse Proxy                            │
└────────┬────────────────────────────────────────┘
         │
         │ HTTP (5000)
         │
┌────────▼────────────────────────────────────────┐
│  Flask API (Port 5000)                          │
│  - Systemd Service                              │
│  - Auto-restart on failure                      │
└─────────────────────────────────────────────────┘
```

### Deployment Process

#### Frontend Deployment
```bash
# Build
cd frontend
npm run build

# Deploy to VM
scp -r dist/* user@vm:/var/www/tailor/
```

#### Backend Deployment
```bash
# Copy files
./backend/deploy_to_vm.sh

# SSH and restart
ssh user@vm
sudo systemctl restart tailor-api.service
```

### Future Deployment Improvements

#### 1. CI/CD Pipeline
```
Git Push → GitHub Actions
    ↓
Build & Test
    ↓
Deploy to Staging
    ↓
Deploy to Production
```

#### 2. Containerization
```dockerfile
# Dockerfile
FROM python:3.10
COPY backend/ /app/
RUN pip install -r requirements.txt
CMD ["gunicorn", "api_server:app"]
```

#### 3. Kubernetes (Future)
```
┌─────────────────────────────────────┐
│  Kubernetes Cluster                 │
│  ┌─────────┐  ┌─────────┐          │
│  │  Pod 1  │  │  Pod 2  │  ...     │
│  └─────────┘  └─────────┘          │
│       │            │                │
│  ┌────▼────────────▼────┐          │
│  │  Service (Load Bal)  │          │
│  └──────────────────────┘          │
└─────────────────────────────────────┘
```

#### 4. Auto-Scaling
- **Horizontal Pod Autoscaler**: Scale based on CPU/memory
- **Vertical Pod Autoscaler**: Adjust resource requests
- **Cluster Autoscaler**: Add/remove nodes

---

## Monitoring & Observability

### Current Monitoring (Minimal)

**System Logs:**
```bash
# Backend logs
sudo journalctl -u tailor-api.service -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Recommended Monitoring Stack

#### 1. Application Metrics

**Prometheus (Future):**
```python
from prometheus_client import Counter, Histogram

request_count = Counter('api_requests_total', 'Total API requests')
request_duration = Histogram('api_request_duration_seconds', 'Request duration')
```

**Metrics to Track:**
- API request rate
- Response times (p50, p95, p99)
- Error rates
- Processing job duration
- GPU utilization
- Memory usage

#### 2. Logging

**Structured Logging:**
```python
import logging
import json

logger.info("Processing started", extra={
    "user_id": user_id,
    "video_id": video_id,
    "job_id": job_id
})
```

**Log Aggregation (Future):**
- **ELK Stack**: Elasticsearch, Logstash, Kibana
- **Cloud Logging**: GCP Cloud Logging
- **Splunk**: Enterprise log management

#### 3. Distributed Tracing

**OpenTelemetry (Future):**
```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("process_sam2"):
    # Processing logic
```

**Trace Flow:**
```
Frontend Request → API → SAM2 Service → Drive API
     ↓              ↓         ↓            ↓
   Span 1        Span 2    Span 3      Span 4
```

#### 4. Alerting

**Alert Rules:**
- API error rate > 5%
- Response time p95 > 5s
- GPU memory > 90%
- Disk space < 20%
- Service down

**Alert Channels:**
- Email
- Slack
- PagerDuty (for critical alerts)

#### 5. Health Checks

**Endpoint:**
```http
GET /health
```

**Checks:**
- Database connectivity (if added)
- Drive API connectivity
- GPU availability
- Disk space
- Memory usage

---

## Future Enhancements

### Short-Term (3-6 months)

1. **Job Queue System**
   - Redis/RabbitMQ for async processing
   - Job status tracking
   - Retry logic

2. **Database Integration**
   - PostgreSQL for metadata
   - User preferences
   - Processing history

3. **Improved Error Handling**
   - Retry mechanisms
   - Better error messages
   - Failure recovery

4. **Performance Optimization**
   - Caching layer (Redis)
   - CDN for static assets
   - Database query optimization

### Medium-Term (6-12 months)

1. **Multi-User Support**
   - User management
   - Team workspaces
   - Sharing capabilities

2. **Advanced Analytics**
   - Dashboard for statistics
   - Trend analysis
   - Export capabilities

3. **Mobile App**
   - iOS/Android apps
   - Push notifications
   - Offline support

4. **API Versioning**
   - v1, v2 APIs
   - Backward compatibility
   - Deprecation strategy

### Long-Term (12+ months)

1. **Machine Learning Improvements**
   - Custom model training
   - A/B testing framework
   - Model versioning

2. **Real-time Collaboration**
   - WebSocket support
   - Live progress updates
   - Collaborative annotation

3. **Enterprise Features**
   - SSO integration
   - Audit logs
   - Compliance features

4. **Global Scale**
   - Multi-region deployment
   - Edge computing
   - Regional data storage

---

## Conclusion

This system design document provides a comprehensive overview of the Tailor application, covering:

- ✅ Functional and non-functional requirements
- ✅ Core entities and data modeling
- ✅ API design principles
- ✅ High-level architecture
- ✅ Network essentials
- ✅ Data storage and sharding (including Google Drive analysis)
- ✅ Caching strategies
- ✅ Scalability considerations
- ✅ CAP theorem analysis
- ✅ Security and authentication
- ✅ Deployment architecture
- ✅ Monitoring and observability
- ✅ Future enhancements

The system is designed to be scalable, secure, and maintainable, with clear paths for future growth and enhancement.

---

## References

- [Hello Interview - System Design Guide](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction)
- [Google Drive API Documentation](https://developers.google.com/drive/api)
- [OAuth 2.0 Specification](https://oauth.net/2/)
- [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)
- [SAM2 Documentation](https://github.com/facebookresearch/segment-anything-2)

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Author:** Tailor Development Team

