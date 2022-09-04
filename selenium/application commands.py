import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

print(driver.current_url)
print(driver.title)
print(driver.page_source)

time.sleep(2)

driver.close()
