import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from web_gnews.Common.my_logger import logger
from web_gnews.TestData import global_data
from web_gnews.TestData.global_data import normal_user, admin_user

"""
fixture: scope, yield, return value
"""


@pytest.fixture(scope="class", name="init")
def init_driver():
    """
    instance web driver, Home_page
    :return: driver
    """
    logger.info("======== class fixture, open browser, goto home page =======")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(global_data.IMPLICITLY_WAIT_TIME)
    driver.maximize_window()
    driver.get(global_data.BASE_URL)
    yield driver
    logger.info("======== class fixture, close browser =======")
    driver.quit()


@pytest.fixture(scope="function", name="back_to_home_page")
def back_to_home_page(init):
    logger.info("======== function fixture, goto home page =======")
    init.get(global_data.BASE_URL)


