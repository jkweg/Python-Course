from math import sin, pi, sqrt, exp

# Zadanie:
"""
Przy pomocy w.w. symboli i funkcji zdefiniować:
- cos
- tangens i cotanges
- funkcje hiperboliczne (sin, cos, tan, cotan)
- secans i cosecans
- wszystkie pochodne (pierwszego stopnia) w.w. funkcji
*Opcjonalnie*: użyć biblioteki sympy

Zaproponuj architekturę (ew. obiektową) i logikę wybierania funkcji przez użytkownika w terminalu

Całe rozwiązanie powinno się mieścić w jednym pliku.
Wyświetlać 3 miejsca po przecinku przy pomocy print(f"Wynik: {x}").

"""

def cos(x):
    return sin(x + pi/2)

def tg(x):
    return sin(x)/sin(x + pi/2)

def ctg(x):
    return sin(x + pi/2)/sin(x)




def sinh(x):
    return((exp(x) - exp(-x)) / 2)

def cosh(x):
    return((exp(x) + exp(-x)) / 2)

def tgh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def ctgh(x):
    return (exp(x) + exp(-x)) / (exp(x) - exp(-x))



def sec(x):
    return 1/sin(x + pi/2)

def cosec(x):
    return 1/sin(x)




def d_cos(x):
    return -sin(x)

def d_tg(x):
    return 1 / (sin(x + pi/2) ** 2)

def d_ctg(x):
    return -1 / (sin(x) ** 2)

def d_sec(x):
    return sin(x) / (sin(x + pi/2) ** 2)

def d_cosec(x):
    return -sin(x + pi/2) / (sin(x) ** 2)

def d_sinh(x):
    return (exp(x) + exp(-x)) / 2

def d_cosh(x):
    return (exp(x) - exp(-x)) / 2

def d_tgh(x):
    return 4 / ((exp(x) + exp(-x)) ** 2)

def d_ctgh(x):
    return -4 / ((exp(x) - exp(-x)) ** 2)


class obliczenia:

    def __init__(self,nazwa,funkcja,pochodna):
        self.nazwa = nazwa
        self.funkcja = funkcja
        self.pochodna = pochodna
    
    def oblicz(self,x):
        return self.funkcja(x) , self.pochodna(x)

class Maszyna:

    def __init__(self):

        self.operacje = {
            '1': obliczenia('cos', cos, d_cos),
            '2': obliczenia('tg', tg, d_tg),
            '3': obliczenia('ctg', ctg, d_ctg),
            '4': obliczenia('sec', sec, d_sec),
            '5': obliczenia('cosec', cosec, d_cosec),
            '6': obliczenia('sinh', sinh, d_sinh),
            '7': obliczenia('cosh', cosh, d_cosh),
            '8': obliczenia('tgh', tgh, d_tgh),
            '9': obliczenia('ctgh', ctgh, d_ctgh)
        }
    
    def menu(self):

        print("Mozliwe opcje: \n")

        for klucz , obl in self.operacje.items():
            print(f"{klucz} , {obl.nazwa}\n")
        print("Albo 0 jak nie chcesz nic robic")
    
    def wlacz(self):

        while True:

            self.menu()
            opcja = input("Wybierz opcje (0-9): ").strip()

            if opcja == '0':
                break
                
            if opcja not in self.operacje:
                print("Nie ma takiej opcjii")
                continue

            obliczenie = self.operacje[opcja]

            print(f"Wybrana opcja {obliczenie.nazwa}\n")

            try:
                dane = input("Podaj x do obliczen: ").strip().replace(',','.')
                x = float(dane)
                print("\n")
                print(f"Wyniki dla {x}")

                wynik_funkcja , wynik_pochodna = obliczenie.oblicz(x)
                print("\n")
                print(f"Wynik funkcji: {wynik_funkcja:.3f}\n")
                print(f"Wynik pochodnej: {wynik_pochodna:.3f}")

            except ValueError:
                print("To nie jest dobra liczba")

            print("\n")

            koncowa_opcja = input("Wybierz 0 jak chcesz wyjsc lub cokolwiek innego jak chcesz wykonac inna operacje: ").strip()

            if koncowa_opcja == '0':
                break



if __name__ == "__main__":
    aplikacja = Maszyna()
    aplikacja.wlacz()


