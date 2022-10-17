
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

from web_gnews.Common.my_logger import logger
from web_gnews.PageObjects.home_page import HomePage
from web_gnews.PageObjects.product_list_page import ProductListPage
from web_gnews.PageObjects.product_detail_page import ProductDetailPage
from web_gnews.PageObjects.cart_detail_page import CartDetailPage


@pytest.mark.usefixtures("login", "back_home")
class TestCart:

    @pytest.mark.test
    def test_add_product_to_cart(self, login):
        """
        1 login;
            homepage, -click-pruduct-list;
            product-list-page, -click-pruduct-detail;
            product-detail-page, -click-add-cart; - alert ok
            product-detail-page, -click-cart-button

        :return:
        """
        logger.info("======== test =======")
        # homepage, -click-pruduct-list;
        HomePage(login).click_product_list()
        # product-list-page, -click-pruduct-detail;
        ProductListPage(login).click_to_product_detail_page()
        # product-detail-page, -click-add-cart; - alert ok
        product_detail = ProductDetailPage(login)
        product_detail.add_to_cart()
        name1 = product_detail.get_product_name()
        logger.info(f"Product name in detail page is: {name1}")
        # product-detail-page, -click-cart-button
        product_detail.click_to_cart_detail()
        # in Cart page, get product name, and delete the item
        cart_page = CartDetailPage(login)
        name2 = cart_page.get_product_name()
        cart_page.delete_product_item()
        logger.info(f"Product name in cart page is: {name2}")
        # compare product name in cart and detail page
        assert name1 == name2

    # ddt for add cart failed scenarios
    # @pytest.mark.parametrize()
    # @pytest.mark.usefixtures("back_home")
    # def test_add_cart_failed_cases(self, back_home):
    #     # homepage, -click-product-list;
    #     HomePage(back_home).click_product_list()
    #     time.sleep(5)


