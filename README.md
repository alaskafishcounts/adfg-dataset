# 🐟 ADFG Fish Counts Dataset - Local Backup

## 📊 Overview

This is the **local backup copy** of the Alaska Department of Fish & Game (ADFG) fish count data, automatically synced from the main public repository. This dataset covers all monitored locations across Alaska from 1950 to present, providing comprehensive fish population data for research, analysis, and public information.

## ⚠️ Important Note

**This is a backup repository, not the primary data source.** For production use, always access the main repository:
- **Primary Source**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
- **This Backup**: Automatically synced every 6 hours from the primary repository
- **Purpose**: Offline access and backup for the Alaska Fish Counts app

## 🏗️ Data Structure

### 📁 Organization
```
[LocationID]/
  [SpeciesID]/
    [YEAR]-[location-slug]-[species-slug].json
```

### 📊 Example Files
- `79/420/2025-iliuliuk-river-town-creek-sockeye.json`
- `40/420/2025-kenai-river-late-run-sockeye-sockeye.json`
- `13/410/2025-russian-river-chinook.json`

## 🎯 Data Sources

- **Primary Source**: [ADFG Fish Counts Tool](https://www.adfg.alaska.gov/sf/FishCounts/)
- **Update Frequency**: Daily during fishing season
- **Coverage**: 1950-present across all monitored locations
- **Species**: Chinook, Sockeye, Coho, Pink, Chum, Steelhead

## 📈 Current Status

- **Total Locations**: 54 active monitoring stations
- **Total Species**: 6 primary salmon species
- **Data Years**: 1950-2025
- **File Count**: 2,400+ JSON data files
- **Last Updated**: August 18, 2025

## 🔍 Data Format

Each JSON file contains:
```json
{
  "COLUMNS": ["YEAR", "COUNTDATE", "FISHCOUNT", "SPECIESID", "COUNTLOCATIONID", "COUNTLOCATION", "SPECIES"],
  "DATA": [
    [2025, "June, 08 2025 00:00:00", 1, 420, 79, "Iliuliuk River(Town Creek)", "Sockeye"]
  ]
}
```

## 🚀 Usage

### Direct Access
```bash
# Raw GitHub access
curl https://raw.githubusercontent.com/alaskafishcounts/adfg-dataset/main/79/420/2025-iliuliuk-river-town-creek-sockeye.json
```

### Programmatic Access
```javascript
// Fetch specific location/species/year
const response = await fetch('https://raw.githubusercontent.com/alaskafishcounts/adfg-dataset/main/79/420/2025-iliuliuk-river-town-creek-sockeye.json');
const data = await response.json();
```

## 📍 Location Coverage

### Regions
- **Southcentral**: Kenai River, Russian River, Little Susitna
- **Southwest**: Iliuliuk River, Karluk River, Ayakulik River
- **Interior**: Chena River, Salcha River, Gulkana River
- **Southeast**: Situk River, Chilkat River, Taku River

### Monitoring Methods
- **Weirs**: Fixed counting structures
- **Fish Wheels**: Rotating collection devices
- **Visual Counts**: Direct observation
- **Sonar**: Acoustic monitoring

## 🔄 Updates

- **Primary Updates**: Every 6 hours via automated pipeline to [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
- **Backup Sync**: This local copy automatically synced from primary repository
- **Update Frequency**: Daily during fishing seasons, weekly off-season
- **Automated**: GitHub Actions workflow integration
- **Real-time**: Live data from ADFG monitoring stations

## 🏗️ Dual Repository Architecture

This project uses a **dual repository setup** for maximum reliability:

### Primary Repository
- **Public Data Source**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
- **Purpose**: Main data source for all applications and public access
- **Update Frequency**: Every 6 hours via automated pipeline
- **Access**: Public via GitHub raw URLs and CDN

### This Local Backup
- **App Backup**: `afcapp-repo-0101/local-dataset-adfg-data-fish-count`
- **Purpose**: Backup/offline access for the Alaska Fish Counts app
- **Update Frequency**: Automatically synced from primary repository
- **Access**: App-specific backup and offline functionality

### Data Flow
```
ADFG Servers → Pipeline → Primary Repository → Local Backup → Live App
```

## 📚 Documentation

- **Manifest**: `manifest.json` - Complete file index
- **Locations**: Location metadata and coordinates
- **Species**: Species codes and descriptions
- **API**: Data access patterns and examples

## 🤝 Contributing

This dataset is maintained automatically through the ADFG data pipeline. For questions or issues:

- **Primary Data Repository**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
- **App Repository**: [alaskafishcounts/afcapp-repo-0101](https://github.com/alaskafishcounts/afcapp-repo-0101)
- **Live App**: [Alaska Fish Counts](https://alaskafishcounts.com/)

**Note**: This local backup is automatically synced from the primary repository. For data contributions or issues, please use the primary repository.

## 📄 License

Public domain data from the Alaska Department of Fish & Game. Use freely for research, analysis, and public information.

---

**Data Source**: Alaska Department of Fish & Game  
**Maintained By**: Alaska Fish Counts Team  
**Last Updated**: August 18, 2025

