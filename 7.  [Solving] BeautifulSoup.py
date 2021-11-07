import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###

response = requests.get("https://workey.codeit.kr/orangebottle/index") # url을 요청.
page = response.text # url에서 노출되는 페이지의 html 코드를 저장

soup = BeautifulSoup(page, 'html.parser') # 저장된 html 코드를 내가 다룰 수 있게 parser로 정리
numbers = soup.select('span.phoneNum') # html 코드에서 span 태그 중 class가 phoneNum인 엘리먼츠들을 선택

phone_numbers = []

for number in numbers:
    phone_numbers.append(number.get_text()) # 빈 리스트에 필터링된 요소들의 텍스트를 저장


# 출력 코드
print(phone_numbers)
