class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def rasyti_atbulai(self):
        print(self.tekstas[::-1])

    def rasyti_mazosiomis(self):
        print(self.tekstas.lower())

    def rasyti_didziosiomis(self):
        print(self.tekstas.upper())

    def eiles_numeris(self, vieta):
        splitted_text = self.tekstas.split()
        print(splitted_text[vieta - 1])

    def simboliu_skaicius(self, simbolis):
        print(self.tekstas.count(simbolis))
#

    def pakeisti_simbolius(self, senas_simbolis, naujas_simbolis):
        keiciami = self.tekstas.replace(senas_simbolis, naujas_simbolis)
        print(keiciami)

    def skaiciuojam_simboliu_savybes(self, simbolis):
        didziosios = self.tekstas.upper()
        print(didziosios.count(simbolis.upper()))

    def upper_lower_digits(self, skaicius):
        tekstas = self.tekstas
        lower = 0
        upper = 0
        digits = 0
        rezultatas = 0
        for x in tekstas:
            if x.islower():
                lower += 1
            elif x.isupper():
                upper += 1
            elif x.isdigit():
                digits += 1
        if skaicius == 1:
            rezultatas = upper
        elif skaicius == 2:
            rezultatas = lower
        elif skaicius == 3:
            rezultatas = digits
        print (rezultatas)

tekstas1 = Sakinys("Petras  Bugailiskis petraitis")
tekstas1.rasyti_atbulai()
tekstas1.rasyti_mazosiomis()
tekstas1.rasyti_didziosiomis()
tekstas1.eiles_numeris(3)
tekstas1.simboliu_skaicius("P")
tekstas1.pakeisti_simbolius("a", "e")
tekstas1.upper_lower_digits()

# tekstas = "Petras petraitis"
# tekstas = tekstas.count("p")
# print(tekstas)





