import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com")
driver.maximize_window()

alllinks= driver.find_elements(By.TAG_NAME, "a")

print(len(alllinks))
count=0
for link in alllinks:
    # print(link.get_attribute('href'))
     url=link.get_attribute('href')
     try:
        res=requests.head(url)
     except:
        None

     if res.status_code>=400:
        print(url,"this is a broken link")
        count+=1

for link in alllinks:
    # print(link.get_attribute('href'))
     url=link.get_attribute('href')
     try:
        res=requests.head(url)
     except:
        None

     if res.status_code<400:
        print(url,"this is valid link")
print(count)

driver.quit()