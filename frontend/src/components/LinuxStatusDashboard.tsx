import React, { useState, useEffect } from 'react';

interface LinuxFile {
  name: string;
  type: 'video' | 'image' | 'other' | 'directory';
  size?: string;
  lastModified?: string;
  status?: 'processing' | 'completed';
  fullPath?: string;
}

interface LinuxStatus {
  videosDirectory: string;
  resultsDirectory: string;
  videos: LinuxFile[];
  results: LinuxFile[];
  processing: string[];
  completed: string[];
  lastUpdate: string;
}

interface CoordinateInput {
  nestX: number;
  nestY: number;
  mouseX: number;
  mouseY: number;
}

const LinuxStatusDashboard: React.FC = () => {
  const [status, setStatus] = useState<LinuxStatus | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const [selectedFolder, setSelectedFolder] = useState<string | null>(null);
  const [showCoordinateModal, setShowCoordinateModal] = useState(false);
  const [coordinates, setCoordinates] = useState<CoordinateInput>({
    nestX: 677,
    nestY: 881,
    mouseX: 766,
    mouseY: 773
  });
  const [isProcessing, setIsProcessing] = useState(false);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/linux-status');
        const data = await response.json();
        
        if (data.success) {
          setStatus(data.status);
          setIsConnected(true);
        }
      } catch (error) {
        console.error('Error fetching Linux status:', error);
        setIsConnected(false);
      }
    };

    // Fetch status immediately
    fetchStatus();
    
    // Set up polling every 3 seconds
    const interval = setInterval(fetchStatus, 3000);
    
    return () => clearInterval(interval);
  }, []);

  const formatTime = (timestamp: string) => {
    return new Date(timestamp).toLocaleTimeString();
  };

  const handleFolderSelect = (folderPath: string) => {
    setSelectedFolder(folderPath);
    setShowCoordinateModal(true);
  };

  const handleCoordinateSubmit = async () => {
    if (!selectedFolder) return;
    
    setIsProcessing(true);
    try {
      const response = await fetch('http://localhost:3001/api/process-folder', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          folderPath: selectedFolder,
          coordinates: coordinates
        })
      });

      const result = await response.json();
      
      if (result.success) {
        alert(`✅ Started processing folder: ${selectedFolder}\nNest: (${coordinates.nestX}, ${coordinates.nestY})\nMouse: (${coordinates.mouseX}, ${coordinates.mouseY})`);
        setShowCoordinateModal(false);
        setSelectedFolder(null);
      } else {
        alert(`❌ Error: ${result.error}`);
      }
    } catch (error) {
      console.error('Error processing folder:', error);
      alert(`❌ Error processing folder: ${error instanceof Error ? error.message : 'Unknown error'}`);
    } finally {
      setIsProcessing(false);
    }
  };

  const getFullPath = (file: LinuxFile, baseDir: string) => {
    return file.fullPath || `${baseDir}/${file.name}`;
  };

  const getFileIcon = (filename: string) => {
    const ext = filename.split('.').pop()?.toLowerCase();
    switch (ext) {
      case 'mp4':
      case 'avi':
      case 'mov':
        return '🎬';
      case 'npz':
        return '🧠';
      case 'jpg':
      case 'jpeg':
        return '🖼️';
      default:
        return '📄';
    }
  };

  if (!status) {
    return (
      <div className="linux-status-dashboard p-6 bg-gray-800 rounded-lg shadow-lg text-white">
        <h2 className="text-3xl font-bold mb-6 text-center">🐧 Linux Mint Status</h2>
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p className="text-gray-400">Loading Linux Mint status...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="linux-status-dashboard p-6 bg-gray-800 rounded-lg shadow-lg text-white">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-3xl font-bold">🐧 Linux Mint Status</h2>
        <div className="flex items-center gap-2">
          <span className={`inline-block w-3 h-3 rounded-full ${isConnected ? 'bg-green-500' : 'bg-red-500'}`}></span>
          <span className="text-sm text-gray-400">Last update: {formatTime(status.lastUpdate)}</span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {/* Stats Cards */}
        <div className="bg-gray-700 p-4 rounded-lg">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Videos</p>
              <p className="text-2xl font-bold text-blue-400">{status.videos.length}</p>
            </div>
            <div className="text-3xl">🎬</div>
          </div>
        </div>

        <div className="bg-gray-700 p-4 rounded-lg">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Processing</p>
              <p className="text-2xl font-bold text-yellow-400">{status.processing.length}</p>
            </div>
            <div className="text-3xl">⚙️</div>
          </div>
        </div>

        <div className="bg-gray-700 p-4 rounded-lg">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Completed</p>
              <p className="text-2xl font-bold text-green-400">{status.completed.length}</p>
            </div>
            <div className="text-3xl">✅</div>
          </div>
        </div>

        <div className="bg-gray-700 p-4 rounded-lg">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Results</p>
              <p className="text-2xl font-bold text-purple-400">{status.results.length}</p>
            </div>
            <div className="text-3xl">📊</div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Videos Directory */}
        <div className="bg-gray-700 p-4 rounded-lg">
          <h3 className="text-lg font-semibold mb-3 flex items-center">
            📁 Videos Directory
            <span className="ml-2 text-sm text-gray-400">({status.videosDirectory})</span>
          </h3>
          <div className="max-h-48 overflow-y-auto">
            {status.videos.length === 0 ? (
              <p className="text-gray-400 text-sm">No videos found</p>
            ) : (
              <div className="space-y-2">
                {status.videos.map((video, index) => (
                  <div key={index} className="flex items-center justify-between p-2 bg-gray-600 rounded group">
                    <div className="flex items-center gap-2 flex-1 min-w-0">
                      <span className="text-lg">{getFileIcon(video.name)}</span>
                      <div className="flex-1 min-w-0">
                        <div className="text-sm font-mono truncate" title={getFullPath(video, status.videosDirectory)}>
                          {video.name}
                        </div>
                        <div className="text-xs text-gray-400 truncate" title={getFullPath(video, status.videosDirectory)}>
                          📁 {getFullPath(video, status.videosDirectory)}
                        </div>
                        {video.size && typeof video.size === 'number' && (
                          <div className="text-xs text-gray-500">
                            📏 {(video.size / (1024 * 1024)).toFixed(2)} MB
                          </div>
                        )}
                      </div>
                    </div>
                    <button
                      onClick={() => handleFolderSelect(getFullPath(video, status.videosDirectory))}
                      className="opacity-0 group-hover:opacity-100 bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded text-xs transition-opacity"
                      title="Process this video with SAM2"
                    >
                      🎬 Process
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Results Directory */}
        <div className="bg-gray-700 p-4 rounded-lg">
          <h3 className="text-lg font-semibold mb-3 flex items-center">
            📊 Results Directory
            <span className="ml-2 text-sm text-gray-400">({status.resultsDirectory})</span>
          </h3>
          <div className="max-h-48 overflow-y-auto">
            {status.results.length === 0 ? (
              <p className="text-gray-400 text-sm">No results found</p>
            ) : (
              <div className="space-y-2">
                {status.results.map((result, index) => (
                  <div key={index} className="flex items-center justify-between p-2 bg-gray-600 rounded group">
                    <div className="flex items-center gap-2 flex-1 min-w-0">
                      <span className="text-lg">{getFileIcon(result.name)}</span>
                      <div className="flex-1 min-w-0">
                        <div className="text-sm font-mono truncate" title={getFullPath(result, status.resultsDirectory)}>
                          {result.name}
                        </div>
                        <div className="text-xs text-gray-400 truncate" title={getFullPath(result, status.resultsDirectory)}>
                          📁 {getFullPath(result, status.resultsDirectory)}
                        </div>
                      </div>
                    </div>
                    <button
                      onClick={() => handleFolderSelect(getFullPath(result, status.resultsDirectory))}
                      className="opacity-0 group-hover:opacity-100 bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded text-xs transition-opacity"
                      title="Process this folder with SAM2"
                    >
                      🎯 Process
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Processing Status */}
      {status.processing.length > 0 && (
        <div className="mt-6 bg-yellow-900/20 border border-yellow-500/30 p-4 rounded-lg">
          <h3 className="text-lg font-semibold mb-3 text-yellow-400">⚙️ Currently Processing</h3>
          <div className="space-y-2">
            {status.processing.map((file, index) => (
              <div key={index} className="flex items-center gap-2">
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-yellow-400"></div>
                <span className="text-sm font-mono">{file}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Completed Jobs */}
      {status.completed.length > 0 && (
        <div className="mt-6 bg-green-900/20 border border-green-500/30 p-4 rounded-lg">
          <h3 className="text-lg font-semibold mb-3 text-green-400">✅ Recently Completed</h3>
          <div className="space-y-2">
            {status.completed.slice(0, 5).map((file, index) => (
              <div key={index} className="flex items-center gap-2">
                <span className="text-green-400">✅</span>
                <span className="text-sm font-mono">{file}</span>
              </div>
            ))}
            {status.completed.length > 5 && (
              <p className="text-sm text-gray-400">... and {status.completed.length - 5} more</p>
            )}
          </div>
        </div>
      )}

      {/* Coordinate Input Modal */}
      {showCoordinateModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-gray-800 p-6 rounded-lg shadow-xl max-w-md w-full mx-4">
            <h3 className="text-xl font-bold mb-4 text-white">
              🎯 SAM2 Processing Coordinates
            </h3>
            <p className="text-gray-400 mb-4">
              Processing folder: <span className="font-mono text-blue-400">{selectedFolder}</span>
            </p>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  🏠 Nest Coordinates
                </label>
                <div className="grid grid-cols-2 gap-2">
                  <input
                    type="number"
                    value={coordinates.nestX}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, nestX: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="X"
                  />
                  <input
                    type="number"
                    value={coordinates.nestY}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, nestY: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="Y"
                  />
                </div>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  🐭 Mouse Coordinates
                </label>
                <div className="grid grid-cols-2 gap-2">
                  <input
                    type="number"
                    value={coordinates.mouseX}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, mouseX: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="X"
                  />
                  <input
                    type="number"
                    value={coordinates.mouseY}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, mouseY: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="Y"
                  />
                </div>
              </div>
            </div>
            
            <div className="flex gap-3 mt-6">
              <button
                onClick={() => setShowCoordinateModal(false)}
                className="flex-1 bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded transition-colors"
                disabled={isProcessing}
              >
                Cancel
              </button>
              <button
                onClick={handleCoordinateSubmit}
                disabled={isProcessing}
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded transition-colors disabled:opacity-50"
              >
                {isProcessing ? '🔄 Processing...' : '🚀 Start Processing'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default LinuxStatusDashboard;
