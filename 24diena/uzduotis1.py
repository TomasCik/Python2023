# import requests
#
#
# def valiutos_tikrinimas(valiuta):
#     response = requests.get('https://api.frankfurter.app/currencies')
#     data = response.json()
#     palaikomos_valiutos = data.keys()
#     # print(palaikomos_valiutos)
#
#     if valiuta in palaikomos_valiutos:
#         return True
#     else:
#         return False
#
# palaikomos_valiutos = valiutos_tikrinimas('EUR')
# def valiut_kursai(val1, val2):
#     if not valiutos_tikrinimas(val1) or not valiutos_tikrinimas(val2):
#         print("Klaida: Neleistina valiuta!")
#         print("Galimi formatai:", ", ".join(palaikomos_valiutos))
#
#         print(palaikomos_valiutos)
#         return
#
#     response = requests.get(f'https://api.frankfurter.app/latest?from={val1}&to={val2}')
#     data = response.json()
#     print(data)
#
# valiut_kursai('EUR', 'asd')
#
#
import requests


def valiutos_tikrinimas(valiuta):
    response = requests.get('https://api.frankfurter.app/currencies')
    data = response.json()
    palaikomos_valiutos = list(data.keys())

    if valiuta in palaikomos_valiutos:
        return palaikomos_valiutos
    else:
        return []


def valiut_kursai(val1, val2):
    val1 = val1.upper()
    val2 = val2.upper()
    palaikomos_valiutos = valiutos_tikrinimas('EUR')

    if not valiutos_tikrinimas(val1) or not valiutos_tikrinimas(val2):
        print("Klaida: Neleistina valiuta!")
        print("Galimi formatai:", ", ".join(palaikomos_valiutos))
        return

    response = requests.get(f'https://api.frankfurter.app/latest?from={val1}&to={val2}')
    data = response.json()
    rate = data['rates'].get(val2)
    if val1 = val2
        print('1')

    result = f"1 {val1} = {rate} {val2}"
    print(result)



valiut_kursai('CZK', 'USD')
