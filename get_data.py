# 抓取作者及書籍

import requests
from bs4 import BeautifulSoup
import json
import jieba
from generate_cloud import generate_cloud
from count_author import count_author

def get_data(user_input):
    # Load the JSON data from a file
    with open('url.json', 'r', encoding='utf-8') as file:
        url_dict = json.load(file)

    # Convert the JSON data to a dictionary
    # target = input("請輸入你想搜尋的分類 "+",".join([i for i in url_dict.keys()])+"：")
    target = user_input

    url = url_dict.get(target, 'NOT FOUND')
    if url == 'NOT FOUND':
        print(f'404 {url}')
    else:
        response = requests.get(url)

        # 放分詞
        words_repo = []
        if response.status_code == 200:
            data = []
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('li', class_='item')
            for item in items:
                h4_tag = item.find('h4')
                msg_tag = item.find('ul', class_='msg')
            
                if h4_tag:
                    a_tag = h4_tag.find('a')

                    li_tag = msg_tag.find('li')
                    if li_tag:
                        author_tag = li_tag.find('a')
                        if author_tag:
                            author = author_tag.text.strip()

                    if a_tag:
                        title = a_tag.text.strip()
                        link = a_tag['href']
                
                        # 資料清洗
                        unwanted_words = ["限量", "特價", "暢銷", "新書"]
                        for word in unwanted_words:
                            title = title.replace(word, "")
                        title = title.strip()

                        # Remove any non-alphanumeric characters that are not part of a word

                        data.append({'link':link, 'title':title, "author":author})

                        words = list(jieba.cut(title))
                        words_repo.extend(words)

                        # Print the cleaned title and author
            with open('data.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
            
            words_repo = ' '.join(i for i in words_repo)
            
            author_rank = count_author(target)

            image_path, keyword = generate_cloud(words_repo)

            return image_path, keyword, words_repo


        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
