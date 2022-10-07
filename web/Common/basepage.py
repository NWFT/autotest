
"""
Why?
    1. log every step for traceability
    2. deduce duplicated codes
        a) wait element visible
        b) find element
        c) click()
        d) input()
        e) get text
        f) get attributes
"""
import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from web.Common.my_logger import logger
from web.Common.path_handler import screenshots_dir
from web.TestData import global_data


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_visible(self, locator, page_operation, timeout=10, poll_frequency=0.5):
        """
        Wait element visible.
        :param locator: element locator, from PageElementsLocator
        :param page_operation: page? which page, eg., login_page, register_page
                            operation? click, input, get_text, get_attributes
        :param timeout: waiting timeout default=10s
        :param poll_frequency: poll frequency, default=0.5s
        :return: None
        """
        logger.info(f"With {page_operation}, Waiting for element {locator} visible.")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            # log error
            logger.exception(f"Waiting element timeout after {timeout}s.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case failed
            raise
        else:
            end = time.time()
            logger.info("Spent {:.3f} seconds, on waiting.".format(end-start))

    def wait_page_contains_element(self, locator, page_operation, timeout=10, poll_frequency=0.5):
        """
        Wait page contains element.
        :param locator: element locator, from PageElementsLocator
        :param page_operation: page? which page, eg., login_page, register_page
                            operation? click, input, get_text, get_attributes
        :param timeout: waiting timeout default=10s
        :param poll_frequency: poll frequency, default=0.5s
        :return: None
        """
        logger.info(f"With {page_operation}, Waiting for page contains element {locator}.")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            # log error
            logger.exception(f"Waiting page contains element timeout after {timeout}s.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case failed
            raise
        else:
            end = time.time()
            logger.info("Spent {:.3f} seconds, on waiting.".format(end-start))

    def get_element(self, locator, page_operation, timeout=10, poll_frequency=0.5, wait=None):
        # before get element, should check page contains, or element visible
        # if wait Not None, page should contains element
        # else visible, default is wait_element_visible
        if wait:
            self.wait_page_contains_element(locator, page_operation, timeout, poll_frequency)
        else:
            self.wait_element_visible(locator, page_operation, timeout, poll_frequency)

        logger.info(f"With {page_operation}, Finding element {locator}.")
        try:
            ele = self.driver.find_element(*locator)
        except:
            # log error
            logger.exception("Finding element failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise
        else:
            return ele

    def click_element(self, locator, page_operation, timeout=10, poll_frequency=0.5):
        # wait element, find element
        ele = self.get_element(locator, page_operation, timeout, poll_frequency)
        # click element
        logger.info(f"With {page_operation}, Click element {locator}.")
        try:
            ele.click()
        except:
            # log error
            logger.exception("Click element failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise

    def input_text(self, locator, page_operation, value, timeout=10, poll_frequency=0.5):
        # wait element, find element
        ele = self.get_element(locator, page_operation, timeout, poll_frequency)
        # input text
        logger.info(f"With {page_operation}, send text {value} to {locator}.")
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            # log error
            logger.exception("Input text failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise

    def get_text(self):
        pass

    def get_attribute(self):
        pass

    def get_page_screenshot(self, page_operation):
        # image-name-format: {Page-name_Operation}_timestamp.png
        cur_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        file_path = os.path.join(screenshots_dir, "{}_{}.png".format(page_operation, cur_time))
        self.driver.save_screenshot(file_path)
        logger.info(f"Screenshot has been saved at: {file_path}")


if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    base = BasePage(driver)
    driver.get(global_data.LOGIN_URL)

    from web.PageElementsLocator.login_page_locator import LoginPageLocators
    loc = LoginPageLocators.username_loc
    # base.wait_element_visible(loc, "Login_Username")

    # get element
    # ele = base.get_element(loc, "Login_Username", wait="x")
    base.input_text(loc, "Login_Username", "aaaaaa")
    base.click_element(LoginPageLocators.submit_loc, "Login_Username")
    driver.close()
