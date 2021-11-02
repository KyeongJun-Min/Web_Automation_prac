import requests

### 코드를 작성하세요 ###
rating_page = requests.get("https://workey.codeit.kr/ratings/index").text

# 출력 코드
print(rating_page)
