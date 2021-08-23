from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration
import glob
from pathlib import Path
import sys

def build_site(schema_dir: Path = Path('./schemas'), site_p: Path = Path('./site') ):
    site_p.mkdir(parents=True, exist_ok=True)
    config = GenerationConfiguration(minify=False, examples_as_yaml=True, expand_buttons=True)

    for schema_p in schema_dir.glob('*.json'):
        print(f'Building {schema_p.name}', file=sys.stdout)
        generate_from_filename(schema_p, site_p / f'{schema_p.stem}.html', config=config)

if __name__ == '__main__':
    build_site()
