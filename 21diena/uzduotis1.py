#
# from enum import Enum
#
# class Irasas:
#     def __init__(self, suma):
#         self.suma = suma
#
# class PajamuIrasas(Irasas):
#     pass
#
# class IslaiduIrasas(Irasas):
#     pass
#
# biudzetas = []
#
# irasas1 = PajamuIrasas(2000)
# irasas2 = IslaiduIrasas(20)
# biudzetas.append(irasas1)
# biudzetas.append(irasas2)
#
# for x in biudzetas:
#     if isinstance(x, PajamuIrasas):
#         print(x.suma)
#         print("čia pajamos")
#
#     elif isinstance(x, IslaiduIrasas):
#         print(x.suma)
#         print("Čia išlaidos")

#
#
#
#
#
#
#



from enum import Enum

class IrasoTipas(Enum):
    PAJAMOS = 'Pajamos'
    ISLAIDOS = 'Išlaidos'

class Irasas:
    def __init__(self, suma, tipas):
        self.suma = suma
        self.tipas = tipas

biudzetas = []

irasas1 = Irasas(2000, IrasoTipas.PAJAMOS)
irasas2 = Irasas(20, IrasoTipas.ISLAIDOS)
biudzetas.append(irasas1)
biudzetas.append(irasas2)

for irasas in biudzetas:
    if irasas.tipas == IrasoTipas.PAJAMOS:
        print(irasas.suma)
        print("Čia pajamos")
    elif irasas.tipas == IrasoTipas.ISLAIDOS:
        print(irasas.suma)
        print("Čia išlaidos")









