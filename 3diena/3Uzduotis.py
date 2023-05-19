import datetime

while True:
    try:
        ivesti_data = input("Įveskite tikslų gimimo laiką pvz 1901 01 01 05:25 :")
        gimimo_data = datetime.datetime.strptime(ivesti_data, "%Y %m %d %H:%M")
        break
    except ValueError:
        print("įveskite datą parodytu formatu, ar nemokate skaityti??")

data_siandien = datetime.datetime.today()

skirtumas = data_siandien - gimimo_data

metai_skirtumas = round(skirtumas.days / 365)
print("Praejo", metai_skirtumas, "metai")

menesiu_skirtumas = round(metai_skirtumas * 12)
print(menesiu_skirtumas, "menesiai")

print(skirtumas.days, "dienos")

valandu_skirtumas = round(skirtumas.days * 24)
print(valandu_skirtumas, "valandos")

skirtumas_min = round(valandu_skirtumas * 60)
print(skirtumas_min, "minutes")

skirtumas_sec = round(skirtumas_min * 60)
print(skirtumas_sec, "sekundes")

print(round(skirtumas.total_seconds()))

# print(skirtumas)
# print(skirtumas.year)
# print(skirtumas.days)
# # print(" praejo",skirtumas.seconds, "dienos")
# # # print(skirtumas.min)
# # #
# #
# #
# # import datetime
# # now  = datetime.datetime.today()
# # print(now.year)
