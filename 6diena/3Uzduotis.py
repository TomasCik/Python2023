class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass

biudzetas = []

irasas1 = PajamuIrasas(2000)
irasas2 = IslaiduIrasas(20)
biudzetas.append(irasas1)
biudzetas.append(irasas2)

for x in biudzetas:
    if isinstance(x, PajamuIrasas):
        print(x.suma)
        print("čia pajamos")

    elif isinstance(x, IslaiduIrasas):
        print(x.suma)
        print("Čia išlaidos")




