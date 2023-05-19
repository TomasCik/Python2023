salys = ["Lietuva", "Latvija", "Estija", "Suomija", "Švedija"]

gyventoju_skaicius = {"Lietuva": 3000000, "Latvija": 1800000, "Estija": 1300000, "Suomija": 5000000,
                      "Švedija": 10000000}


print(gyventoju_skaicius["Lietuva"])

salys.append("Lenkija")
print(salys)

gyventoju_skaicius["Lenkija"] = 38000000
print(gyventoju_skaicius)

salys.pop(2)
print(salys)

gyventoju_skaicius["Lietuva"] = 2800000
print(gyventoju_skaicius)

x = salys.index("Suomija")
print(x)

salys.insert(1, "Norvegija")
print(salys)

salys.remove("Suomija")
print(salys)

salys.clear()
print(salys)







