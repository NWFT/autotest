"""
A) setup steps,
Python-Appium <==> Appium  <==> Appium-proxy in device

1. download
https://appium.io/
# this tools for session test, element location
https://github.com/appium/appium-inspector/releases

2. download Android studio (adb devices for virtual device/real device)

3. desired_caps
# aapt dump badging apk-name
# package: name='com..'
# launchable-activity: name='com.lemon.lemonban.activity.WelcomeActivity'  label='' icon=''

//设置 包名：com.android.settings
//浏览器 包名：com.android.browser
//计算器 包名：com.android.calculator2

"""
"""
B) message work flow 
Test Scripts <=JsonWireProtocol/W3c WebDriver=> Appium <==> WebDriverAgent <=LibraryCalls=> XCUITest <==> iOS App
                                                        <==> AndroidDriver <==> UIautomator <==> Android App
1)JsonWireProtocol/W3c Webdriver
https://www.selenium.dev/documentation/legacy/json_wire_protocol/
2) Appium GUI Logs
a) 发送http请示到appium server
    (--> POST /wd/hub/session)
    
b) appium server收到之后，创建session
c) 获取已连接的设备，并找对应的安卓版本号
    (No app sent in, not parsing package/activity)
    
d) 获取io.appium.settings的状态，获取它的版本，以确保是当前匹配最新的版本。settings_apk-debug.apk
   获取io.appium.uiautomator2.server的状态，获取它的版本，以确保是当前匹配最新的版本。
       io.appium.uiautomator2.server.-debug-androidTest
e) 启动手机上的uiautomator.server的服务，然后设置将本地appium server收到的指令都从本地8200端口，转发到设备的6790端口
    ([WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body)
    
f) 跟手机创建会话。
  ([WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}})
  ([WD Proxy] Matched '/session' to command name 'createSession')
  ([WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body)
  ([WD Proxy] Got response with status 200: {"sessionId")
g) 打开app
    ([AndroidDriver] Screen already unlocked, doing nothing)
    ([UiAutomator2] Starting 'com.android.)
    ([W3C (f88267c9)] Responding to client with driver.createSession())
    (<-- POST /wd/hub/session 200)

h) 如果60s内，appium server没有收到客户端的http请求，主动关闭与客户端的会话，与手机端的会话。然后关闭app
    ([BaseDriver] Shutting down because we waited 60 seconds for a command)
    
"""

"""
adb: Android Debug Bridge. PC <==> MPhone
    client/server:5037/deamon
    (adb start-server/kill-server; adb devices; adb pull/push PC-dir MP-dir ; adb shell;)
    (adb push d:\test.log /sdcard/)
    (adb -P 5037 -s emulator-5554 shell)
    (adb uninstall com.xyz.abc / adb install xxx.apk)
    adb shell dumpsys activity | find "mResumedActivity"
    adb shell dumpsys activity activities | findstr mResumedActivity
     
monkey: 
"""


from appium import webdriver


desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.0",   # check device on info
    "deviceName": "emulator-5554",  # any
    "appPackage": "com.android.calculator2",    # apk info
    "appActivity": "com.android.calculator2.Calculator",    # startup page
    "noReset": True
}

webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

"""
elements locators
active/html

3rd tool: elements' feature / 坐标/图片
http://testingpai.com/article/1595507262082

id
class_name
accessibility_id

"""