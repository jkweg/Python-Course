import argparse
import yaml
import sys
from pathlib import Path
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class AppConfig:
    name: str
    debug: bool

@dataclass(slots=True, frozen=True)
class ServerConfig:
    host: str
    port: int
    timeout: int

@dataclass(slots=True, frozen=True)
class AppConfiguration:
    app: AppConfig
    server: ServerConfig

class ConfigSectionIterator:
    def __init__(self, config: dict):
        self._sections = list(config.items())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sections):
            raise StopIteration
        
        section = self._sections[self._index]
        self._index += 1
        return section

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=Path, required=True)
args = parser.parse_args()

if not args.config.exists():
    print("Błąd: Plik nie istnieje!")
    sys.exit(1)

with open(args.config, "r", encoding="utf-8") as file:
    raw_config = yaml.safe_load(file)

iterator = ConfigSectionIterator(raw_config)

app_cfg = None
server_cfg = None

for section_name, section_data in iterator:
    print(f"Przetwarzam sekcję: {section_name}")
    
    if section_name == "app":
        app_cfg = AppConfig(**section_data)
    elif section_name == "server":
        server_cfg = ServerConfig(**section_data)

final_config = AppConfiguration(app=app_cfg, server=server_cfg)

print("\nKonfiguracja załadowana:")
print(f"  {final_config.app}")
print(f"  {final_config.server}")