
"""

"""
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from app.Common.basepage import BasePage
from web.Common.my_logger import logger
from web.Common.path_handler import screenshots_dir
from web.TestData import global_data


class WebPage(BasePage):

    def switch_window(self, name="new"):
        """
        many windows used during test, switch between them.
        :param name: which window switch to, default is the last open one
        :return: None
        """
        # need time to open the new window
        logger.info("switch window begin.")
        time.sleep(1)
        # get all window handlers
        wins = self.driver.window_handles
        logger.info(f"all windows handlers: {wins}")
        # new, switch to the last open window
        if name == "new":
            # switch_to window/frame/
            logger.info(f"Change window to: {wins[-1]}")
            self.driver.switch_to.window(wins[-1])

    # use js to set readonly values
    def input_value_to_readonly_element(self, locator, page_operation, value):
        # get element
        logger.info("Input values to readonly element.")
        ele = self.get_element(locator, page_operation)
        # arguments[0] [1], parameters for js
        js_code = 'arguments[0].removeAttribute("readonly");' \
                  'arguments[0].value = arguments[1];'

        # js, values from outside to js code
        self.driver.execute_script(js_code, ele, value)

    # forward to homepage
    def page_go_to_homepage(self):
        logger.info("set driver go to home page.")
        self.driver.forward()

    # back to last page
    def page_back_to_last(self):
        logger.info("set driver back to the last page.")
        self.driver.back()

    # go to forward page
    def page_forward_to(self):
        logger.info("set driver forward to page.")
        self.driver.forward()

    # refresh current page
    def page_refresh(self):
        logger.info("set driver refresh current page.")
        self.driver.refresh()


if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    base = BasePage(driver)
    driver.get("http://www.alex-info.ca:8000/login/")

    loc = (By.NAME, "username")
    # base.wait_element_visible(loc, "Login_Username")

    # get element
    # ele = base.get_element(loc, "Login_Username", wait="x")
    base.input_text(loc, "Login_Username", "aaaaaa")
    base.click_element((By.CLASS_NAME, "input_submit"), "Login_Username")

    print(base.get_text((By.XPATH, '//div[@id="error_info"]'),"Login_Submit-clicked"))
    print(base.get_attribute((By.XPATH, '//div[@id="error_info"]'), "Login_Submit-clicked", "id"))
    driver.close()
