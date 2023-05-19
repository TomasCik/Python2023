import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y %m %d")

    def darbo_dienu_skaicius(self):

        dabar = datetime.datetime.now()
        viso_darb_dienu = dabar - self.dirba_nuo

        return viso_darb_dienu.days

    def atlyginimas(self):
        darbo_dienos = self.darbo_dienu_skaicius()
        atlyginimas  = darbo_dienos * 8 * self.valandos_ikainis
        print("Darbo dienų: ", darbo_dienos)
        print("Atlyginimo suma: ", atlyginimas)

class NormalusDarbuotojas(Darbuotojas):


    def darbo_dienu_skaicius(self):

        dabar = datetime.datetime.now()
        viso_darb_dienu = dabar - self.dirba_nuo

        return viso_darb_dienu.days// 7 * 5


    # class NormalusDarbuotojas(Darbuotojas):
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         super().__init__(vardas, valandos_ikainis, dirba_nuo)
#         self.savaitgaliai = 0
#
#     def tik_darbo_dienos(self):
#         darbo_dienos = super().darbo_dienu_skaicius()
#         savaitgaliai = self.savaitgaliai
#
#         # Skaičiuojame darbo dienas per savaitę
#         darbo_dienos_per_savaitę = darbo_dienos // 7 * 5 + darbo_dienos % 7
#
#         # Atimame savaitgalius
#         darbo_dienos_per_savaitę -= savaitgaliai * 2
#
#         return darbo_dienos_per_savaitę

    # def atlyginimas(self):
    #     darbo_dienos_per_savaite = self.tik_darbo_dienos()
    #     atlyginimas = darbo_dienos_per_savaite * 8 * self.valandos_ikainis
    #     print("Darbo dienų: ", darbo_dienos_per_savaite)
    #     print("Atlyginimo suma: ", atlyginimas)


darbuotojas1 = Darbuotojas("Petras", 10, "2021 10 15")
darbuotojas1.darbo_dienu_skaicius()
darbuotojas1.atlyginimas()
darbuotojas2 = NormalusDarbuotojas("Antanas", 12, "2021 10 15")
darbuotojas2.atlyginimas()








