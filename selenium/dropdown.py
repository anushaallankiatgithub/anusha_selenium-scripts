import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

dropdown= Select(driver.find_element(By.XPATH,"//*[@id='input-country']"))

options=driver.find_elements(By.TAG_NAME,"option")
print(len(options))
for option in options:
    print(option.get_attribute("value"),"   ",option.text )

dropdown.select_by_visible_text('India')
time.sleep(5)
driver.close()