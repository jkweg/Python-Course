class KontoBankowe:

    def __init__(self,saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Saldo poczatkowe nie moze byc ujemne")  # zakladamy ze to zakladanie nowego konta , wiec nie ma debetu
    
    def wplac(self,kwota):

        if kwota > 0:
            self.__saldo += kwota 
            print(f"Wplacono: {kwota}")
        else:
            print("Kwota nie moze byc ujemna!")
    
    def wyplac(self,kwota):
        if kwota > 0 and kwota <= self.__saldo:
            self.__saldo -= kwota
            print(f"Wyplacono: {kwota}")
        else:
            print("Ujemna kwota lub brak wystarczajacych srodkow na koncie")

    def pokaz_saldo(self):
        return(f"Aktualny stan konta: {self.__saldo}")
    
    @property
    def saldo(self):
        return self.__saldo

konto1 = KontoBankowe(5000)

konto1.pokaz_saldo()
konto1.wplac(2000)
konto1.wplac(-200)
konto1.wyplac(3000)
konto1.wyplac(4001)
print(konto1.pokaz_saldo())