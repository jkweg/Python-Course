from dataclasses import dataclass, fields

class BaseConfigSection:
    pass

@dataclass(slots=True, frozen=True)
class AppConfig(BaseConfigSection):
    name: str
    debug: bool

    def validate(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError("Pole 'name' musi być typu str.")
        if not isinstance(self.debug, bool):
            raise TypeError("Pole 'debug' musi być typu bool.")

        if not self.name:
            raise ValueError("Pole 'name' nie może być puste.")
        if len(self.name) < 3:
            raise ValueError("Pole 'name' musi zawierać conajmniej 3 litery.")
        if not self.name.isalpha():
            raise ValueError("Pole 'name' możę zawierać tylko litery.")

    def __str__(self) -> str:
        return ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in fields(self)
        )

    def display(self) -> None:
        print(f"AppConfig: {str(self)}")

@dataclass(slots=True, frozen=True)
class ServerConfig(BaseConfigSection):
    host: str
    port: int

    def validate(self) -> None:
        if not isinstance(self.host, str):
            raise TypeError("Pole 'host' musi być typu str.")
        if not isinstance(self.port, int):
            raise TypeError("Pole 'port' musi być typu int.")
            
        if not self.host:
            raise ValueError("Pole 'host' nie może być puste.")
        if not (1 <= self.port <= 65535):
            raise ValueError("Pole 'port' musi mieścić się w zakresie od 1 do 65535.")
        
@dataclass(slots=True, frozen=True)
class DatabaseConfig(BaseConfigSection):
    username: str
    password: str
    db_name: str

    def validate(self) -> None:
        if not isinstance(self.username, str):
            raise TypeError("Pole 'username' musi być typu str.")
        if not isinstance(self.password, str):
            raise TypeError("Pole 'password' musi być typu str.")
        if not isinstance(self.db_name, str):
            raise TypeError("Pole 'db_name' musi być typu str.")

        if not self.username or not self.password or not self.db_name:
            raise ValueError("Pola bazy danych (username, password, db_name) nie mogą być puste.")


app = AppConfig("MojaAplikacja", True)
app.validate()
app.display()