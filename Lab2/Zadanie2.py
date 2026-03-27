import argparse
import yaml
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=Path, required=True)
args = parser.parse_args()

config_path = args.config

if not config_path.exists():
    print(f"Błąd: Plik {config_path} nie istnieje!")
    exit(1)

with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

def print_config(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print("  " * indent + f"{key}:")
            print_config(value, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")

print_config(config)