from statistics import mean, median


sarasas = list(range(0, 50))
print(sarasas)

padaugintas = map(lambda x: x*10, sarasas)
print(list(padaugintas))

padalintas = filter(lambda x: x % 7 ==0, sarasas)
print(list(padalintas))

kvadratu = map(lambda x: x**2, sarasas)
kvadratu_listas = list(kvadratu)

print(kvadratu_listas)

print(sum(kvadratu_listas))
print(max(kvadratu_listas))
print(min(kvadratu_listas))
print(mean(kvadratu_listas))
print(int(median(kvadratu_listas)))

atbulas_rusiuotas = sorted(kvadratu_listas, reverse=True)
print(atbulas_rusiuotas)

