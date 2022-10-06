"""
autoit、pywin32

http://testingpai.com/article/1595507248769

# 1、pywinauto  => pip install pywinauto
# 缺点：只能在windows上使用
# 优点：可以选择多个文件，路径中有中文也能可以

# 2、pyauogui  => pip install pyautogui
# 优点： 跨平台(linux,mac,windows都可以用)
# 缺点：只能选择一个文件，文件路径有中文会出问题

# ------------pywinauto  通过窗口上传文件----------------------
from pywinauto.keyboard import send_keys

输入文件名
# send_keys('C:\课件\images\9.png')
# # 输入回车键
# send_keys('{VK_RETURN}')


------------pyautogui  通过窗口上传文件----------------------
# 输入文件名
pyautogui.write('D:\selenium-screenshot-4.png')
# 输入回车键，注意要按2次
pyautogui.press('enter', 2)
"""


import pyautogui
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto.keyboard import send_keys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.ketangpai.com/User/login.html")
sleep(2)
driver.find_element("xpath", '//input[@name="account"]').send_keys("2501768591@qq.com")
driver.find_element("xpath", '//input[@name="pass"]').send_keys("yuan5311645")
driver.find_element('xpath', '//div[@id="login"]//div[contains(@class,"pt-login")]//a[text()="登录"]').click()

sleep(7)
driver.find_element('xpath', '//a[@title="Python全栈第33期"]').click()
sleep(6)
driver.find_element('xpath', '//div[@id="third-nav"]//a[text()="资料"]').click()

sleep(5)
driver.find_element('xpath', "//div[contains(@class,'add-resource-btn')]").click()
sleep(5)
# 点击 上传本地文件   按钮，弹出windows对话框
ele = driver.find_element('xpath', '//a[contains(@class,"webuploader-container")]')
ActionChains(driver).click(ele).perform()

# 等待windows弹框出现
sleep(4)

# pyautogui的用法
# pyautogui.write('D:\\BaiduNetdiskDownload\\report_.html')
# pyautogui.press('enter', presses=2)

# pywinauto的用法
send_keys('"D:\selenium-screenshot-5.png"')
send_keys('"D:\selenium-screenshot-4.png"')
# 输入回车键
send_keys('{VK_RETURN}')

sleep(10)
driver.quit()

