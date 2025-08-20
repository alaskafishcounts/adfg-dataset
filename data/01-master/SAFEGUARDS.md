# 🛡️ Naming Convention Safeguards

## 🎯 Purpose

This document explains how to use the built-in safeguards to prevent future naming convention violations in the ADFG Fish Count Data Repository.

## 📚 Available Safeguards

### 1. **README.md** - Human Reference
- **Purpose**: Clear documentation of naming rules
- **Use**: Read before creating any files
- **Location**: Repository root

### 2. **validate-naming.py** - Script Validation
- **Purpose**: Programmatic validation of filenames
- **Use**: Import in Python scripts to validate before saving
- **Location**: Repository root

### 3. **naming-config.json** - Machine-Readable Rules
- **Purpose**: JSON configuration for automated validation
- **Use**: Parse in scripts to get naming rules
- **Location**: Repository root

## 🚀 How to Use These Safeguards

### For Human Users

1. **Before creating any files**:
   - Read `README.md` to understand the rules
   - Check `naming-config.json` for quick reference
   - Use the validation checklist in README

2. **When reviewing files**:
   - Look for any `-salmon` suffixes
   - Check for underscores instead of hyphens
   - Verify location names match official ADFG names

### For Script Developers

#### Option 1: Import the Validation Module
```python
import sys
sys.path.append('/path/to/adfg-data-fish-count')
from validate_naming import validate_filename, get_correct_pattern

# Validate before saving
try:
    validate_filename("2025-jim-creek-sockeye.json")
    # Save file
except ValueError as e:
    print(f"❌ Invalid filename: {e}")
    # Handle error
```

#### Option 2: Parse the JSON Config
```python
import json

with open('naming-config.json', 'r') as f:
    config = json.load(f)

forbidden_patterns = config['naming_conventions']['forbidden_patterns']
species_mapping = config['naming_conventions']['species_mapping']

# Use in your validation logic
```

#### Option 3: Use the Pattern Detection
```python
from validate_naming import get_correct_pattern

# Get correct naming pattern from existing files
location_slug, species_slug = get_correct_pattern(
    "Jim Creek", "Sockeye Salmon", 73, 420, "/path/to/repo"
)

filename = f"2025-{location_slug}-{species_slug}.json"
# This will be: "2025-jim-creek-sockeye.json" (correct!)
```

## 🔧 Integration Examples

### In Download Scripts
```python
import os
import json

def download_and_save(location_name, species_name, location_id, species_id, year, repo_path):
    # Get correct naming pattern
    location_slug, species_slug = get_correct_pattern(
        location_name, species_name, location_id, species_id, repo_path
    )
    
    # Generate filename
    filename = f"{year}-{location_slug}-{species_slug}.json"
    
    # Validate before saving
    try:
        validate_filename(filename)
        
        # Save file
        filepath = os.path.join(repo_path, str(location_id), str(species_id), filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
        print(f"✅ Saved: {filename}")
        
    except ValueError as e:
        print(f"❌ Validation failed: {e}")
        # Handle error appropriately
```

### In CI/CD Pipelines
```bash
#!/bin/bash
# Pre-commit hook or CI validation

echo "🔍 Validating naming conventions..."

# Run the validation script
python3 validate-naming.py

# Check for any violations
violations=$(python3 -c "
from validate_naming import scan_repository_for_violations
import sys
violations = scan_repository_for_violations('.')
if violations:
    print(f'Found {len(violations)} violations:')
    for v in violations:
        print(f'  {v[\"file\"]}: {v[\"error\"]}')
    sys.exit(1)
else:
    print('✅ No naming violations found')
")

if [ $? -ne 0 ]; then
    echo "❌ Naming convention violations detected!"
    exit 1
fi
```

## 🚨 Emergency Procedures

### If Bad Files Are Created

1. **Immediate Action**:
   ```bash
   # Find all bad files
   find . -name "*-salmon.json"
   
   # Remove them
   find . -name "*-salmon.json" -delete
   ```

2. **Investigate Root Cause**:
   - Check which script created the bad files
   - Verify the script is using the validation safeguards
   - Update the script if needed

3. **Prevent Future Issues**:
   - Add validation to the problematic script
   - Import `validate-naming.py` module
   - Add pre-save validation

### If Validation Fails

1. **Check the Error Message**: The validation script provides specific details
2. **Review Existing Files**: Look at correct examples in the same directory
3. **Use Pattern Detection**: Let `get_correct_pattern()` find the right naming
4. **Consult README.md**: Double-check the rules

## 📊 Monitoring & Maintenance

### Regular Checks
- **Monthly**: Run `validate-naming.py` to check for violations
- **Quarterly**: Review naming consistency across all years
- **Annually**: Update against ADFG official lists

### Automated Monitoring
```python
# Add to your monitoring scripts
from validate_naming import scan_repository_for_violations

violations = scan_repository_for_violations('/path/to/repo')
if violations:
    send_alert(f"Found {len(violations)} naming violations!")
    # Log violations for review
```

## 🎯 Success Metrics

- **0 files** with `-salmon` suffix
- **100% validation** before file creation
- **100% compliance** with naming conventions
- **0 naming violations** in production

## 📞 Support

If you encounter issues with the safeguards:

1. **Check this document** first
2. **Review README.md** for rules
3. **Test with validate-naming.py** to isolate issues
4. **Check naming-config.json** for configuration details

---

**🛡️ REMEMBER**: These safeguards are only effective if you use them! Always validate filenames before creating or uploading files to the repository.

**Last Updated**: 2025-08-19  
**Version**: 1.0  
**Status**: ✅ Active and Enforced
