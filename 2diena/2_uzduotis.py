visi_skaiciai = []

while True:
    skaicius = int(input("Įveskite skaičių:"))
    visi_skaiciai.append(skaicius)
    if skaicius <= 0:
        break

suma = 0
for x in visi_skaiciai:
    suma += x

# suma = sum(visi_skaiciai)
print(suma)
