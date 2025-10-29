import React, { useState, useEffect } from 'react';

interface LinuxStatus {
  videosDirectory: string;
  resultsDirectory: string;
  videos: string[];
  results: string[];
  processing: string[];
  completed: string[];
  lastUpdate: string;
}

const LinuxStatusDashboard: React.FC = () => {
  const [status, setStatus] = useState<LinuxStatus | null>(null);
  const [isConnected, setIsConnected] = useState(false);

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
                  <div key={index} className="flex items-center gap-2 p-2 bg-gray-600 rounded">
                    <span className="text-lg">{getFileIcon(video)}</span>
                    <span className="text-sm font-mono">{video}</span>
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
                  <div key={index} className="flex items-center gap-2 p-2 bg-gray-600 rounded">
                    <span className="text-lg">{getFileIcon(result)}</span>
                    <span className="text-sm font-mono">{result}</span>
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
    </div>
  );
};

export default LinuxStatusDashboard;
