from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web.PageElementsLocator.login_page_locator import LoginPageLocators as loc


class LoginPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # methods: Elements' operation
    def input_username(self, user):
        self.wait.until(EC.visibility_of_element_located(loc.username_loc))
        self.driver.find_element(*loc.username_loc).send_keys(user)

    def input_password(self, password):
        self.wait.until(EC.visibility_of_element_located(loc.password_loc))
        self.driver.find_element(*loc.password_loc).send_keys(password)

    def click_submit(self):
        self.wait.until(EC.visibility_of_element_located(loc.submit_loc))
        self.driver.find_element(*loc.submit_loc).click()

    def login(self, user, password):
        self.wait.until(EC.visibility_of_element_located(loc.username_loc))
        self.driver.find_element(*loc.username_loc).send_keys(user)
        self.driver.find_element(*loc.password_loc).send_keys(password)
        self.driver.find_element(*loc.submit_loc).click()

    def get_error_msg_from_login_area(self):
        """
        get error messages when login failed.
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(loc.login_failed_error_msg_loc))
        return self.driver.find_element(*loc.login_failed_error_msg_loc).text

