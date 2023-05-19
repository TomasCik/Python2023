zodziu_sarasas = []

for zodziai in range(5):
    zodziai = str(input("prašau įveskite žodį: "))

    zodziu_sarasas.append(zodziai)

a = len(zodziu_sarasas[0])
b = zodziu_sarasas.index(zodziu_sarasas[0])
print(zodziu_sarasas[0], "žodžio ilgis:", a, "vieta saraše: ", b+1)

c = len(zodziu_sarasas[1])
d = zodziu_sarasas.index(zodziu_sarasas[1])
print(zodziu_sarasas[1], "žodžio ilgis:", c, "vieta saraše: ", d+1)

e = len(zodziu_sarasas[2])
f = zodziu_sarasas.index(zodziu_sarasas[2])
print(zodziu_sarasas[2], "žodžio ilgis:", e, "vieta saraše: ", f+1)

g = len(zodziu_sarasas[3])
h = zodziu_sarasas.index(zodziu_sarasas[3])
print(zodziu_sarasas[3], "žodžio ilgis:", g, "vieta saraše: ", h+1)

x = len(zodziu_sarasas[4])
y = zodziu_sarasas.index(zodziu_sarasas[4])
print(zodziu_sarasas[4], "žodžio ilgis:", x, "vieta saraše: ", y+1)

# normaliai versija:
#  Užduotis nr. 3
# word_list = []
# list_lenght = int(input("Kiek zodziu norite ivesti? "))
# for x in range(list_lenght):
#     word_list.append(input(f"Iveskite #{x + 1} zodi"))
#
# for x in range(list_lenght):
#     print(f"Zodis: {word_list[x]}; Ilgis: {len(word_list[x])}; Vieta sarase: {word_list.index(word_list[x])+1}")

