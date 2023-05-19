


class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, nauja):
        if str(nauja).isdigit():
            self.__verte = nauja
        else:
            print("verte turi būti skaičius")


namas1 = Namas(14, 25)
print(namas1.verte)
namas1.verte = 45
print(namas1.verte)
namas1.verte = "edfe 79 vbeb"
print(namas1.verte)

