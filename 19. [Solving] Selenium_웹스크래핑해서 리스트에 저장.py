import time
from selenium import webdriver

# HTML 코드 받아오기
driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/orangebottle/index")

branch_infos = []

# 모든 지점에 대한 태그 가져오기
branch_tags = driver.find_elements_by_css_selector("div.branch")

for branch in branch_tags:
    branch_name = branch.find_element_by_css_selector("p.city").text
    address = branch.find_element_by_xpath("//p[@class='address']").text
    phone_number = branch.find_element_by_css_selector("span.phoneNum").text
    branch_infos.append([branch_name, address, phone_number])

print(branch_infos)

driver.quit()
