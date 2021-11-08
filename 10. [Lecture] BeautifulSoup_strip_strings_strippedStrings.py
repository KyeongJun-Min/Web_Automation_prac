import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

popular_artist = []

for tag in soup.select('ul.popular__order li'):
    popular_artist.append(tag.get_text().strip())  # strip() 함수는 문자열에서 불필요한 공백들을 제거해줌
    print(list(tag.strings)) # 각 태그 안에 있는 요소들이 리스트에 따로따로 분리되어서 노출  태그변수.strings
    print(list(tag.stripped_strings))  # stripped_strings : strings 내용에서 strip을 적용해서 불필요한 요소 제거
    print(list(tag.stripped_strings)[1])

print(popular_artist)
