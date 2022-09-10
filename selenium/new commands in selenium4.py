import time

# new tab and new browser - new commands introduced in selenium4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
driver.get("https://www.gmail.com/")
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get("https://www.google.com/")
driver.switch_to.new_window('window')
driver.get("https://www.youtube.com/")

time.sleep(3)

# driver.close()
# closes only youtube.com or current window

driver.quit()
# closes all tabs and windows