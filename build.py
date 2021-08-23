from json_schema_for_humans.generate import generate_from_filename
import glob
from pathlib import Path

if __name__ == '__main__':
    site_p = Path('./site')
    site_p.mkdir(parents=True, exist_ok=True)
    
    for schema_p in Path('./schemas').glob('*.json'):
        generate_from_filename(schema_p, site_p / f'{schema_p.stem}.html')
