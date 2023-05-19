from time import time  # importuojame time modulį



def laika_skaicis(funkc):
    def wrapper(*args, **kwargs):
        start_time = time()  # fiksuojame starto laiką
        funkc(*args, **kwargs)
        end_time = time()
        vykdymo_laikas = end_time - start_time
        print("Funkcijos vykdymo laikas:", vykdymo_laikas, "sekundės")

    return wrapper


@laika_skaicis
def spausdintuvas(tekstas):
    print(tekstas*100)

# Testuojame funkciją
spausdintuvas("asdfasdfjgdsflhgsadfsdf"
              "assdasdasdasdasdasdsad"
              "sdsasdasdsad")

