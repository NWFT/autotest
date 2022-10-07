
"""
variables will be user globally
"""

import os

# implicitly wait time, 5 means 5s
IMPLICITLY_WAIT_TIME = 5

# url relatives
BASE_URL = "http://www.alex-info.ca:8000/"

# login
LOGIN_URL = os.path.join(BASE_URL, "login/")
# register
REGISTER_URL = os.path.join(BASE_URL, "register/")
# user center
USER_CENTER_URL = os.path.join(BASE_URL, "center/")
# address
ADDRESS_URL = os.path.join(BASE_URL, "addresses/")
# change password
CHANGE_PSW_URL = os.path.join(BASE_URL, "pass/")
# carts
CARTS_URL = os.path.join(BASE_URL, "carts/")
# carts
