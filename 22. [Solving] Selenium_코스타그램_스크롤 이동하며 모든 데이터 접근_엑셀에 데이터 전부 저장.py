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

'''
썸네일을 클릭하면 상세 정보가 뜨는데요, 이번 과제에서는 각 포스트의 이미지 주소를 추출한 다음, 출력해 주는 코드를 추가해 주세요.

이미지 주소는 하이라이트된 div 태그의 style 속성 값에 있는 /images/costagram/posts/post0.jpg 부분입니다.

이전 과제의 해답 코드는 템플릿 코드로 작성해 놨습니다.
'''


import time

from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
url = "https://workey.codeit.kr/costagram/index"
driver.implicitly_wait(3)

wb = Workbook(write_only=True)
ws = wb.create_sheet("코스타그램 data")
ws.append(['이미지 주소', '내용', '해시태그', '좋아요 수', '댓글 수'])

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
    split_image_url = driver.find_element_by_xpath("//div[@class='post-container__image']").get_attribute('style').split(" ")[1]
    image_url = split_image_url[5:-3]

    text_content = driver.find_element_by_xpath("//span[@class='content__text']").text
    hash_tag = driver.find_element_by_css_selector("div.content__tag-cover").text
    like_count = driver.find_element_by_xpath("//span[@class='content__like-count']").text
    comment_count = driver.find_element_by_css_selector("span.content__comment-count").text

    ws.append([image_url, text_content, hash_tag, like_count, comment_count])

    driver.find_element_by_css_selector("button.close-btn").click()

wb.save("코스타그램.xlsx")

driver.quit()

