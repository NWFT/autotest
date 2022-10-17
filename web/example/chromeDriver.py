import time

from selenium import webdriver

driver = webdriver.Chrome()
# webdriver.Remote()
print(driver)
driver.get("https://www.google.com")
time.sleep(3)
driver.quit()


