
from selenium.webdriver.common.by import By


class ProductListLocators:
    # ranking rate
    rank_loc = (By.XPATH, '//div[@class="r_wrap fr clearfix"]//div[@class="sort_bar"]/a')

    # product list
    product_list_loc = (By.XPATH, '//div[@class="r_wrap fr clearfix"]//h4')

    # hot ranking

