# 🐟 Alaska Fish Count Data Repository

**Official fish count data from Alaska Department of Fish & Game (ADFG) monitoring stations**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/alaskafishcounts/adfg-dataset)
[![License](https://img.shields.io/badge/License-Public%20Domain-green.svg)](LICENSE)
[![Data Source](https://img.shields.io/badge/Data%20Source-ADF%26G%20Official-blue.svg)](https://www.adfg.alaska.gov/)

## 📊 About This Repository

This repository contains official fish count data from 58+ monitoring stations across Alaska, operated by the Alaska Department of Fish & Game (ADF&G). The data is automatically synchronized from ADF&G's official sources and made available for public use.

### 🎯 Purpose
- **Public Data Access**: Provide easy access to official ADF&G fish count data
- **Application Support**: Serve as the data source for the [Alaska Fish Count App](https://alaskafishcounts.com)
- **Research & Analysis**: Enable researchers, anglers, and the public to analyze fish populations
- **Transparency**: Ensure public access to government fish monitoring data

## 📁 Repository Structure

```
adfg-dataset/
├── manifest.json          # Data index and metadata
├── README.md             # This file
├── 1/                    # Location ID 1 (e.g., Kenai River)
│   ├── 410/              # Species ID 410 (Chinook Salmon)
│   │   ├── 2025-kenai-river-chinook.json
│   │   ├── 2024-kenai-river-chinook.json
│   │   └── ...
│   ├── 420/              # Species ID 420 (Sockeye Salmon)
│   │   ├── 2025-kenai-river-sockeye.json
│   │   └── ...
│   └── ...
├── 5/                    # Location ID 5 (e.g., Russian River)
│   └── ...
└── ...                   # Additional locations
```

### 📋 File Naming Convention
- **Format**: `YEAR-location-slug-species-slug.json`
- **Example**: `2025-kenai-river-chinook.json`
- **Location Slug**: Lowercase, hyphenated location name
- **Species Slug**: Lowercase, hyphenated species name

## 🐟 Supported Species

| Species ID | Common Name | Scientific Name | Color Code |
|------------|-------------|-----------------|------------|
| 410 | Chinook Salmon (King) | *Oncorhynchus tshawytscha* | Blue |
| 420 | Sockeye Salmon (Red) | *Oncorhynchus nerka* | Red |
| 430 | Coho Salmon (Silver) | *Oncorhynchus kisutch* | Green |
| 440 | Pink Salmon (Humpy) | *Oncorhynchus gorbuscha* | Pink |
| 450 | Chum Salmon (Dog) | *Oncorhynchus keta* | Yellow/Orange |
| 561 | Steelhead Trout | *Oncorhynchus mykiss* | Purple |

### 🏃 Run Types
Some species have multiple run types:
- **Early Run**: Spring/early summer arrivals
- **Late Run**: Late summer/fall arrivals
- **Mixed Run**: Combined early and late runs

## 📍 Monitoring Locations

This repository contains data from **58+ monitoring stations** across Alaska, including:

### 🏔️ Major Regions
- **Southcentral Alaska**: Kenai River, Russian River, Ship Creek
- **Southeast Alaska**: Fish Creek, Montana Creek, Steep Creek
- **Interior Alaska**: Chena River, Salcha River, Clear Creek
- **Southwest Alaska**: Kvichak River, Naknek River, Alagnak River

### 🎯 Location Coverage
- **Rivers & Streams**: Primary salmon spawning habitats
- **Fish Passes**: Artificial structures for fish counting
- **Weirs**: Natural barriers used for monitoring
- **Sonar Sites**: Advanced acoustic monitoring stations

## 📊 Data Format

Each JSON file contains structured fish count data:

```json
{
  "metadata": {
    "location_id": 1,
    "location_name": "Kenai River",
    "species_id": 420,
    "species_name": "Sockeye Salmon",
    "year": 2025,
    "last_updated": "2025-01-28T10:00:00Z",
    "data_source": "ADF&G Official"
  },
  "data": [
    {
      "date": "2025-06-15",
      "count": 1250,
      "cumulative": 1250,
      "notes": "Daily fish count"
    },
    {
      "date": "2025-06-16", 
      "count": 1875,
      "cumulative": 3125,
      "notes": "Daily fish count"
    }
  ]
}
```

### 📈 Data Fields
- **date**: Date of the count (YYYY-MM-DD format)
- **count**: Number of fish counted on that date
- **cumulative**: Running total for the season
- **notes**: Additional information about the count

## 🔄 Data Updates

### ⏰ Update Schedule
- **Automatic**: Data is synchronized every 6 hours during peak season
- **Manual**: Updates can be triggered manually via GitHub Actions
- **Real-time**: New data appears within hours of ADF&G updates

### 📅 Seasonal Patterns
- **Spring**: Early-run Chinook and Steelhead
- **Summer**: Peak salmon runs (June-August)
- **Fall**: Late-run salmon and spawning completion
- **Winter**: Limited monitoring, data may be sparse

## 🛠️ Usage Examples

### 📱 Web Application
Visit [Alaska Fish Count App](https://alaskafishcounts.com) for an interactive interface.

### 🔗 Direct API Access
```javascript
// Fetch manifest to discover available data
const manifest = await fetch('https://raw.githubusercontent.com/alaskafishcounts/adfg-dataset/master/manifest.json')
  .then(response => response.json());

// Access specific location/species/year data
const data = await fetch('https://raw.githubusercontent.com/alaskafishcounts/adfg-dataset/master/1/420/2025-kenai-river-sockeye.json')
  .then(response => response.json());
```

### 📊 Data Analysis
```python
import requests
import json

# Get manifest
manifest_url = "https://raw.githubusercontent.com/alaskafishcounts/adfg-dataset/master/manifest.json"
manifest = requests.get(manifest_url).json()

# Find available data for Kenai River Sockeye
kenai_sockeye = manifest['organized']['1']['species']['420']['files']
print(f"Available years: {list(kenai_sockeye.keys())}")
```

## 🔗 Related Resources

### 🌐 Official Sources
- **[ADF&G Fish Counts](https://www.adfg.alaska.gov/sf/FishCounts/)**: Official ADF&G fish count website
- **[ADF&G Sport Fish](https://www.adfg.alaska.gov/sf/)**: Sport fishing information
- **[ADF&G Commercial Fisheries](https://www.adfg.alaska.gov/Commercial/)**: Commercial fishing data

### 📱 Applications
- **[Alaska Fish Count App](https://alaskafishcounts.com)**: Interactive web application
- **[Mobile App](https://alaskafishcounts.com)**: Mobile-optimized interface
- **[API Documentation](https://alaskafishcounts.com/api)**: Developer resources

### 📚 Documentation
- **[Data Dictionary](https://alaskafishcounts.com/docs)**: Detailed field descriptions
- **[API Reference](https://alaskafishcounts.com/api/docs)**: Technical documentation
- **[User Guide](https://alaskafishcounts.com/guide)**: How to use the data

## 📄 License & Attribution

### 📜 License
This data is in the **Public Domain** and available for unrestricted use.

### 🏛️ Attribution
When using this data, please attribute:
- **Data Source**: Alaska Department of Fish & Game (ADF&G)
- **Repository**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
- **Application**: [Alaska Fish Count App](https://alaskafishcounts.com)

### 📊 Citation
```
Alaska Department of Fish & Game. (2025). Fish Count Data. 
Retrieved from https://github.com/alaskafishcounts/adfg-dataset
```

## 🤝 Contributing

### 🐛 Reporting Issues
- **Data Issues**: Report data problems via [GitHub Issues](https://github.com/alaskafishcounts/adfg-dataset/issues)
- **Feature Requests**: Suggest improvements for the data structure
- **Documentation**: Help improve this README or other documentation

### 🔧 Development
- **Data Pipeline**: Contribute to the automated data synchronization
- **Validation**: Help improve data quality checks
- **Documentation**: Enhance user guides and technical docs

## 📞 Support & Contact

### 🆘 Getting Help
- **GitHub Issues**: [Report problems](https://github.com/alaskafishcounts/adfg-dataset/issues)
- **Email**: [support@alaskafishcounts.com](mailto:support@alaskafishcounts.com)
- **Documentation**: [User Guide](https://alaskafishcounts.com/guide)

### 📧 Contact Information
- **Project Maintainer**: Alaska Fish Count App Team
- **Data Source**: Alaska Department of Fish & Game
- **Repository**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)

---

**Last Updated**: January 28, 2025  
**Version**: AFCA v1.0.1  
**Data Source**: Alaska Department of Fish & Game (ADF&G)  
**Repository**: [alaskafishcounts/adfg-dataset](https://github.com/alaskafishcounts/adfg-dataset)
