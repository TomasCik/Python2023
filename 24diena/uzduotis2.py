import requests



def currency_pair_analysis(valiuta1='USD', valiuta2='EUR', nuo='2022-01-01', iki='2022-12-31'):
    url = f"https://api.frankfurter.app/{nuo}..{iki}?from={valiuta1}"
    respons = requests.get(url)
    duomenys = respons.json()["rates"]
    dic = {}
    for datos in duomenys:
        for valiuta in duomenys[datos]:
            if valiuta2 == valiuta:
                santykis = duomenys[datos][valiuta]
                dic.update({datos: santykis})
    min_verte = min(dic.values())
    min_data = min(dic, key=dic.get)
    max_verte = max(dic.values())
    max_data = max(dic, key=dic.get)
    print(f"#Valiutų poroje {valiuta1}-{valiuta2}, periode nuo {nuo} iki {iki}:\n"
          f"#Žemiausias kursas buvo {min_data} - {min_verte}\n"
          f"#Aukščiausias kursas buvo {max_data} - {max_verte}")


currency_pair_analysis()








