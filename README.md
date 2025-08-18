# 🐟 ADFG Fish Count Data Repository

## 📋 Overview

This repository contains historical fish count data from the Alaska Department of Fish & Game (ADFG) monitoring stations. All data is organized by location and species, with consistent naming conventions maintained across all years (1950-2025).

## 🏗️ Directory Structure

```
adfg-data-fish-count/
├── {location_id}/           # ADFG location ID (e.g., 5, 13, 24)
│   └── {species_id}/        # ADFG species ID (e.g., 410, 420, 430)
│       ├── YYYY-location-slug-species-slug.json
│       ├── YYYY-location-slug-species-slug.json
│       └── ...
```

## 📁 File Naming Convention

### ✅ CORRECT FORMAT
```
YYYY-location-slug-species-slug.json
```

### 🎯 Examples of CORRECT Naming
- `1993-jim-creek-sockeye.json` ✅
- `2025-situk-river-chinook.json` ✅
- `2000-russian-river-sockeye-early-run.json` ✅
- `2015-kenai-river-late-run-sockeye.json` ✅
- `1998-dog-salmon-river-pink.json` ✅ (Note: "Dog Salmon River" is a location name)
- `2025-dog-salmon-river-sockeye.json` ✅ (salmon in location name is allowed)
- `2025-dog-salmon-river-chinook.json` ✅ (salmon in location name is allowed)

### ❌ Examples of INCORRECT FORMATS (NEVER USE)
- `1993-jim-creek-sockeye-salmon.json` ❌ (No `-salmon` suffix on species)
- `2025-situk-river-chinook-salmon.json` ❌ (No `-salmon` suffix on species)
- `2000-russian-river-sockeye-salmon-early-run.json` ❌ (No `-salmon` suffix on species)

## �� CRITICAL NAMING RULES

### 1. **NO `-salmon` SUFFIX on Species Names**
- **Never add** `-salmon` to species names
- **Correct**: `sockeye`, `chinook`, `coho`, `pink`, `chum`
- **Incorrect**: `sockeye-salmon`, `chinook-salmon`, `coho-salmon`

### 2. **Location Names Are Sacred**
- **Never modify** official ADFG location names
- **"Dog Salmon River"** is a legitimate location name - don't change it
- **"Russian River"** is correct - don't add "Upper Station" unless it's in the official name
- **"salmon" in location names is allowed** (e.g., `dog-salmon-river-sockeye.json` ✅)

### 3. **Species Names Are Standardized**
- **Chinook Salmon** → `chinook`
- **Sockeye Salmon** → `sockeye`
- **Coho Salmon** → `coho`
- **Pink Salmon** → `pink`
- **Chum Salmon** → `chum`
- **Steelhead Trout** → `steelhead`
- **Dolly Varden** → `dolly-varden`

### 4. **Run Types Are Preserved**
- **Early Run**: `sockeye-early-run` ✅
- **Late Run**: `sockeye-late-run` ✅
- **Never**: `sockeye-salmon-early-run` ❌

## 🔍 Validation Checklist

Before creating or uploading any file, verify:

- [ ] **No `-salmon` suffix** in the filename
- [ ] **Location name matches** official ADFG location
- [ ] **Species name is standardized** (see species mapping above)
- [ ] **Run types are preserved** but without `-salmon`
- [ ] **Filename follows pattern**: `YYYY-location-slug-species-slug.json`

## 🛠️ Script Validation

### For Download Scripts
Scripts should validate against this README by:

1. **Checking existing files** in the target directory
2. **Finding the most common pattern** (excluding any with `-salmon`)
3. **Using the correct pattern** for new files
4. **Never creating files** with `-salmon` suffix

### Example Validation Logic
```python
def validate_filename(filename):
    """Validate filename against naming conventions"""
    if '-salmon' in filename:
        raise ValueError(f"Filename contains forbidden '-salmon' suffix: {filename}")
    
    # Check other naming rules...
    return True
```

## 📊 Data Quality Standards

### File Content
- **JSON format** with proper structure
- **DATA array** containing fish count records
- **COLUMNS array** defining data structure
- **Metadata** including download timestamp and source

### Historical Consistency
- **Same location-species combination** should have **identical naming** across all years
- **1993-jim-creek-sockeye.json** should match **2025-jim-creek-sockeye.json**
- **No variations** in location or species slugs for the same combination

## 🗂️ Manifest Management

### Manifest Structure
The `manifest.json` file provides a lightweight index of all available data:

```json
{
  "index": {
    "locations": {
      "73": {
        "slug": "jim-creek",
        "species": {
          "420": {
            "slug": "sockeye",
            "years": [2025],
            "total_files": 1
          }
        },
        "total_files": 1
      }
    }
  },
  "metadata": {
    "schema": "v2-lightweight-index-only"
  }
}
```

