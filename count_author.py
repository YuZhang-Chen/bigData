import json

# 讀取 data.json 文件
def count_author():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    dic_author = {}

    for i in data:
        author = i['author'].strip().split(',')
        for j in author:
            if j not in dic_author:
                dic_author[j] = 1
            else:
                dic_author[j] += 1

    sorted_authors = sorted(dic_author.items(), key=lambda item: item[1], reverse=True)

    top_authors = []
    current_count = None

    for author, count in sorted_authors:
        if len(top_authors) >= 10 and count != current_count:
            break
        top_authors.append((author, count))
        current_count = count
    
    for author, count in top_authors:
        print(f"{author}: {count}本")
