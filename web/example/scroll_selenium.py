"""
让元素滚动到可见区域后，再操作。
1、大部分的网页自己会滚

2、元素本身：ele.location_once_scrolled_into_view

3、js：element.scrollIntoView()
    js_code = 'arguments[0].scrollIntoView()'
    driver.execute_script(js_code,ele)


"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
# driver.get("http://www.baidu.com")
driver.get("https://www.google.com")

driver.find_element(By.NAME,"q").send_keys("selenium",Keys.ENTER)

loc = (By.XPATH,'//a[text()="6"]')
# loc = (By.XPATH,'//a//span[text()="10"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
ele.location_once_scrolled_into_view
# js_code = 'arguments[0].scrollIntoView()'
# driver.execute_script(js_code,ele)

# js_code = 'window.scrollTo(0,500)'

sleep(3)
driver.quit()
