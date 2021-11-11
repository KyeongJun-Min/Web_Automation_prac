from selenium import webdriver
driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")

driver.get("https://codeit.kr")

driver.quit()
