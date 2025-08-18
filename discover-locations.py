#!/usr/bin/env python3

import requests
import json
import time
from datetime import datetime
import os

print("🚀 ADFG Location Discovery Scan")
print("=" * 80)
print("🎯 Purpose: Find all active ADFG locations and identify what we're missing")
print("📊 Scope: Location IDs 1-99, testing all major species")
print("⏱️  Estimated time: 5-10 minutes")
print("=" * 80)

def test_location(location_id, species_id=420, year=2025):
    """Test if a location has data for a species"""
    url = f"https://www.adfg.alaska.gov/sf/FishCounts/index.cfm?ADFG=export.JSON&countLocationID={location_id}&year={year}&speciesID={species_id}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.text
            if '"DATA"' in data and len(data) > 200:
                return True, "Has data"
            else:
                return False, "No data"
        else:
            return False, f"HTTP {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Test species: Sockeye (420) - most common
test_species = 420
active_locations = []

print("🔍 Scanning locations 1-99...")
print("=" * 80)

for location_id in range(1, 100):
    print(f"📍 Testing Location {location_id:2d}...", end=" ")
    
    success, result = test_location(location_id, test_species)
    
    if success:
        active_locations.append(location_id)
        print(f"✅ ACTIVE - Has data")
    else:
        print(f"❌ {result}")
    
    time.sleep(0.5)  # Be respectful to ADFG servers
    
    # Progress update every 10 locations
    if location_id % 10 == 0:
        print(f"📊 Progress: {location_id}/99 locations tested")

print(f"\n🎉 Scan Complete!")
print(f"📊 Results:")
print(f"   Total locations tested: 99")
print(f"   Active ADFG locations: {len(active_locations)}")
print(f"   Active location IDs: {sorted(active_locations)}")

# Check what we have vs what we found
existing_locations = [int(d) for d in os.listdir('.') if d.isdigit()]
print(f"\n📁 Existing in dataset: {sorted(existing_locations)}")
print(f"🌐 Active ADFG found: {sorted(active_locations)}")

# Find missing locations
missing_ids = set(active_locations) - set(existing_locations)
if missing_ids:
    print(f"\n❌ MISSING LOCATIONS: {sorted(missing_ids)}")
    print("These locations have ADFG data but we don't have them!")
else:
    print(f"\n✅ All active ADFG locations are in our dataset!")

# Find extra locations
extra_ids = set(existing_locations) - set(active_locations)
if extra_ids:
    print(f"\n⚠️  EXTRA LOCATIONS: {sorted(extra_ids)}")
    print("These are in our dataset but ADFG doesn't have current data")

print(f"\n📋 Summary:")
print(f"   🌐 ADFG has data for: {len(active_locations)} locations")
print(f"   📁 We have in dataset: {len(existing_locations)} locations")
print(f"   ❌ Missing from dataset: {len(missing_ids)} locations")
print(f"   ⚠️  Extra in dataset: {len(extra_ids)} locations")

if missing_ids:
    print(f"\n🚨 ACTION REQUIRED: Download data for missing locations!")
    print(f"   Missing IDs: {sorted(missing_ids)}")
