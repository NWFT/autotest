
from selenium.webdriver.common.by import By


class CartDetailLocators:
    # product name
    product_name_loc = (By.XPATH, '//ul[@class="cart_list_td clearfix"]//li[@class="col03"]')

    # delete button
    delete_product_item_loc = (By.XPATH, '//li[@class="col08"]/a')


