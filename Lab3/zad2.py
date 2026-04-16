import argparse
import yaml
import sys
from pathlib import Path

def flatten_config(config: dict, prefix: str = ""):
    for key, value in config.items():
        full_key = f"{prefix}.{key}" if prefix else key
        
        if isinstance(value, dict):
            yield from flatten_config(value, full_key)
        else:
            yield full_key, value

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=Path, required=True)
args = parser.parse_args()

if not args.config.exists():
    print("Błąd: Plik nie istnieje!")
    sys.exit(1)

with open(args.config, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

gen = flatten_config(config)

try:
    first = next(gen)
    print(f"Pierwsza wartość: {first[0]} = {first[1]}\n")
except StopIteration:
    print("Plik konfiguracji jest pusty lub nie zawiera płaskich wartości.")
    sys.exit(0)

print("Pozostałe pola:")
for path, value in gen:
    print(f"  {path} = {value}")