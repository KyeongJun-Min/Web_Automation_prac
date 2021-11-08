import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###
response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

popular_searches = []

for tag in soup.select("ul.rank__order li"):
    popular_searches.append(list(tag.stripped_strings)[2])

# 출력 코드
print(popular_searches)
