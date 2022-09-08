import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker")
driver.maximize_window()
driver.switch_to.frame(0)

exp_month = "November"
exp_year="2032"
exp_day="3"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    month = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text
    year = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text
    if (month==exp_month) and (year==exp_year):
      break
    else:
      driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()

days_ele = driver.find_elements(By.XPATH, "//a[@class='ui-state-default']")

for day in days_ele:
    if day.text==exp_day:
        day.click()
        break
