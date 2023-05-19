

def tik_string(tekstas):
    import functools
    def wrapper(*args, **kwargs):
        for text in args:
            if type(text) != str:
                print("Leistinas duomenų tipas yra tik STRING!")
                return

        for text in kwargs.values():
            if type(text) != str:
                print("Leistinas duomenų tipas yra tik STRING!")
        else:
            return tekstas(*args, **kwargs)
    return functools.wraps(tekstas)(wrapper)

@tik_string
def pasisveikinimas(tekstas):
    print("Labas,", tekstas)

pasisveikinimas("Jonas")
pasisveikinimas(564)




















