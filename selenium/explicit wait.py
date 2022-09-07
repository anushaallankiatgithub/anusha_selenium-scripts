#  wait commands
#  Explicit wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
mywait=WebDriverWait(driver,10,ignored_exceptions=[Exception])   # explicit wait declaration
driver.maximize_window()
driver.get("https://www.google.com")
element=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
element.send_keys("selenium")
element.submit()

mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']"))).click() #explicit wait utilization
# element1.click()

driver.quit()