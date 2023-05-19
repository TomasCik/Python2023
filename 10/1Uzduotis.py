

class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, nauja_verte):
        if nauja_verte < 0:
            print("Vertė negali būti neigiama!")
        else:
            self.__verte = nauja_verte

namas1 = Namas(150, 20000)
namas2 = Namas(200, 330000)

namas1.verte = 220000
namas2.verte = 600000
print(namas1.plotas, namas1.verte)
print(namas2.plotas, namas2.verte)
