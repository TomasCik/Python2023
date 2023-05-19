# # # # def kvadratas(skaicius):
# # # #     kvadratu = skaicius **2
# # # #     # print(f"Jūsų skaičius pakeltas kvadratu lygus : " {kvadratu})
# # # #     print("Jūsų skaičius pakeltas kvadratu lygus: ", kvadratu)
# # # #     return kvadratu
# # # #
# # # # ivesti_skaiciu  = int(input("Įveskite skaičių: "))
# # # #
# # # # kvadratas(ivesti_skaiciu)
# # # #
# # #
# # # def daug_kvadratu(*args):
# # #     for skaicius in args:
# # #         print(skaicius **2)
# # #
# # # ivesti_skaiciu  = int(input("Įveskite skaičių arba kelis atskirtus kableliu: "))
# # #
# # # daug_kvadratu(ivesti_skaiciu)
# # #
# # #
# # # #
# # # # def pasisveikinti (vardas):
# # # #     print(f"sveikas, {vardas}")
# # # #     return vardas
# # # #
# # # # ivesti_varda = input("įveskite vardą: ")
# # # #
# # # # pasisveikinti(ivesti_varda)
# #
# # # sarasas = [1, 2, 3, 4]
# # #
# # # sarasas_2 = []
# # # for skaicius in sarasas:
# # #     sarasas_2.append(skaicius ** 2)
# # #
# # # print(sarasas_2)
# #
# #
# # # sarasas = [1, 2, 5]
# # # suma = 0
# # # for x in sarasas:
# # #     suma += x
# # # print(suma)
# #
# #
# # sarasas = [4, 3, 2, 1]
# # naujas = filter(lambda x: x<2, sarasas)
# # print(list(naujas))
# #
# # sarasas = [2, 2.5, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# #
# # int_kiekis = sum(isinstance(x, int) for x in sarasas)
# # float_kiekis = sum(isinstance(x, float) for x in sarasas)
# # skaiciu_kiekis = int_kiekis + float_kiekis
# #
# # print(skaiciu_kiekis)
# #
# # zodziai = [x for x in sarasas if isinstance(x, str)]
# # print(zodziai)
# # #
# # #
# # #
# # #
# # for a in range(5):
# #     if a == 2:
# #         print("Pasiekeme 2")
# #
# #     if a == 3:
# #         print (a)
# #
#
# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas =  vardas
#         self.pavarde = pavarde
#         self.__atlyginimas = atlyginimas
#
#     def __repr__(self):
#
#             return f"Vardas: {self.vardas}, Pavarde: {self.pavarde}, Atlyginimas: {self.__atlyginimas}"
#
#     @property
#     def atlyginimas(self):
#         return self.__atlyginimas
#
#     @atlyginimas.setter
#     def atlyginimas(self, naujas):
#
#         if naujas < 0:
#             print ("atlyginimas negali būti neigiamas")
#         else:
#             self.__atlyginimas = naujas
#
#
#
#
#
# Domas = Darbuotojas ("Domas", "Domavicius", 1200)
# print(Domas.atlyginimas)
#
#
# Domas.atlyginimas = 1500
# print(Domas.atlyginimas)
# print(Domas)
#
x = "   abc   asd     "
x.rstrip()
print(x.rstrip())
#
#
#
#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
