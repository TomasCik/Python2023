import math
import logging


logging.basicConfig(filename="2Uzduotis.log", level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s")


# Sukuriame sumavimo funkciją
def skaiciu_sum(*args):
    suma = sum(args)
    # print(f"Skaičių suma {args} yra lygi {suma}")
    logging.info(f"Skaičių suma {args} yra lygi {suma}")
    return suma

skaiciu_sum(4, 5, 6, 8)


# Sukuriame kvadratinės šaknies funkciją
def kvadr_saknis(x):
    try:
        saknis = math.sqrt(x)
        # print(f"Šaknis iš skaičiaus lygi: {saknis}")

    except TypeError:
        logging.exception(f"ivesta netinkama reiksme: {x}")


try:
    kvadr_saknis(asedfsda)
except NameError:
    logging.exception(f"ivesta netinkama reiksme: ")




# Sukuriame sakinio simbolių skaičiau funkciją
def sakinio_ilgis(sakinys):
    y = len(sakinys)
    # print(y)
    logging.info(f"sakinio simboliu skaicius: {y}")
    return y
sakinio_ilgis(" asda asdsdasdasdsd")



# Sukuriame dalybos funkciją
def dalyba(x, y):
    rezultatas = x/y
    # print (f"Padalinam: {x}/{y} = {rezultatas}")
    logging.info((f"Padalinam: {x}/{y} = {rezultatas}"))
    return rezultatas


dalyba(6, 2)

















