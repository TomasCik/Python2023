
def parametru_ribojimas(funkc):
    def wrapper(*args, **kwargs):
        if len(args) > 2 or len(kwargs) >2:
            print("Leistingas argumentus kaičius yra 2!")
            return
        elif len(args) < 2 or len(kwargs) <2:
            print("per mažai argumentų!")
            return
        else:
            return funkc(*args, **kwargs)
    return wrapper


@parametru_ribojimas
def suma(a, b):
    print(a+b)

suma(1, )






