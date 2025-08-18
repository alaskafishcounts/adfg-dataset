# 🛡️ Naming Convention Safeguards

## 🎯 Purpose

This document explains the **CORRECT** naming conventions used in the ADFG Fish Count Data Repository and how to maintain consistency going forward.

## 📋 **CORRECT NAMING CONVENTION (ENFORCED)**

### **File Format**
```
{year}-{location-slug}-{species-slug}.json
```

### **Examples of CORRECT Naming**
- `2025-situk-river-chinook.json` ✅
- `2025-gulkana-river-sockeye.json` ✅
- `2025-coghill-river-sockeye.json` ✅
- `2025-eshamy-creek-sockeye.json` ✅
- `2025-jim-creek-sockeye.json` ✅
- `2025-kenai-river-chinook.json` ✅

### **Examples of INCORRECT Naming (FORBIDDEN)**
- `2025-location-chinook.json` ❌ (generic "location")
- `2025-situk-river-chinook-salmon.json` ❌ (extra "salmon" suffix)
- `2025_situk_river_chinook.json` ❌ (underscores instead of hyphens)
- `2025-situk-river-sockeye-salmon.json` ❌ (extra "salmon" suffix)

## 🚨 **CRITICAL RULES - NEVER VIOLATE**

### **1. Location Names**
- **MUST** use official slugs from `master-locations.json`
- **NEVER** use generic terms like "location", "river", "creek"
- **ALWAYS** use the exact slug (e.g., "situk-river", "gulkana-river")

### **2. Species Names**
- **MUST** use short, consistent names
- **NEVER** include "salmon", "trout", or other taxonomic suffixes
- **ALWAYS** use: `chinook`, `sockeye`, `coho`, `pink`, `chum`, `steelhead`, `rainbow`, `dolly-varden`, `pacific-lamprey`

### **3. File Structure**
- **MUST** use hyphens (`-`) between components
- **NEVER** use underscores (`_`) or spaces
- **ALWAYS** follow: `{year}-{location-slug}-{species-slug}.json`

## 🔧 **AUTOMATED SAFEGUARDS SYSTEM**

### **1. Master Data Integration (ENFORCED)**
The download script (`adfg-data-pipeline.py`) now **STRICTLY ENFORCES**:
- **REQUIRED**: Loads `master-locations.json` from the app
- **REQUIRED**: Uses official location slugs for naming
- **NO FALLBACKS**: Cannot generate filenames without master data
- **VALIDATION**: Every filename is validated against SAFEGUARDS.md rules
- **ERRORS**: Script fails if naming conventions are violated

### **2. Validation Functions**
```python
def validate_filename(filename):
    """
    Validate filename against correct naming convention
    """
    # Check format: year-location-species.json
    if not re.match(r'^\d{4}-[a-z0-9-]+-[a-z0-9-]+\.json$', filename):
        raise ValueError(f"Invalid filename format: {filename}")
    
    # Check for forbidden patterns
    forbidden_patterns = [
        '-salmon.json',
        '-trout.json',
        'location-',
        # REMOVED: 'river-', 'creek-' - these are VALID in official location slugs
        # Official slugs like 'situk-river', 'gulkana-river' are CORRECT
    ]
    
    for pattern in forbidden_patterns:
        if pattern in filename:
            raise ValueError(f"Forbidden pattern '{pattern}' in filename: {filename}")
    
    return True
```

### **3. Pre-Save Validation**
```python
def save_file_with_validation(data, location_id, species_id, year, location_slug, species_slug):
    """
    Save file with automatic naming validation
    """
    filename = f"{year}-{location_slug}-{species_slug}.json"
    
    # Validate before saving
    try:
        validate_filename(filename)
        
        # Save file
        filepath = f"{location_id}/{species_id}/{filename}"
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
        print(f"✅ Saved with correct naming: {filename}")
        return True
        
    except ValueError as e:
        print(f"❌ Naming validation failed: {e}")
        return False
```

## 📊 **CURRENT REPOSITORY STATUS**

