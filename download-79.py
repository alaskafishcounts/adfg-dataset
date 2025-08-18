#!/usr/bin/env python3

import requests
import json
import os
import time

print("🚀 Downloading Complete Data for Location 79 (Montana Creek)")
print("=" * 80)

# All species to test
species_list = [
    (410, "Chinook"),
    (420, "Sockeye"), 
    (430, "Coho"),
    (440, "Pink"),
    (450, "Chum")
]

# Test years: 2020-2025 (recent range)
years = list(range(2020, 2026))

successful_downloads = []

for year in years:
    print(f"\n📅 Testing year {year}...")
    
    for species_id, species_name in species_list:
        print(f"  🐟 Testing {species_name} (ID: {species_id})...", end=" ")
        
        url = f"https://www.adfg.alaska.gov/sf/FishCounts/index.cfm?ADFG=export.JSON&countLocationID=79&year={year}&speciesID={species_id}"
        
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
                    # Create directory structure
                    os.makedirs(f"79/{species_id}", exist_ok=True)
                    
                    # Generate filename
                    filename = f"79/{species_id}/{year}-montana-creek-{species_name.lower()}.json"
                    
                    # Save the data
                    with open(filename, 'w') as f:
                        f.write(data)
                    
                    # Parse to get actual fish count
                    try:
                        json_data = json.loads(data)
                        fish_count = len(json_data.get('DATA', []))
                        print(f"✅ {fish_count} records - SAVED")
                        
                        successful_downloads.append({
                            'year': year,
                            'species': species_name,
                            'species_id': species_id,
                            'filename': filename,
                            'fish_count': fish_count
                        })
                    except:
                        print(f"✅ SAVED (parse error)")
                else:
                    print(f"❌ No data")
            else:
                print(f"❌ HTTP {response.status_code}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        # Small delay to be respectful
        time.sleep(0.5)

# Summary
print(f"\n" + "=" * 60)
print(f"🎉 Download Complete!")
print(f"📊 Results:")
print(f"   Total downloads attempted: {len(species_list) * len(years)}")
print(f"   Successful downloads: {len(successful_downloads)}")

if successful_downloads:
    print(f"\n📁 Files downloaded:")
    for download in successful_downloads:
        print(f"   {download['filename']} - {download['fish_count']} records")
    
    print(f"\n🔍 Analysis:")
    print(f"   Location 79 is Montana Creek")
    print(f"   Primary species: {', '.join(set(d['species'] for d in successful_downloads))}")
    print(f"   Data range: {min(d['year'] for d in successful_downloads)} - {max(d['year'] for d in successful_downloads)}")
else:
    print(f"\n❌ No data found for location 79")
