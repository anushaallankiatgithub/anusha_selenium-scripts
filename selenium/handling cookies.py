from selenium import webdriver

from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com/")
driver.maximize_window()

cookies=driver.get_cookies()
print(len(cookies))

# for cookie in cookies:
    # print (cookie)
    # print(cookie.get('domain'),':',cookie.get('value'))

driver.add_cookie({'name':'newlyaddedcookie','value':'12345'})
cookies=driver.get_cookies()
print('new length of cookies',len(cookies))


driver.delete_cookie('newlyaddedcookie')
cookies=driver.get_cookies()
print(len(cookies))
driver.quit()