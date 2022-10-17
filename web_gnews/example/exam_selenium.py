import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("http://alex-info.ca")

# find a element and click
# ele = driver.find_element(By.LINK_TEXT, "http://www.alex-info.ca:8000")
# eles = driver.find_elements(By.PARTIAL_LINK_TEXT, "http")

loc = (By.XPATH, "//a[contains(@href, 8000)]")
ele = driver.find_element(*loc)

ele.click()
# print(ele.tag_name)

wait = WebDriverWait(driver, 10)

loc = (By.XPATH, '//a[contains(@href, "login")]')
wait.until(EC.visibility_of_element_located(loc))

driver.find_element(*loc).click()

time.sleep(3)
# close current window
driver.close()
# stop webdriver service
driver.quit()
