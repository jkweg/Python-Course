import argparse
import yaml
import sys
from pathlib import Path
from dataclasses import dataclass

@dataclass
class AppConfig:
    name: str
    debug: bool

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['app']['name'], debug=data['app']['debug'])

@dataclass
class ServerConfig:
    host: str
    port: int
    timeout: int

    @classmethod
    def from_dict(cls, data):
        return cls(host=data['server']['host'], port=data['server']['port'], timeout=data['server']['timeout'])

@dataclass
class GlobalConfig:
    app: AppConfig
    server: ServerConfig

    @classmethod
    def from_dict(cls, data):
        return cls(
            app=AppConfig.from_dict(data),
            server=ServerConfig.from_dict(data)
        )

def print_pretty(obj, indent=0):
    for key, value in obj.__dict__.items():
        if hasattr(value, "__dict__"):
            print("  " * indent + f"{key}:")
            print_pretty(value, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=Path, required=True)
args = parser.parse_args()

if not args.config.exists():
    print("Błąd: Plik nie istnieje")
    sys.exit(1)

with open(args.config, "r", encoding="utf-8") as file:
    try:
        raw_data = yaml.safe_load(file)
        if raw_data is None:
            print("Błąd: Plik YAML jest pusty")
            sys.exit(1)
            
        config = GlobalConfig.from_dict(raw_data)
        print_pretty(config)

    except yaml.YAMLError:
        print("Błąd: Niepoprawny format pliku YAML")
        sys.exit(1)
    except KeyError as e:
        print(f"Błąd: Brak wymaganego klucza w konfiguracji: {e}")
        sys.exit(1)