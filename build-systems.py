#!/usr/bin/env python3
import json
import os
import glob
from datetime import datetime

print("🚀 Building DEADENDS and HISTORICAL_LOCK systems...")
print("=" * 60)

# Get all JSON files
json_files = glob.glob("**/*.json", recursive=True)
json_files = [f for f in json_files if not f.endswith('manifest.json') and not f.endswith('DEADENDS.json') and not f.endswith('HISTORICAL_LOCK.json')]

print(f"📁 Found {len(json_files)} data files")

# Analyze file patterns
historical_files = []
current_year_files = []

for file_path in json_files:
    try:
        filename = os.path.basename(file_path)
        if filename.startswith('20') and '-' in filename:
            year = int(filename[:4])
            location_species = filename[5:-5]
            
            if year < 2025:
                historical_files.append({
                    'file_path': file_path,
                    'year': year,
                    'location_species': location_species,
                    'locked': True,
                    'reason': 'Historical data - auto-locked'
                })
            else:
                current_year_files.append({
                    'file_path': file_path,
                    'year': year,
                    'location_species': location_species,
                    'locked': False,
                    'reason': 'Current year - always check for updates'
                })
    except Exception as e:
        print(f"⚠️ Error analyzing {file_path}: {e}")

print(f"📊 Analysis Results:")
print(f"   Historical files (locked): {len(historical_files)}")
print(f"   Current year files: {len(current_year_files)}")

# Update HISTORICAL_LOCK.json
lock_data = {
    "version": "1.0.0",
    "description": "Historical data lock system",
    "last_updated": datetime.now().isoformat(),
    "current_year": 2025,
    "historical_cutoff_year": 2024,
    "total_locked_files": len(historical_files),
    "locked_files": historical_files
}

with open('HISTORICAL_LOCK.json', 'w') as f:
    json.dump(lock_data, f, indent=2)
print("✅ Updated HISTORICAL_LOCK.json")

# Update DEADENDS.json
deadends_data = {
    "version": "1.0.0",
    "description": "Permanent record of failed combinations",
    "last_updated": datetime.now().isoformat(),
    "total_deadends": 0,
    "deadends": [],
    "notes": ["Will be populated as pipeline encounters failures"]
}

with open('DEADENDS.json', 'w') as f:
    json.dump(deadends_data, f, indent=2)
print("✅ Updated DEADENDS.json")

print("\n✅ Systems built successfully!")
print(f"🔒 Historical Lock: {len(historical_files)} files locked")
print(f"🚫 Deadends: Ready for failed combination tracking")
