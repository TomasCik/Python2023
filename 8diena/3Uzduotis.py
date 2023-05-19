sarasas = [2, 2.5, "Labas", True, False, 5, 7, 8, 2.8, "Vakaras"]


int_kiekis = sum(type(x) is int for x in sarasas)
float_kiekis =  sum((type(x) is float for x in sarasas))
skaiciu_kiekis = int_kiekis + float_kiekis

print(skaiciu_kiekis)

zodziai = filter(lambda x: isinstance(x, str), sarasas)
tekstas = " ".join(zodziai)
print(tekstas)

# bool_kiekis = sum(isinstance(x, bool) and x for x in sarasas)
# print(bool_kiekis)

# kitokie varintai
filtras = filter(lambda x: type(x) is int or type(x) is float, sarasas)
filtro_list = list(filtras)
print(sum(filtro_list))

string_filtras = filter(lambda x: type(x) is str , sarasas)
filtro_list = list(string_filtras)
sujungta = " ".join(filtro_list)
print(sujungta)


bool_kiekis = sum(c == True for c in sarasas)
print(bool_kiekis)




