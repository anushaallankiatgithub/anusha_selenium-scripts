from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox')]")
# checkboxes=driver.find_elements(By.CSS_SELECTOR,"input.form-check-input[type='checkbox']")
checkboxes=driver.find_elements(By.XPATH,"//*[contains(@id,'day')]")
print(len(checkboxes))

# to select all checkboxes
# for cb in checkboxes:
#     cb.click()

# select 1st and 3rd checkboxes

for i in range(len(checkboxes)):
    if (i==0  or i==2):
     checkboxes[i].click()
     print(checkboxes[i].get_attribute('id'))


