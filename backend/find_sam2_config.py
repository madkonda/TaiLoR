#!/usr/bin/env python3
"""
Find SAM2 configuration files and check installation
"""

import os
import sys

def find_sam2_configs():
    print("🔍 Searching for SAM2 configuration files...")
    
    # Common SAM2 installation paths
    search_paths = [
        "/home/morsestudio/sam2",
        "/home/morsestudio/anaconda3/envs/sam2",
        "/usr/local",
        "/opt"
    ]
    
    config_files = []
    
    for path in search_paths:
        if os.path.exists(path):
            print(f"📁 Searching in: {path}")
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(('.yaml', '.yml')) and 'sam2' in file.lower():
                        full_path = os.path.join(root, file)
                        config_files.append(full_path)
                        print(f"  ✅ Found: {full_path}")
    
    return config_files

def check_sam2_import():
    print("\n🐍 Checking SAM2 import...")
    try:
        from sam2.build_sam import build_sam2_video_predictor
        print("✅ SAM2 import successful")
        
        # Try to find the config in the package
        import sam2
        sam2_path = os.path.dirname(sam2.__file__)
        print(f"📦 SAM2 package path: {sam2_path}")
        
        # Look for configs in the package
        config_dir = os.path.join(sam2_path, "configs")
        if os.path.exists(config_dir):
            print(f"📁 Config directory found: {config_dir}")
            for root, dirs, files in os.walk(config_dir):
                for file in files:
                    if file.endswith(('.yaml', '.yml')):
                        print(f"  📄 Config file: {os.path.join(root, file)}")
        
        return sam2_path
        
    except ImportError as e:
        print(f"❌ SAM2 import failed: {e}")
        return None

def main():
    print("🚀 SAM2 Configuration Finder")
    print("=" * 50)
    
    # Find config files
    config_files = find_sam2_configs()
    
    # Check SAM2 import
    sam2_path = check_sam2_import()
    
    print("\n📋 Summary:")
    print(f"Found {len(config_files)} config files")
    if sam2_path:
        print(f"SAM2 package path: {sam2_path}")
    
    # Look for the specific config we need
    target_configs = ["sam2.1_hiera_l.yaml", "sam2.1_hiera_large.yaml"]
    for config in target_configs:
        for config_file in config_files:
            if config in config_file:
                print(f"\n🎯 Found target config: {config_file}")
                return config_file
    
    print("\n❌ Target config not found")
    return None

if __name__ == "__main__":
    main()
