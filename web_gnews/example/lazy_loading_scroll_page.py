#!/usr/bin/python3

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
driver.maximize_window()
ele = driver.find_element(By.ID, 'kw')
ele.send_keys("京东商城", Keys.ENTER)
loc = (By.XPATH, '//a[contains(text(),"正品低价、品质保障")]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
win = driver.window_handles
driver.switch_to.window(win[-1])
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 京东页面的内容 - 滚动多少，加载多少。所要操作的内容，并不知道大概要滚动多少。
lo = (By.XPATH, '//span[text()="居家优品"]')
# 获取当前的窗口大小。整个窗口的高和宽。
win_size = driver.get_window_size()
# 窗口有window.outerHeight(包含工具栏和滚动条),window.innerHeight(不包含工具栏和滚动条,仅内容可视区域)
# 获取当前窗口的内容可视区域
inner_height = driver.execute_script("var a = window.innerHeight;return a;")
print("当前窗口的内容可视区域-高度：",inner_height)
# 获取当前整个html页面的body高度。
body_height = driver.execute_script("var a = document.body.scrollHeight;return a;")
print("当前整个html页面的body-高度:",body_height)

scrolled_height = 0
new_body_height = body_height
old_body_height = 0
break_flag = False
while new_body_height != old_body_height:
    distance = int((new_body_height -scrolled_height)/ (inner_height * 0.8)) + 1
    for i in range(distance):
        # 滚动距离为 窗口内容可视区域的百分之50.可灵活配置哦！
        driver.execute_script("var a = window.innerHeight;window.scrollBy(0,a*0.5);")
        # 滚动一次，页面内容会更新一部分。在滚动之后，查找当前页面是否包含了它。如果没有，继续滚动。如果有，退出。
        try:
            WebDriverWait(driver, 7).until(EC.visibility_of_element_located(lo))
        except:
            pass
        else:
            print("找到啦！！！")
            driver.find_element(*lo).click()
            break_flag = True # 终止for循环
            break
    if break_flag is True:  # 终止While循环
        break
        # time.sleep(3)
    # 更新滚动
    old_body_height = new_body_height
    scrolled_height = new_body_height
    new_body_height = driver.execute_script("var a = document.body.scrollHeight;return a;")
    print("老 - 当前整个html页面的body-高度:", old_body_height)
    print("新 - 当前整个html页面的body-高度:", new_body_height)


time.sleep(10)
driver.quit()