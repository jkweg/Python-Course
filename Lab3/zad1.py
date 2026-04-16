import argparse
import yaml
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=Path, required=True)
args = parser.parse_args()

if not args.config.exists():
    print("Błąd: Plik nie istnieje!")
    sys.exit(1)

with open(args.config, "r", encoding="utf-8") as file:
    try:
        config = yaml.safe_load(file)
        if config is None:
            print("Błąd: Plik YAML jest pusty")
            sys.exit(1)
    except yaml.YAMLError:
        print("Błąd: Niepoprawny format pliku YAML")
        sys.exit(1)

top_level_keys = [key for key in config]

print("Sekcje konfiguracji:")
for idx, section in enumerate(top_level_keys):
    print(f"  [{idx}] {section}")

print() 
if 'server' in config:
    print("Sekcja 'server':")
    server_config = config['server']
    
    keys = list(server_config.keys())
    values = list(server_config.values())
    
    for k, v in zip(keys, values):
        print(f"  {k}  -> {v}")