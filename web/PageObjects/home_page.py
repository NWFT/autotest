from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.PageElementsLocator.home_page_locator import HomePageLocators as loc


class HomePage(object):
    # attributes

    # methods
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait_for_page = WebDriverWait(driver, 3)

    def is_exit_exist(self):
        """
        if exit exists, return True
        :return: True/False
        """
        try:
            self.wait_for_page.until(EC.visibility_of_element_located(loc.exit_loc))
        except:
            return False
        else:
            return True



