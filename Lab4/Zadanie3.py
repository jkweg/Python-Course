from typing import override
from datetime import datetime

class Pojazd:

    def __init__(self,marka,model,rok):
        self.marka = marka
        self.model = model
        self.rok = rok
    
    def opis(self):
        return f"Marka: {self.marka}\nModel: {self.model}\nRok: {self.rok}\n"
    
    @classmethod
    def utworz_domyslny(cls):
        return cls("Marka", "Model", 2000)

    @staticmethod
    def czy_poprawny_rok(rok):
        obecny_rok = datetime.now().year
        return 1885 <= int(rok) <= obecny_rok

class Samochod(Pojazd):
    
    def __init__(self, marka, model, rok,iloscDrzwi):
        super().__init__(marka, model, rok)
        self.iloscDrzwi = iloscDrzwi
    
    @override
    def opis(self):
        return f"Marka: {self.marka}\nModel: {self.model}\nRok: {self.rok}\nIlosc drzwi: {self.iloscDrzwi}\n"
    
    @classmethod
    def utworz_domyslny(cls):
        return cls("Volkswagen", "Golf", 2020, 5)


class Motocykl(Pojazd):
    
    def __init__(self, marka, model, rok,typ):
        super().__init__(marka, model, rok)
        self.typ = typ
    
    def opis(self):
        return f"Marka: {self.marka}\nModel: {self.model}\nRok: {self.rok}\nTyp:  {self.typ}\n"
    
    @classmethod
    def utworz_domyslny(cls):
        return cls("Yamaha", "MT-07", 2023, "Naked")
    

auto1 = Samochod("Seat", "Cordoba" , "1996",4)
print(auto1.opis())

motor1 = Motocykl("KTM" , "250" , "2024","Kross")
print(motor1.opis())

pojazd1 = Pojazd.utworz_domyslny()
auto2 = Samochod.utworz_domyslny()
motor2 = Motocykl.utworz_domyslny()

print(pojazd1.opis())
print(auto2.opis())
print(motor2.opis())