
from web.PageElementsLocator.login_page_locator import LoginPageLocators as loc
from web.Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, user, password):
        self.input_text(loc.username_loc, "Login_input_username", user)
        self.input_text(loc.password_loc, "Login_input_password", password)
        self.click_element(loc.submit_loc, "Login_click_submit")

    def get_error_msg_from_login_area(self):
        """
        get error messages when login failed.
        :return: text
        """
        return self.get_text(loc.login_failed_error_msg_loc, "Login_Get_error_msg")

