import time
import datetime

while True:
    try:
        ivestos_sec = input("Iveskite norimą laiką sekundėmis ( pvz 10): ")
        sek = float(ivestos_sec)
        if sek > 0:
            break
        else:
            print("Skaičius negali būti neigiamas, įveskite teigiamą sekundžių skaičių")

    except ValueError:
        print("Įveskite sekundžių skaičių , tokiu formatu kaip parodyta pavyzdyje!")

zodis = input("Įveskite  žodį: ")
while True:
    print(zodis)
    time.sleep(sek)
