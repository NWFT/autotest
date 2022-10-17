"""
android5
automationName: UiAutomator2

xpath定位表达式：
//*[contains(@text,"手机号码或")]

等待toast元素存在
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
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True,
    "chromedriverExecutableDir":"D:\ChromeDrivers\chrome67-69"
}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


# 点击我的柠檬元素
loc = (MobileBy.ID,'com.lemon.lemonban:id/navigation_my')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击头像
loc = (MobileBy.ID,'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击登陆按钮
loc = (MobileBy.ID,'com.lemon.lemonban:id/btn_login')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# toast弹出来
# toast的定位表达式
loc = (MobileBy.XPATH,'//*[contains(@text,"手机号码或")]')
try:
    WebDriverWait(driver,30,0.01).until(EC.presence_of_element_located(loc))
    print(driver.find_element(*loc).text)
except:
    print("我没有找到toast提示框！！")
