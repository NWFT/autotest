import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from web.TestData import global_data
"""
fixture: scope, yield, return value
"""


@pytest.fixture(scope="class", name="init")
def init_driver():
    """
    instance web driver
    :return: driver
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(global_data.IMPLICITLY_WAIT_TIME)
    driver.get(global_data.LOGIN_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", name="back_to_login_page")
def back_to_login_page(init):
    init.get(global_data.LOGIN_URL)

