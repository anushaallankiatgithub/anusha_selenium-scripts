from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

searchbox= driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
# is_enabled() and is_displayed() should be accessed through web elements
print(searchbox.is_enabled())
print(searchbox.is_displayed())

print(searchbox.is_selected())
# is_selected works for check boxes and radio buttons

driver.quit()
