

class Zmogus():
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"Vardas: {self.vardas}, Amžius: {self.amzius}")


zmogus1 = Zmogus("Romas", 19)
zmogus2 = Zmogus("Tomas", 20)
zmogus3 = Zmogus("Domas", 50)

zmones = []
zmones.append(zmogus1)
zmones.append(zmogus2)
zmones.append(zmogus3)
print(zmones)


atbulas_sortas_amziu = sorted(zmones, key=lambda x: x.amzius, reverse=True)
atbulas_sortas_varda = sorted(zmones, key=lambda x: x.vardas, reverse=True)
print(atbulas_sortas_amziu)
print(atbulas_sortas_varda)

from operator import attrgetter
surusiuota = sorted(zmones, key=attrgetter("vardas"), reverse=True)
print(surusiuota)



