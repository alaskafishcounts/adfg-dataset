# 🐟 ADFG Fish Counts Dataset

## 📊 Overview

This repository contains the complete Alaska Department of Fish & Game (ADFG) fish count data in JSON format. The dataset covers all monitored locations across Alaska from 1950 to present, providing comprehensive fish population data for research, analysis, and public information.

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

- **Daily**: During active fishing seasons
- **Weekly**: Off-season maintenance
- **Automated**: GitHub Actions workflow integration
- **Real-time**: Live data from ADFG monitoring stations

## 📚 Documentation

- **Manifest**: `manifest.json` - Complete file index
- **Locations**: Location metadata and coordinates
- **Species**: Species codes and descriptions
- **API**: Data access patterns and examples

## 🤝 Contributing

This dataset is maintained automatically through the ADFG data pipeline. For questions or issues:

- **Repository**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
- **App Repository**: [alaskafishcounts/afcapp-repo-0101](https://github.com/alaskafishcounts/afcapp-repo-0101)
- **Live App**: [Alaska Fish Counts](https://alaskafishcounts.com/)

## 📄 License

Public domain data from the Alaska Department of Fish & Game. Use freely for research, analysis, and public information.

---

**Data Source**: Alaska Department of Fish & Game  
**Maintained By**: Alaska Fish Counts Team  
**Last Updated**: August 18, 2025

