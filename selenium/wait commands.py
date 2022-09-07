

#  wait commands
#  Implicit wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://www.google.com")
element=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
element.send_keys("selenium")
element.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()