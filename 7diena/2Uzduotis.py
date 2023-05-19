import os
import datetime

file_path = "Tekstas.txt"

with open(file_path, "w") as w_failas:
    w_failas.write("Zen of Python\n")

with open(file_path, "a") as data_failas:
    dabar = datetime.datetime.now()
    data_failas.write(dabar.strftime("%Y-%m-%d %H:%M:%S"))

with open(file_path, "a", encoding="utf-8") as nauja_eiluteUK:
    nauja_eiluteUK.write("\nBeautiful is better than ugly.")

naujas = ""
skaicius = 1

with open(file_path, "r") as numeravimas:
    for eilute in numeravimas:
        naujas += str(skaicius) + " " + eilute
        skaicius += 1

with open(file_path, "w") as numeruotas_failas:
    numeruotas_failas.write(naujas)

# Pridedame atvirkščią tekstą prie "Tekstas.txt" failo
with open(file_path, "a", encoding="utf-8") as atbulas_tekstas:
    atbulas_tekstas.write(naujas[::-1])

with open(file_path, "r", encoding="utf-8") as r_failas:
    print(r_failas.read())
