"""
鼠标操作：ActionChains
2部分：操作 + 执行(perform())

操作：
move_to_element
click
double_click
context_click
click_and_hold
release
drag_and_drop
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

sleep(2)
loc = (By.XPATH,'//*[@id="s-usersetting-top"]')

# 1、先找到鼠标要操作的元素对象
ele = driver.find_element(*loc)

# 悬浮在这个元素上
# 2、ActionChains实例化
ta = ActionChains(driver)

# 3、调用鼠标操作
ta.move_to_element(ele).click(ele)

# 4、调用perfrom()执行鼠标操作
ta.perform()

# 等待下拉列表的元素可见，操作
loc = (By.XPATH,'//a[text()="高级搜索"]')
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


sleep(10)
driver.quit()
