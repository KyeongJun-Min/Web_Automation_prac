import requests

# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

rating_paages = []
for i in range(0, 4+1):
    url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
    response = requests.get(url)
    rating_page = response.text
    rating_paages.append(rating_page)

print(len(rating_paages))
print(rating_paages[0])
