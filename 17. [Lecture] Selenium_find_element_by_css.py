from selenium import webdriver

driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
driver.implicitly_wait(3) # 웹 사이트 로딩까지 기다릴 시간

driver.get("https://workey.codeit.kr/costagram/index")

driver.find_element_by_css_selector(".top-nav__login-link").click()

driver.find_element_by_css_selector(".login-container__login-input").send_keys('codeit')
driver.find_element_by_css_selector(".login-container__password-input").send_keys('datascience')

driver.find_element_by_css_selector(".login-container__login-button").click()
