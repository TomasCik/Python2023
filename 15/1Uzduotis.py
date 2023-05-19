# import re
#
# def datos_keitimas(text):
#     pattern = re.compile(r'(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})')
#     result = pattern.findall(text)
#
#     for data in result:
#         diena = data[0]
#         menuo = data[1]
#         metai = data[2]
#         nauja_data = f"{metai} {menuo} {diena}"
#         print(f"Data nauju formatu: {nauja_data}")
#
# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," \
#        " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
#        " Ut enim ad minim veniam, 22.12.1687 quis nostrud exercitation ullamco laboris nisi " \
#        "ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in " \
#        "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 01.02.1870 sint occaecat " \
#        "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#
#
# datos_keitimas(text)



import re

re.MULTILINE
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," \
       " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
       " Ut enim ad minim veniam, 22.12.1687 quis nostrud exercitation ullamco laboris nisi " \
       "ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in " \
       "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 01.02.1870 sint occaecat " \
       "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

pattern = re.compile(r"(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})")
result = pattern.sub(r"\3 \2 \1", text)
print(result)






