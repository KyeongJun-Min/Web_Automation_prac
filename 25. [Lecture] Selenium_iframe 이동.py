from selenium import webdriver

driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
url = "https://blog.naver.com/codeitofficial"

driver.get(url)

driver.switch_to.frame("mainFrame")
target = driver.find_element_by_css_selector('#blogTitleText') # 웹 요소를 찾을 수 없다는 오류
print(target)

driver.switch_to.parent_frame()
target = driver.find_element_by_css_selector('#blogTitleText') # 웹 요소를 찾을 수 없다는 오류
print(target)
