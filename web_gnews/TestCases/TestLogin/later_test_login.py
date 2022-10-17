import pytest

from web.PageObjects.home_page import HomePage
from web.PageObjects.login_page import LoginPage
from web.TestData.login_data import login_data, invalid_data

"""
prefix: init login_page driver
test_data, 
    user: aaaaaa
    password: qqqqqqqq
assert,
    success: jump to homepage, 'logout' button
"""


@pytest.mark.usefixtures("init", "back_to_login_page")
class TestLogin:

    def test_login_success(self, init):
        # test step, login
        LoginPage(init).login(login_data["user"], login_data["password"])
        # assert,
        assert HomePage(init).is_exit_exist()

    @pytest.mark.parametrize("case", invalid_data)
    def test_login_failed_user_password_wrong(self, init, case):
        login_page = LoginPage(init)
        login_page.login(case["user"], case["password"])
        assert case["check"] == login_page.get_error_msg_from_login_area()




