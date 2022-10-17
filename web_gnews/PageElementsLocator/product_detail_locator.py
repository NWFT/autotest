
from selenium.webdriver.common.by import By


class ProductDetailLocators:
    # add cart button
    add_cart_button_loc = (By.ID, "add_cart")

    # cart detail button
    cart_detail_button_loc = (By.XPATH, '//a[@class="cart_name fl"]')

    # product name
    product_name_loc = (By.XPATH, '//div[@class="goods_detail_list fr"]/h3')