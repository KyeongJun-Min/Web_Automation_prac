'''
저번 영상에서 설명드렸던 코스타그램 스크래핑을 시작해 봅시다.

이번 과제에서는 아래 동작들에 대한 Selenium 코드를 짜 주세요:

웹 드라이버 생성 후 코스타그램 (https://workey.codeit.kr/costagram/index) 접속
코스타그램 로그인
웹 페이지 끝까지 스크롤
각 썸네일(포스팅)을 클릭하고, 창이 뜨면 닫기 버튼 누르기
웹 드라이버 종료
웹사이트 로딩을 생각해서, wait도 추가해 주는 것 잊지 마세요!
'''

import time

from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
url = "https://workey.codeit.kr/costagram/index"
driver.implicitly_wait(3)

wb = Workbook(write_only=True)
ws = wb.create_sheet("코스타그램 data")

driver.get(url)

driver.find_element_by_xpath("//a[@class='top-nav__login-link']").click()
driver.find_element_by_xpath("//input[@class='login-container__login-input']").send_keys("codeit")
driver.find_element_by_css_selector("input.login-container__password-input").send_keys("datascience")
driver.find_element_by_xpath("//input[@class='login-container__login-button']").click()

last_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

while(True):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(0.5)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if(new_height == last_height):
        break
    last_height = new_height

thumb_nails = driver.find_elements_by_xpath("//div[@class='post-list__post post']")

for thumb_nail in thumb_nails:
    thumb_nail.click()
    time.sleep(0.3)
    driver.find_element_by_css_selector("button.close-btn").click()

driver.quit()

