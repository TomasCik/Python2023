
print("Keliamųjų metų skaičiuoklė")


metai1 = int(input("Įveskite metus: "))
metai2 = int(input("Įveskite antrus metus: "))
sarasas = []

for metai in range(metai1, metai2):
    if (metai % 400 ==0) or (metai % 100 != 0 and metai % 4  == 0):
        sarasas.append(metai)


print("Keliamųji metai yra:", sarasas)
input("spauskite bet kurį klavišą norėdami išeiti")











