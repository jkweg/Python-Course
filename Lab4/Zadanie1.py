class Student:
    def __init__(self,imie,nazwisko,indeks):
        self.imie = imie
        self.nazwisko = nazwisko
        self.indeks = indeks
    
    def przedstaw_sie(self):
        print(f"Imie: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Indeks: {self.indeks}")
    
    def __str__(self):
        return f"Imie: {self.imie} \nNazwisko: {self.nazwisko} \nIndeks: {self.indeks}"

student1 = Student("Jakub" , "Węgrzyniak" , "424737")
student2 = Student("Krystian", "Augustyn" , "426498")

student1.przedstaw_sie()
print()
student2.przedstaw_sie()

print()

print(student1)