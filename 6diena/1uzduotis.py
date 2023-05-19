
class Automobilis():

    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.model = modelis
        self.kuras = kuro_tipas
        print(f"{self.metai} {self.model} {self.kuras}")

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

class Elektromobilis(Automobilis):

    def pildyti_degalu(self):
        print ("Baterija įkrauta")



    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")



auto1 = Automobilis("1992", "Focus", "Balta")
auto1.vaziuoti()
auto1.stoveti()
auto1.pildyti_degalu()
print("--------------------------")
auto2 = Elektromobilis("2022", "model3", "juoda")
auto2.vaziuoti()
auto2.stoveti()
auto2.pildyti_degalu()
auto2.vaziuoti_autonomiskai()






