import requests
from bs4 import BeautifulSoup
from collections import Counter

# URLを指定
url = 'https://example.com'  # 対象のページURLを指定してください

# ページの内容を取得
response = requests.get(url)
html_content = response.content

# BeautifulSoupでHTMLをパース
soup = BeautifulSoup(html_content, 'html.parser')

# aタグのhref属性からURLを抽出
urls = [a['href'] for a in soup.find_all('a', href=True)]

# URLの頻度をカウント
url_counter = Counter(urls)

# 頻出するURLを出力
for url, count in url_counter.most_common():
    print(f'{url}: {count}回')
  