### **✅ Correctly Named Files**
- **Location 5 (Situk River)**: `2025-situk-river-chinook.json`
- **Location 6 (Gulkana River)**: `2025-gulkana-river-sockeye.json`
- **Location 7 (Coghill River)**: `2025-coghill-river-sockeye.json`
- **Location 8 (Eshamy Creek)**: `2025-eshamy-creek-sockeye.json`
- **Location 72 (Kenai River)**: `2025-kenai-river-chinook.json`

### **❌ Previously Incorrect Files (CLEANED UP)**
- ~~`2025-location-chinook.json`~~ (removed)
- ~~`2024-location-chinook.json`~~ (removed)
- ~~`2023-location-chinook.json`~~ (removed)

## 🚀 **HOW TO MAINTAIN CONSISTENCY**

### **For Developers**

1. **Always use the download script**: `adfg-data-pipeline.py`
2. **Never manually create files** with custom names
3. **The script automatically uses correct naming** from master data

### **For Data Updates**

1. **Run the pipeline script**:
   ```bash
   python3 adfg-data-pipeline.py --download LOCATIONS --species SPECIES --years START,END
   ```

2. **Script automatically**:
   - Loads master locations data
   - Uses correct location slugs
   - Generates proper filenames
   - Validates before saving

### **For Manual Verification**

1. **Check file naming**:
   ```bash
   # Find any files with "location" in name
   find . -name "*location*" -type f
   
   # Find any files with "salmon" suffix
   find . -name "*-salmon.json" -type f
   ```

2. **Expected result**: No files should be found

## 🔍 **MONITORING & ENFORCEMENT**

### **Automated Checks**
The download script now includes:
- **Pre-save validation** of all filenames
- **Master data integration** for consistent naming
- **Automatic slug detection** from existing files
- **Error logging** for any naming violations

### **Manual Audits**
- **Weekly**: Check for any new incorrectly named files
- **Monthly**: Verify naming consistency across all locations
- **Quarterly**: Review against ADFG official naming standards

### **Violation Response**
If incorrectly named files are found:

1. **Immediate removal** of bad files
2. **Investigation** of how they were created
3. **Fix the source** (script or manual process)
4. **Re-run download** with correct naming

## 📚 **REFERENCE DATA SOURCES**

### **Master Locations File**
- **Path**: `appprod/data/01-master/master-locations.json`
- **Purpose**: Official location slugs and metadata
- **Usage**: Script automatically loads this for naming

### **Master Species File**
- **Path**: `appprod/data/01-master/master-species.json`
- **Purpose**: Official species names and codes
- **Usage**: Script uses this for species naming

### **Location-Species Combinations**
- **Path**: `appprod/data/01-master/master-combos.json`
- **Purpose**: Valid location-species combinations
- **Usage**: Script validates combinations before downloading

## 🎯 **SUCCESS METRICS**

- **100% of files** follow correct naming convention
- **0 files** with generic "location" names
- **0 files** with extra taxonomic suffixes
- **100% consistency** across all years and locations
- **Automated validation** prevents future violations

## 🚨 **EMERGENCY PROCEDURES**

### **If Bad Files Are Created**

1. **Stop the process** immediately
2. **Remove bad files**:
   ```bash
   find . -name "*location*" -delete
   find . -name "*-salmon.json" -delete
   ```
3. **Fix the source** (script or process)
4. **Re-run with correct naming**

### **If Validation Fails**

1. **Check the error message** for specific details
2. **Verify master data** is loaded correctly
3. **Check file paths** and permissions
4. **Review script logs** for debugging info

## 📞 **SUPPORT & MAINTENANCE**

### **For Issues**
1. **Check this document** first
2. **Review script logs** for error details
3. **Verify master data** is accessible
4. **Test with small downloads** first

### **For Updates**
1. **Update master data** files as needed
2. **Test naming consistency** after changes
3. **Update this document** to reflect changes
4. **Verify all locations** maintain correct naming

---

**🛡️ REMEMBER**: The naming convention is now **AUTOMATED** and **ENFORCED** by the download script. Always use the script to maintain consistency!

**Last Updated**: 2025-08-12  
**Version**: 3.0  
**Status**: ✅ Active, **STRICTLY ENFORCED**, No Fallbacks, No Exceptions
