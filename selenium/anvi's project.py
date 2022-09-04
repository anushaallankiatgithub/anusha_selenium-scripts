import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()

driver.get("https://www.amazon.com/")

search=driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys("pink backpack")

driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

driver.find_element(By.XPATH,"//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/h2/a").click()
driver.find_element(By.XPATH,"//*[@id='add-to-cart-button']").click()
driver.find_element(By.XPATH,"//*[@id='sw-gtc']/span/a").click()

time.sleep(3)

driver.quit()



