# 取得每個分類的網址

import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.books.com.tw/web/sys_saletopb/books/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_='mod_b type02_l001-1 clearfix')

    url_dict = {}

    for element in elements:
        li_items = element.find_all('li')
        for li in li_items:
            a_tag = li.find('a')
            if a_tag:
                text = a_tag.get_text()
                href = a_tag.get('href')
                url_dict[text] = href
                
            else:
                print(f"{li.text.strip()}")
    
    with open('url.json', 'w', encoding='utf-8') as f:
        json.dump(url_dict, f, ensure_ascii=False, indent=4)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")