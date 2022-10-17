
"""
知不知道要找的元素，在哪一屏？
   滑一屏找一屏。--- while：break/条件不成立(old==new)
   滑一屏，就进入了新的页面，在新的页面里，去找元素。
   如果找着了，不滑了，break
   如果没找着，继续滑到新的页面。

   这个屏幕是怎么知道它到下一屏了呢??  driver.page_source获取当前页面源码
   old - 历史页面  初始值：None
   new - 当前新页面  初始值：driver.page_source
   如果我执行了滑屏操作：
   old = new
   new = driver.page_source


如果滑到底部，还没有找着，就不再滑动。
    怎么样，知道已经滑到底部了?
    如果 old == new ，已经滑到底部了
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 在andriod 7.1.2 上面打开柠檬班app
desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "huawei",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "noReset": True

}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 切换到题 库
loc = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# 等待题 库页面元素加载
loc = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')
WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located(loc))
sleep(0.5)

# ==================   列表滑动流程   ===============

# 设备大小
size = driver.get_window_size()
# size
x = size["width"] * 0.5
y_start = size["height"] * 0.9
y_end = size["height"] * 0.1

# 要找的元素
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'text("接口测试")')

old = None
new = driver.page_source

while old != new:
    # 找元素 - driver.find_element或者等待，没找着元素或者等待失败，都是会抛异常
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(loc))
    except:
        # 没找着，滑到下一屏，继续循环
        driver.swipe(x, y_start, x, y_end, 200)
        sleep(1)
        # 更新新旧页面
        old = new
        new = driver.page_source
    else:
        # 找着了，break
        driver.find_element(*loc).click()
        break