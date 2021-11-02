import requests

# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

rating_pages = []

for year in range(2010, 2012+1):
    for month in range(1,12+1):
        for week in range(0, 4+1):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, week)
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)
            print(url)

print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드
