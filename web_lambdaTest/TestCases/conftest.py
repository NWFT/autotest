import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from web.Common.my_logger import logger
from web.PageObjects.login_page import LoginPage
from web.TestData import global_data
from web.TestData.global_data import normal_user, admin_user
from selenium.webdriver.remote.remote_connection import RemoteConnection

"""
fixture: scope, yield, return value
"""


@pytest.fixture(scope="class", name="init")
def init_driver():
    """
    instance web driver, Login_page
    :return: driver
    """
    logger.info("======== class fixture, open browser, goto login page =======")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(global_data.IMPLICITLY_WAIT_TIME)
    driver.get(global_data.LOGIN_URL)
    yield driver
    logger.info("======== class fixture, close browser =======")
    driver.quit()


@pytest.fixture(scope="function", name="back_to_login_page")
def back_to_login_page(init):
    logger.info("======== function fixture, goto login page =======")
    init.get(global_data.LOGIN_URL)


@pytest.fixture(scope="class", name="login")
def init_global_login_driver(init):
    """
    instance web driver, Login_page, and login
    after, close driver
    :return: driver
    """
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.implicitly_wait(global_data.IMPLICITLY_WAIT_TIME)
    # driver.get(global_data.LOGIN_URL)
    # LoginPage(driver).login(normal_user["user"], normal_user["password"])
    # yield driver
    # driver.quit()
    # user fixture's feature, use "init" fixture, delete overlapped codes.
    logger.info("======== class fixture, login page, login with global normal user =======")
    LoginPage(init).login(normal_user["user"], normal_user["password"])
    yield init


@pytest.fixture(scope="function", name="back_home")
def back_homepage(login):
    logger.info("======== function fixture, goto home page =======")
    login.get(global_data.BASE_URL)


@pytest.fixture(scope='function', name="driver")
def driver(request):
    desired_caps = {}

    browser = {
        "platform": "Windows 10",
        "browserName": "chrome",
        "version": "latest"
    }

    desired_caps.update(browser)
    test_name = request.node.name
    build = "Add product to Cart"
    tunnel_id = False
    username = "nwft.sh"
    access_key = "y4CugKvEyf8oTH8NoTaVw1vlrweUGHj8IMCGdTzLbCWNOUPFOe"

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['build'] = build
    desired_caps['name'] = test_name
    desired_caps['video'] = True
    desired_caps['visual'] = True
    desired_caps['network'] = True
    desired_caps['console'] = True
    caps = {"LT:Options": desired_caps}

    executor = RemoteConnection(selenium_endpoint)
    browser = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )

    yield browser

    def fin():
        # browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
        # "failed").lower()))
        if request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)