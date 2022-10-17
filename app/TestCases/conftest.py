import os

import pytest
import yaml
from appium import webdriver

from app.Common.path_handler import conf_dir


"""
fixture: scope, yield, return value
"""


# init the base driver
def _base_driver(port=4723, **kwargs):
    # read app caps values
    with open(os.path.join(conf_dir, "desired_caps.yaml"), encoding="utf-8") as fs:
        desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
    # if kwargs:
    #     for k,v in kwargs.items():
    #         desired_caps[k] = v
    # init driver
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), desired_caps)
    # return driver
    return driver


# login process
def _login_process(driver):
    # check main page, if no login button, pass
    try:
        # find login element in homepage
        pass
    except:
        # try login process
        # click button
        # input username, password
        # click submit
        pass
    else:
        # login already, nothing to do
        pass


# init driver and login
@pytest.fixture()
def init_driver_login():
    # ini driver
    driver = _base_driver()
    # login
    # if login pass; else login with user/password
    _login_process(driver)
    yield

    driver.quit()

