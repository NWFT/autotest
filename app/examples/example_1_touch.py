
"""
TouchAction: 操作 + 执行(perform)
操作 - 有3个参数：元素对象、x、y (二选一)
tap：点击
press：按住
long_press：长按住
wait: 等待
move_to:移动
release：释放


执行：perform


设备的大小：driver.get_window_size()
"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.0",   # check device on info
    "deviceName": "emulator-5554",  # any
    "appPackage": "com.android.calculator2",    # apk info
    "appActivity": "com.android.calculator2.Calculator",    # startup page
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 切换到题 库
loc = (MobileBy.ID,'com.lemon.lemonban:id/navigation_tiku')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# 等待题 库页面元素加载
loc = (MobileBy.ID,'com.lemon.lemonban:id/fragment_category_type')
WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located(loc))
sleep(0.5)


# 滑屏操作
# 设备大小
size = driver.get_window_size()
# size
x = size["width"] * 0.5
y_start = size["height"] * 0.9
y_end = size["height"] * 0.1

driver.swipe(x,y_start,x,y_end,200)

sleep(7)
driver.quit()

# 点击
# 滑动：上下滑动/左右
# 触屏操作  多点触控
# h5混合应用 - 微信小程序/公众号
# toast