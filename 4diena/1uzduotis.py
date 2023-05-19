#
# def skaiciu_suma(skaicius1, skaicius2, skaicius3):
#     suma = skaicius1 + skaicius2 + skaicius3
#     print(suma)
#     return suma
#
# skaiciu_suma(1, 5, 5)
#
# def skaiciu_saraso_suma(sarasas):
#     suma = sum(sarasas)
#     print(suma)
#     return suma
#
# skaiciu_saraso_suma([1, 2, 3])
#
# def max_number(*args):
#     maks = max(args)
#     print(maks)
#     return maks
#

# max_number(1, 2, 3, 4)


def atbulas(zodis):

    atbulas_zodis = zodis[::-1]
    print(atbulas_zodis)
    return atbulas_zodis

# atbulas("labas")
#
# def teksto_analize(tekstas):
#     zodis = 1
#     didziosios = 0
#     mazosios = 0
#     skaicius = 0
#
#     for simbolis in tekstas:
#         if simbolis.isupper():
#             didziosios += 1
#
#         elif simbolis.islower():
#             mazosios += 1
#
#         elif simbolis.isdigit():
#             skaicius += 1
#
#     print("didžiosios: ", didziosios)
#     print("mažosios: ", mazosios)
#     print("skaičiai: ", skaicius)
#
#
# teksto_analize("pEtr1as")

#
# def unikalus_simboliai(tekstas):
#     simboliai = list(set(tekstas))
#     print(simboliai)
#
#
# unikalus_simboliai("petraspa")

#
# def unikalus_simboliai(tekstas):
#     simboliu_sarasas = []
#     for simbolis in tekstas:
#         if simbolis not in simboliu_sarasas:
#             simboliu_sarasas.append(simbolis)
#
#     print(simboliu_sarasas)
#
# unikalus_simboliai("pertrastttas 0 fjgjgfi")





