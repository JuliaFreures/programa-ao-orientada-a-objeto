class Animal:
    def falar(self):
        return "Som genérico"
class Ave(Animal):
    def falar(self):
        return "Piu"
class Papagaio(Ave):
    def falar(self):
        return super().falar() + " e repete palavras"
p = Papagaio()
print(p.falar())