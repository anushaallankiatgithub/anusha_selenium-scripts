# import webdriver from selenium
# webdriver is a python module available in selenium package


from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# driver is an object of chrome class. chrome class is predefined in webdriver module.
# chrome class takes driver executable path as a parameter.

driver.get("https://www.google.com/")
driver.maximize_window()
# launching url
driver.find_element(By.NAME,"q").send_keys("Awesome Anvitha")
# clsnms=driver.find_elements(By.CLASS_NAME,"gNO89b")
# print(len(clsnms))
# Search button using xpath locator
driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']/center/input[1]").click()
# full xpath/absolute xpath written manually for search button- /html/body/div/div[3]/form/div/div/div[3]/center/input[1]
# relative/xpath/partial xpath written manually for search button- //div[@class='FPdoLc lJ9FBc']/center/input[1]
# search button using css selector
# driver.find_element(By.CSS_SELECTOR,"input.gNO89b[data-ved=0ahUKEwiX9ZDfhvb5AhUhIjQIHTi1AlwQ4dUDCA0]").click()
# click on Awesome Anvitha - YouTube link
# driver.find_element(By.PARTIAL_LINK_TEXT,"Awesome Anvitha - YouTube").click()
# #
# driver.find_element(By.PARTIAL_LINK_TEXT,"La Grande Roue de Montréal - view from inside the ferris wheel").click()
#
# driver.close()