# 畫文字雲
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

def generate_cloud(text):

    # Calculate the frequency of each word
    cleaned_text = re.sub(r"[^\u4e00-\u9fffA-Za-z]", " ", text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    
    # Find the top 10 most common words and their frequencies
    most_common_words = word_counts.most_common(10)
    total_words = sum(word_counts.values())
    
    print("\n出現率最高的詞 前十名")
    for word, count in most_common_words:
        frequency = count / total_words
        print(f"The word '{word}' has a frequency of {frequency:.2%}")
    # Generate word cloud
    cleaned_text = re.sub(r"[^\u4e00-\u9fffA-Za-z]", " ", text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    wordcloud = WordCloud(font_path='msjh.ttc',  # 微軟正黑體，確保支援中文
                      width=800, height=400,
                      background_color='white',
                      collocations=False).generate_from_frequencies(word_counts)
    
    # Display the word cloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()