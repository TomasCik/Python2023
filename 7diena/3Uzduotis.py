import os
import datetime


os.chdir("C:\\Users\\tomas\\Desktop")
# os.mkdir("Naujas katalogas")

os.chdir("C:\\Users\\tomas\\Desktop\\Naujas katalogas")
with open ("Tekstas.txt", "w") as w_failas:

with open ("Tekstas.txt", "a") as data_failas:
    w_failas.write("Tekstas.txt")
    dabar = datetime.datetime.now()
    data_failas.write(dabar.strftime("%Y-%m-%d %H:%M:%S"))


