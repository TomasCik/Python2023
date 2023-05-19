from enum import Enum

class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuTipas(Enum):
    alga = "Darbo uzmokestis"
    pasalpa = "Pasalpa"
    kita = "Kita"

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija, tipas):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija
        self.tipas = tipas

class IslaiduTipas(Enum):
    maistas = "Maistas"
    transportas = "Transportas"
    butas = "Butas"
    kita = "Kita"

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, tipas):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.tipas = tipas

class Biudzetas:
    def __init__(self):
        self.pajamu_irasai = []
        self.islaidu_irasai = []
    def ivesti_pajamas(self, suma, siuntejas, papildoma_informacija, tipas):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija, tipas)
        self.pajamu_irasai.append(pajamu_irasas)
        print("Pajamos sekmingai ivestos.")
    def ivesti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, tipas):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, tipas)
        self.islaidu_irasai.append(islaidu_irasas)
        print("Islaidos sekmingai ivestos.")
    def gauti_balansa(self):
        pajamu_suma = sum(irasas.suma for irasas in self.pajamu_irasai)
        islaidu_suma = sum(irasas.suma for irasas in self.islaidu_irasai)
        balansas = pajamu_suma - islaidu_suma
        return balansas
    def gauti_ataskaita(self):
        print("Pajamu irasai:")
        for irasas in self.pajamu_irasai:
            print("Suma:", irasas.suma)
            print("Siuntejas:", irasas.siuntejas)
            print("Papildoma informacija:", irasas.papildoma_informacija)
            print("Pajamu tipas:", irasas.tipas.value)
            print("-----------------")
        print("Islaidu irasai:")
        for irasas in self.islaidu_irasai:
            print("Suma:", irasas.suma)
            print("Atsiskaitymo budas:", irasas.atsiskaitymo_budas)
            print("Isigyta preke/paslauga:", irasas.isigyta_preke_paslauga)
            print("Islaidu tipas:", irasas.tipas.value)
            print("-----------------")

class Meniu(Enum):
    pavadinimas = "MINIBIUDZETO PROGRAMA"
    pirmas = "1.Ivesti pajamas"
    antras = "2.Ivesti islaidas"
    trecias = "3.Parodyti balansa"
    ketvirtas = "4.Parodyti biudzeto ataskaita"
    penktas = "5.Iseiti"

pavadinimas = Meniu.pavadinimas.value
pirmas = Meniu.pirmas.value
antras = Meniu.antras.value
trecias = Meniu.trecias.value
ketvirtas = Meniu.ketvirtas.value
penktas = Meniu.penktas.value

def rodyti_menu():
    print(pavadinimas)
    print(pirmas)
    print(antras)
    print(trecias)
    print(ketvirtas)
    print(penktas)

biudzetas = Biudzetas()
while True:
    rodyti_menu()
    pasirinkimas = input("Pasirinkite veiksma (iveskite skaiciu nuo 1 iki 5): ")
    if pasirinkimas == "1":
        suma = float(input("Iveskite pajamu suma: "))
        siuntejas = input("Iveskite siuntėja: ")
        papildoma_informacija = input("Iveskite papildoma informacija: ")
        tipas = PajamuTipas[input("Iveskite viena is siu pajamu tipu (alga, pasalpa, kita): ")]
        biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija, tipas)
    elif pasirinkimas == "2":
        suma = float(input("Iveskite islaidu suma: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        isigyta_preke_paslauga = input("Iveskite isigyta preke/paslauga: ")
        tipas = IslaiduTipas[input("Iveskite viena is siu islaidu tipu (maistas, transportas, butas, kita): ")]
        biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, tipas)
    elif pasirinkimas == "3":
        balansas = biudzetas.gauti_balansa()
        print("Balansas: ", balansas)
    elif pasirinkimas == "4":
        biudzetas.gauti_ataskaita()
    elif pasirinkimas == "5":
        print("Programa baige darba.")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar karta.")