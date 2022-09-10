def chrome_setup_headless():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=serv_obj,options=ops)
    return driver


driver=chrome_setup_headless()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
driver.switch_to.new_window('window')
driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)

print("----printing window handles-----")

print(driver.window_handles[1])
print(driver.window_handles[-1])
print(driver.window_handles[0])

print("----switching  window handles-----")
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
driver.quit()
