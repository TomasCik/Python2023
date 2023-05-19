Pirmas_skaicius = int(input("Įveskite pirmą skaičių: "))

Antras_skaicius = int(input("Įveskite antr1 skaičių: "))

veiksmas = input("kokį veiksmą norite atlikti - sudauginti, sudėti, atimti ar padalinti?")

if veiksmas == "sudauginti":
    a = Pirmas_skaicius * Antras_skaicius
    print(a)

elif veiksmas == "sudėti":
    b = Pirmas_skaicius + Antras_skaicius
    print(b)

elif veiksmas == "atimti":
    c = Pirmas_skaicius - Antras_skaicius
    print(c)

elif veiksmas == "padalinti":
    if b == 0:
        print ("dalyba iš nulio negalima")
    else:
     d = Pirmas_skaicius / Antras_skaicius
         print(d)
