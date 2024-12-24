# 畫文字雲
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re
import os
import requests

def generate_cloud(text):
    # Calculate the frequency of each word
    cleaned_text = re.sub(r"[^\u4e00-\u9fffA-Za-z]", " ", text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    
    # Find the top 10 most common words and their frequencies
    most_common_words = word_counts.most_common(10)
    total_words = sum(word_counts.values())
    
    string = "出現率最高的詞 前十名："
    for word, count in most_common_words:
        frequency = count / total_words
        string += f"\nThe word '{word}' has a frequency of {frequency:.2%}"
    
    # Generate word cloud
    wordcloud = WordCloud(font_path='msjh.ttc',  # 微軟正黑體，確保支援中文
    width=800, height=400,
    background_color='white',
    collocations=False).generate_from_frequencies(word_counts)
    
    # Ensure the directory exists
    output_dir = 'static'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the word cloud to a file
    image_path = os.path.join(output_dir, 'wordcloud.png').replace('\\', '/')
    wordcloud.to_file(image_path)
    
    # Get the ngrok URL


    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        data = response.json()
        public_url = data['tunnels'][0]['public_url']
    except Exception as e:
        return f"Error: {e}"

    

    # Display the word cloud
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis('off')
    # plt.show()
    
    # Return the file path
    return (public_url+'/'+image_path), string