from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get('http://www.testautomationpractice.blogspot.com')
driver.maximize_window()

table_element= driver.find_element(By.XPATH, "//table[@name='BookTable']")

# no.of rows
total_rows= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(total_rows)

# no.of columns
total_col= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
print(total_col)

# print  all the booknames by the author named "Mukesh"

for r in range(2,total_rows+1):
        author= driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
        if author=="Mukesh":
            print(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text)

driver.quit()