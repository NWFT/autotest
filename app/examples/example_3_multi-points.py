
"""
MultiAction

1、add  将单点触控添加
2、perform   执行

"""

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

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
    "appPackage":"com.baidu.BaiduMap",
    "appActivity":"com.baidu.baidumaps.WelcomeScreen",
    "noReset":True

}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

sleep(12)

# 设备大小
size = driver.get_window_size()

# 实例化多点触控类
ma = MultiAction(driver)

# 第一个touchAction  从正中心向左下角滑动
ta1 = TouchAction(driver)
ta1.press(x=size["width"]*0.5, y=size["height"]*0.5).wait(200).\
                    move_to(x=size["width"]*0.1, y=size["height"]*0.9).wait(200).release()

# 第二个touchAction  从正中心向右上角滑动
ta2 = TouchAction(driver)
ta2.press(x=size["width"]*0.5, y=size["height"]*0.5).wait(200).\
                    move_to(x=size["width"]*0.9, y=size["height"]*0.1).wait(200).release()

# 加入到多点触控当中
ma.add(ta1,ta2)

# 执行
ma.perform()

sleep(7)
driver.quit()






