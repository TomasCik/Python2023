# import re
# import requests
#
# def get_server_info(url):
#     response = requests.get(url)
#     content = response.content.decode('utf-8')
#     server_info = re.search(r'Server:\s*(.*?)\r\n', content)
#     if server_info:
#         return server_info.group(1)
#
# # Pavyzdys su vienu URL
# url = "https://www.delfi.lt/"
# server_info = get_server_info(url)
# print(f"URL: {url}\nServeris: {server_info}")




