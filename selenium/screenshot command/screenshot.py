from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
driver.get("https://www.gmail.com/")
driver.maximize_window()
location=os.getcwd()

driver.get_screenshot_as_file(location+"/abc1.png")
print(location)



driver.quit()