### Manifest Rules
- **Always rebuild** manifest after adding/removing files
- **Keep lightweight** - no massive `files` array
- **Structure**: `index.locations[locId].species[speciesId].years[]`
- **One file per year** per location-species combination
- **Schema version** must be current and documented

### Manifest Maintenance
- **Auto-rebuild** after any data pipeline runs
- **Validate structure** matches expected schema
- **Update metadata** with generation timestamp
- **Commit changes** immediately after rebuild
- **Push to repository** to keep live app in sync

## 🚫 Common Mistakes to Avoid

1. **Adding `-salmon` suffix** to species names
2. **Modifying official location names** from ADFG
3. **Creating inconsistent naming** across years
4. **Using underscores** instead of hyphens
5. **Truncating location or species names**
6. **Forgetting to rebuild manifest** after file changes
7. **Leaving manifest out of sync** with actual files
8. **Using old manifest schema** (v1 with massive files array)

## 🔧 Maintenance & Cleanup

### Regular Checks
- **Monthly**: Scan for any files with `-salmon` suffix
- **Quarterly**: Verify naming consistency across all years
- **Annually**: Review against ADFG official location/species lists

### Cleanup Commands
```bash
# Find files with forbidden suffixes
find . -name "*-salmon.json"
find . -name "*-salmon-*.json"

# Remove bad files (use with caution)
find . -name "*-salmon.json" -delete

# Validate manifest structure
python3 ../scripts/utilities/build-lightweight-manifest.py

# Check manifest integrity
python3 -c "
import json
with open('manifest.json') as f:
    data = json.load(f)
    print(f'Schema: {data.get(\"metadata\", {}).get(\"schema\", \"unknown\")}')
    print(f'Locations: {len(data.get(\"index\", {}).get(\"locations\", {}))}')
    print(f'Total files: {data.get(\"metadata\", {}).get(\"total_files\", 0)}')
"
```

## 📚 Reference Resources

- **ADFG Fish Counts Tool**: https://www.adfg.alaska.gov/sf/FishCounts/
- **Official ADFG Location IDs**: See ADFG monitoring station database
- **Species Codes**: ADFG official species identification system
- **This Repository**: Single source of truth for naming conventions

## 🆘 Emergency Contacts

If you find naming inconsistencies or need clarification:

1. **Check this README** first
2. **Review existing files** in the same location/species directory
3. **Compare with historical patterns** from 1950-2024
4. **Never guess** - use established patterns only

## 📈 Success Metrics

- **0 files** with `-salmon` suffix
- **100% consistency** in naming across all years
- **100% compliance** with ADFG official names
- **0 naming variations** for same location-species combinations
- **100% manifest accuracy** - manifest matches actual files
- **Lightweight manifest** - under 5,000 lines (no massive files array)
- **Current schema** - always using latest manifest version

---

**🎯 REMEMBER**: This README is the **single source of truth** for file naming conventions. Any script that creates or modifies files in this repository **MUST** follow these rules to maintain data integrity and consistency.

**Last Updated**: 2025-08-11  
**Version**: 1.0  
**Status**: ✅ Active and Enforced
# CDN Refresh Trigger - Tue Aug 12 12:05:49 AKDT 2025

---

## 🧭 Location & Species ID Index

This repository can include a lightweight index of ADFG Location and Species IDs to aid tooling and documentation.

### Files

- `ids-index.json` — Generated index with metadata
- `scripts/build-id-index.py` — Generator that reads masters from the app repo

### Generate

```bash
cd "$(git rev-parse --show-toplevel)/local-dataset-adfg-data-fish-count"
python3 scripts/build-id-index.py
```

This creates `ids-index.json`:

```json
{
  "meta": {
    "version": "1.0.0",
    "generated": "2025-08-12T00:00:00Z",
    "locations": 100,
    "species": 12
  },
  "locations": {
    "40": { "id": 40, "official_name": "Kenai River (Late-Run Sockeye)", "slug": "kenai-river-late-run-sockeye", "region": "Southcentral" }
  },
  "species": {
    "420": { "id": 420, "name": "Sockeye Salmon", "slug": "sockeye" }
  }
}
```

### Fields

- **locations[id]**: `official_name`, `slug`, `region`, `coordinates`
- **species[id]**: `name`, `slug`, `color`

### Purpose

- Document authoritative ID ↔ name/slug mapping
- Help scripts validate filenames and station selections
- Improve discoverability for humans browsing the repo

> Source of truth remains the master files in the app repository: `appprod/data/01-master/master-locations.json` and `master-species.json`.

