from selenium.webdriver.common.by import By


class HomePageLocators:
    # EXIT button when user login
    exit_loc = (By.XPATH, '//a[@class="quit"]')

    # Product list link at left navigation bar
    product_list_level1 = (By.XPATH, '//div[@class="level1"]')
    product_list_mobile = (By.XPATH, '//div[@class="group_detail fl"]/a')

    # user cart
    user_cart_loc = ()


