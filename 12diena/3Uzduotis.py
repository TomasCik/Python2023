import math
import logging

# Savo logerio sukūrimas
myLogger = logging.getLogger(__name__)
file_handler = logging.FileHandler("3Uzduotis.log")
myLogger.addHandler(file_handler)
myLogger.setLevel(logging.INFO)
formatavimas = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
file_handler.setFormatter(formatavimas)


# spausdinimas į terminalą
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatavimas)
myLogger.addHandler(stream_handler)




# Sukuriame sumavimo funkciją
def skaiciu_sum(*args):
    suma = sum(args)
    # print(f"Skaiciu suma {args} yra lygi {suma}")
    myLogger.info(f"Skaiciu suma {args} yra lygi {suma}")

skaiciu_sum(4, 5, 6, 8)


# Sukuriame kvadratinės šaknies funkciją
def kvadr_saknis(x):
    try:
        saknis = math.sqrt(x)
        # print(f"Šaknis iš skaičiaus lygi: {saknis}")

    except TypeError:
        myLogger.exception(f"ivesta netinkama reiksme: {x}")


# try:
#     kvadr_saknis(asedfsda)
# except NameError:
#     myLogger.exception(f"ivesta netinkama reiksme: ")




# Sukuriame sakinio simbolių skaičiau funkciją
def sakinio_ilgis(sakinys):
    y = len(sakinys)
    # print(y)
    myLogger.info(f"sakinio simboliu skaicius: {y}")

sakinio_ilgis(" asda asdsdasdasdsd")


# Sukuriame dalybos funkciją
def dalyba(x, y):
    try:
        rezultatas = x/y
    # print (f"Padalinam: {x}/{y} = {rezultatas}")

    except ZeroDivisionError:
        myLogger.info((f"Dalyba is nulio negalima:"))

dalyba(6, 0)

















