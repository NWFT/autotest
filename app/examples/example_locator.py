# https://appium.io
"""
id/text
class_name (multi)
description

checkable/checked
clickable
enabled


android_uiautomator  (UiAutomator2)
xpath


坐标

UiAutomator - UiSelector类完成的  java语言-字符串必须是双引号
#  new UiSelector().resourceId("")  # appium 1.15之前
#  resourceId("")   # appium 1.15之后

# 多属性组合
resourceId("").text("")
"""


from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.0",   # check device on info
    "deviceName": "emulator-5554",  # any
    "appPackage": "com.android.calculator2",    # apk info
    "appActivity": "com.android.calculator2.Calculator",    # startup page
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# digit_2 locator (id/xpath/class_name/text/accessibility_id)
# https://appium.io
loc_2 = (AppiumBy.ID, "com.android.calculator2:id/digit_2")
loc_3 = (AppiumBy.ID, "com.android.calculator2:id/digit_3")
loc_plus = (AppiumBy.ACCESSIBILITY_ID, "plus")
loc_equal = (AppiumBy.ACCESSIBILITY_ID, "equals")
loc_result = (AppiumBy.ID, "com.android.calculator2:id/result")

WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc_2))
driver.find_element(*loc_2).click()
driver.find_element(*loc_plus).click()
driver.find_element(*loc_3).click()
driver.find_element(*loc_equal).click()
result = driver.find_element(*loc_result).text

assert result == '5'


from time import sleep

sleep(5)
driver.quit()

