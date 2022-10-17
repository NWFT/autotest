"""

"""
import os
import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from app.Common.basepage import BasePage
from web.Common.my_logger import logger


class AppPage(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # swipe screen, limitation 80%
    def swipe_screen_by_direction(self, direction):
        """

        :param direction:
        :return:
        """
        width, heght = self._get_device_size()
        if direction == 'up':
            start_x = width * 0.5
            start_y = heght * 0.9
            end_x = width * 0.5
            end_y = heght * 0.1
        # elif direction == 'down':
        #     pass
        # elif direction == 'left':
        #     pass
        else:  # right
            start_x = width * 0.1
            start_y = heght * 0.5
            end_x = width * 0.9
            end_y = heght * 0.5

        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, 200)
        except:
            pass


        #
        # # need time to open the new window
        # logger.info("switch window begin.")
        # time.sleep(1)
        # # get all window handlers
        # wins = self.driver.window_handles
        # logger.info(f"all windows handlers: {wins}")
        # # new, switch to the last open window
        # if name == "new":
        #     # switch_to window/frame/
        #     logger.info(f"Change window to: {wins[-1]}")
        #     self.driver.switch_to.window(wins[-1])

    def _get_device_size(self):
        """

        :return:
        """
        try:
            size = self.driver.get_window_size()
        except:
            self.get_page_screenshot()
            raise
        else:
            return size["width"], size["height"]

    # get toast message
    def get_toast_message(self, toast_value, page_operation):
        # get element
        # logger.info("Input values to readonly element.")
        # toast locator example
        loc = ("xpath", '//*[contains(@text, "{}")]'.format(toast_value))
        try:
            self.wait_page_contains_element(loc, page_operation, 10, 0.1)
        except:
            pass

    # h5 pages
    def switch_to_webview(self,webview_name):
        cons = self.driver.contexts
        if webview_name in cons:
            self.driver.switch_to.context(webview_name)
            time.sleep(1)
        else:
            pass  # 提示一下，webview没有获取到。


# if __name__ == '__main__':
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service
    #
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #
    # base = BasePage(driver)
    # driver.get("http://www.alex-info.ca:8000/login/")
    #
    # loc = (By.NAME, "username")
    # # base.wait_element_visible(loc, "Login_Username")
    #
    # # get element
    # # ele = base.get_element(loc, "Login_Username", wait="x")
    # base.input_text(loc, "Login_Username", "aaaaaa")
    # base.click_element((By.CLASS_NAME, "input_submit"), "Login_Username")
    #
    # print(base.get_text((By.XPATH, '//div[@id="error_info"]'), "Login_Submit-clicked"))
    # print(base.get_attribute((By.XPATH, '//div[@id="error_info"]'), "Login_Submit-clicked", "id"))
    # driver.close()
