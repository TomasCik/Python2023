
def velavimas(laikas):
    import time
    def wrapper(*args, **kwargs):
        time.sleep(5)
        return laikas(*args, **kwargs)

    return wrapper

@velavimas
def pasisveikinimas():
    print("Labas!")

pasisveikinimas()

# nelabai gerai nes laikas koreguojasji dekoratoriuje, o ne funkcijos iššaukime





