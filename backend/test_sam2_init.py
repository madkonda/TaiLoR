#!/usr/bin/env python3
"""
Test SAM2 initialization to find the correct way to load it
"""

import os
import sys

def test_sam2_initialization():
    print("🧪 Testing SAM2 initialization methods...")
    
    try:
        from sam2.build_sam import build_sam2_video_predictor
        print("✅ SAM2 import successful")
        
        # Test different config path formats
        config_paths = [
            "sam2.1_hiera_l.yaml",  # Relative path
            "configs/sam2.1/sam2.1_hiera_l.yaml",  # Relative from sam2 package
            "/home/morsestudio/sam2/sam2/configs/sam2.1/sam2.1_hiera_l.yaml",  # Full path
        ]
        
        checkpoint_path = "/home/morsestudio/sam2/checkpoints/sam2.1_hiera_large.pt"
        
        # Check if checkpoint exists
        if not os.path.exists(checkpoint_path):
            print(f"❌ Checkpoint not found: {checkpoint_path}")
            return False
        
        print(f"✅ Checkpoint found: {checkpoint_path}")
        
        # Try each config path
        for i, config_path in enumerate(config_paths):
            print(f"\n🔬 Testing config path {i+1}: {config_path}")
            try:
                # Try to initialize with CPU device
                predictor = build_sam2_video_predictor(config_path, checkpoint_path, device="cpu")
                print(f"✅ SUCCESS with config path: {config_path}")
                return config_path
            except Exception as e:
                print(f"❌ Failed with config path: {config_path}")
                print(f"   Error: {str(e)[:200]}...")
        
        print("\n❌ All config paths failed")
        return None
        
    except ImportError as e:
        print(f"❌ SAM2 import failed: {e}")
        return None

def check_sam2_working_directory():
    print("\n📁 Checking SAM2 working directory...")
    
    # Check if we need to change to the SAM2 directory
    sam2_dir = "/home/morsestudio/sam2"
    if os.path.exists(sam2_dir):
        print(f"📂 SAM2 directory exists: {sam2_dir}")
        
        # Check for common SAM2 files
        common_files = [
            "sam2/build_sam.py",
            "sam2/configs",
            "checkpoints"
        ]
        
        for file_path in common_files:
            full_path = os.path.join(sam2_dir, file_path)
            if os.path.exists(full_path):
                print(f"  ✅ Found: {file_path}")
            else:
                print(f"  ❌ Missing: {file_path}")
        
        return sam2_dir
    else:
        print(f"❌ SAM2 directory not found: {sam2_dir}")
        return None

def main():
    print("🚀 SAM2 Initialization Test")
    print("=" * 50)
    
    # Check working directory
    sam2_dir = check_sam2_working_directory()
    
    # Test initialization
    working_config = test_sam2_initialization()
    
    if working_config:
        print(f"\n🎯 Working config path: {working_config}")
    else:
        print("\n❌ No working config found")
    
    return working_config

if __name__ == "__main__":
    main()
