#!/usr/bin/env python3
"""
Build ADFG ID Index
Reads master files from appprod/data/01-master/ and writes ids-index.json in this folder.

Usage:
  python3 scripts/build-id-index.py
"""
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
APP_ROOT = ROOT.parents[1] / 'appprod' / 'data' / '01-master'
LOC_FILE = APP_ROOT / 'master-locations.json'
SP_FILE = APP_ROOT / 'master-species.json'
OUT_FILE = ROOT / 'ids-index.json'

def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def normalize_locations(obj):
    # Supports array or map under key 'locations'
    raw = obj.get('locations', [])
    if isinstance(raw, dict):
        raw = list(raw.values())
    out = {}
    for loc in raw:
        if loc is None:
            continue
        loc_id = str(loc.get('id')) if 'id' in loc else None
        if not loc_id:
            continue
        out[loc_id] = {
            'id': loc.get('id'),
            'slug': loc.get('slug'),
            'official_name': loc.get('official_name') or loc.get('name'),
            'region': loc.get('region'),
            'coordinates': loc.get('coordinates')
        }
    return out

def normalize_species(obj):
    raw = obj.get('species', [])
    if isinstance(raw, dict):
        raw = list(raw.values())
    out = {}
    for sp in raw:
        if sp is None:
            continue
        sp_id = str(sp.get('id')) if 'id' in sp else None
        if not sp_id:
            continue
        out[sp_id] = {
            'id': sp.get('id'),
            'slug': sp.get('slug'),
            'name': sp.get('name'),
            'color': sp.get('color')
        }
    return out

def main():
    locs = load_json(LOC_FILE)
    sps = load_json(SP_FILE)
    loc_index = normalize_locations(locs)
    sp_index = normalize_species(sps)
    out = {
        'meta': {
            'version': '1.0.0',
            'generated': datetime.now(timezone.utc).isoformat(),
            'source': {
                'locations': str(LOC_FILE),
                'species': str(SP_FILE)
            },
            'locations': len(loc_index),
            'species': len(sp_index)
        },
        'locations': loc_index,
        'species': sp_index
    }
    with OUT_FILE.open('w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"✅ Wrote {OUT_FILE} with {len(loc_index)} locations and {len(sp_index)} species")

if __name__ == '__main__':
    main()


