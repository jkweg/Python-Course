class Pojazd:

    def __init__(self,marka,model,rok):
        self.marka = marka
        self.model = model
        self.rok = rok
    
    def opis(self):
        return f"{self.marka} {self.model} {self.rok}"

class Samochow(Pojazd):
    

auto1 = Pojazd("Seat", "Cordoba" , "1996")
print(auto1.opis())