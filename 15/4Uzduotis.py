import re

def cenzura(tekstas, *keiksmai):
    for keiksmas in keiksmai:
        pattern = re.compile(r'\b' + keiksmas + r'\b')
        tekstas = pattern.sub(keiksmas[0] + '*' * (len(keiksmas) - 2) + keiksmas[-1], tekstas)
    print(tekstas)

tekstas = "baisūs žodžiai, tokie kaip kvaraba, žaltys.."
cenzura(tekstas, "kvaraba", "žaltys")



