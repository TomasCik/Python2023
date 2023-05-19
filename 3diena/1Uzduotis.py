import datetime
while True:
    try:
        ivesta_1data = input("Įveskite pradžios datą formatu metai:mėnuo:diena : ")
        data1 = datetime.datetime.strptime(ivesta_1data, "%Y:%m:%d")
        break
    except ValueError:
        print("įveskite datą parodytu formatu, ar nemokate skaityti??")

while True:
    try:
        ivesta_2data = input("Įveskite pabaigos datą formatu metai:mėnuo:diena : ")
        data2 = datetime.datetime.strptime(ivesta_2data, "%Y:%m:%d")
        if data2 > data1:
            break
        else:
            print("pabaigos data negali būti mažesnė nei pradžios data - tai nelogiška, parinkite kitą datą!")

    except ValueError:
        print("įveskite datą parodytu formatu, ar nemokate skaityti??")


skirtumas = data2 - data1
print("laiko skirtumas: "skirtumas.total_seconds())



