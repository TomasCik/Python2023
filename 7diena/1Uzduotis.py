import os
import datetime

with open ("Tekstas.txt", "w") as w_failas:
    w_failas.write("Zen of Python\n")


with open ("Tekstas.txt", "a") as data_failas:
    dabar = datetime.datetime.now()
    data_failas.write(dabar.strftime("%Y-%m-%d %H:%M:%S"))

with open("Tekstas.txt", "a", encoding="utf-8") as nauja_eiluteUK:
    nauja_eiluteUK.write("\nBeautiful is better than ugly." )

naujas = ""
skaicius = 1

with open ("Tekstas.txt", "r") as numeravimas:
    for eilute in numeravimas:
        naujas += str(skaicius) + " " + eilute
        skaicius += 1
with open ("Tekstas.txt", "w") as numeruotas_failas:
    numeruotas_failas.write(naujas)



# pakeičiam tekstą lietuvišku
# with open("Tekstas.txt", "r+") as r_failas:
#     naujas2 = ""
#     senas_tekstas = "\nBeautiful is better than ugly."
#     naujas_tekstas = "\nGražu yra geriau nei bjauru."
#     for eilute2 in r_failas:
#         naujas2 += eilute2.replace(senas_tekstas, naujas_tekstas)
with open("Tekstas.txt", "r+", encoding="utf-8") as failas:
    turinys = failas.read()
    turinys = turinys.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
    failas.seek(0)
    failas.write(turinys)
with open("Tekstas.txt", "a", encoding="utf-8") as w_failas:
    w_failas.write(turinys)

with open ("Tekstas.txt", "r", encoding="utf-8") as r_failas:
    print(r_failas.read())

with open("Tekstas.txt", 'r', encoding="utf-8") as tekstas:
    print(str(tekstas.read())[::-1])


