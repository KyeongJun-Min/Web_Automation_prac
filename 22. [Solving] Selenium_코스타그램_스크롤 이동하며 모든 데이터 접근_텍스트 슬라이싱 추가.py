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
    split_image_url = driver.find_element_by_xpath("//div[@class='post-container__image']").get_attribute('style').split(" ")[1]
    image_url = split_image_url[5:-3]

    print(image_url)
    driver.find_element_by_css_selector("button.close-btn").click()

driver.quit()

