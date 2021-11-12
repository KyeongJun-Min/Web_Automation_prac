import time
from selenium import webdriver

# HTML 코드 받아오기
driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/music")

time.sleep(3)
driver.execute_script("window.scrollTo(0, 200);")

scroll_height = driver.execute_script("return document.body.scrollHeight")
print(scroll_height)

# 현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤 이동
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(0.5)

    #새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if(new_height == last_height):
        break
    last_height = new_height




