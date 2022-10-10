from selenium.webdriver.common.by import By


class LoginPageLocators:
    # username input
    username_loc = (By.NAME, "username")
    # password input
    password_loc = (By.NAME, "password")
    # submit button
    submit_loc = (By.CLASS_NAME, "input_submit")
    # error message locator
    login_failed_error_msg_loc = (By.XPATH, '//div[@id="error_info"]')
