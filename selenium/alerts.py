import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("hi,this is anusha. accepting the alert")
alertwindow.accept()

# alertwindow.send_keys("hi,this is anusha. declining the alert")
# alertwindow.dismiss()
time.sleep(5)
driver.quit()
