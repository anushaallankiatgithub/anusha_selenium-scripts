from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# driver is an object of chrome class. chrome class is predefined in webdriver module.
# chrome class takes driver executable path as a parameter.

driver.get("https://www.google.com/")
driver.maximize_window()