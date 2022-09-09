from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

box1_ele=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
box2_ele=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

box1_ele.send_keys("welcome to selenium")

act=ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.key_down(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

driver.quit()
