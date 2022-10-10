
"""
Add products to Cart,
0- login
1. Pages: login/home/pruduct-list/pruduct-detail/cart-info

2. Test cases,
# pre-condition (fixture): login
# test steps
# assert

"""
import time

import pytest

from web.Common.my_logger import logger
from web.PageObjects.home_page import HomePage
from web.PageObjects.product_list_page import ProductListPage
from web.PageObjects.product_detail_page import ProductDetailPage
from web.PageObjects.cart_detail_page import CartDetailPage
from web.TestData import global_data


@pytest.mark.usefixtures("driver")
class TestCart:

    @pytest.mark.test
    def test_add_product_to_cart(self, driver):
        """
        1 login;
            homepage, -click-pruduct-list;
            product-list-page, -click-pruduct-detail;
            product-detail-page, -click-add-cart; - alert ok
            product-detail-page, -click-cart-button

        :return:
        """
        homepage = HomePage(driver)
        product_list_page = ProductListPage(driver)
        product_detail = ProductDetailPage(driver)
        cart_page = CartDetailPage(driver)

        logger.info("======== test =======")
        homepage.load_page_with_url(global_data.BASE_URL)
        # homepage, -click-pruduct-list;
        homepage.click_product_list()
        # product-list-page, -click-pruduct-detail;
        product_list_page.click_to_product_detail_page()
        # product-detail-page, -click-add-cart; - alert ok
        product_detail.add_to_cart()
        name1 = product_detail.get_product_name()
        logger.info(f"Product name in detail page is: {name1}")
        # product-detail-page, -click-cart-button
        product_detail.click_to_cart_detail()
        # in Cart page, get product name, and delete the item
        name2 = cart_page.get_product_name()
        cart_page.delete_product_item()
        logger.info(f"Product name in cart page is: {name2}")
        # compare product name in cart and detail page
        assert name1 == name2


