import requests
import re
import random

def download_random_cat_images(count):
    base_url = "http://random.cat/view/"
    image_urls = []

    for _ in range(count):
        random_number = random.randint(1, 1500)
        url = f"{base_url}/{random_number}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            image_url = re.findall(r'<img src="(.*?)"', content)
            if image_url:
                image_urls.append(image_url[0])

    for i, url in enumerate(image_urls, start=1):
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"cat_{i}.jpg", 'wb') as file:
                file.write(response.content)
            print(f"Nuotrauka {i} sėkmingai parsisiųsta.")


count = 5
download_random_cat_images(count)
