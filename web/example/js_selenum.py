import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://www.12306.cn/index/")

loc = (By.ID, "train_date")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
set_time = "2022-11-29"

# arguments[0] [1], parameters for js
js_code = 'arguments[0].removeAttribute("readonly");' \
          'arguments[0].value = arguments[1];'

# js, values from outside to js code
driver.execute_script(js_code,ele,set_time)

time.sleep(3)
# close current window
driver.close()
# stop webdriver service
driver.quit()
