import time

from web.PageElementsLocator.product_detail_locator import ProductDetailLocators as loc
from web.Common.basepage import BasePage


class ProductDetailPage(BasePage):

    def add_to_cart(self):
        """
        click add to cart button, add the product to cart
        :return:
        """
        self.click_element(loc.add_cart_button_loc, "ProductDetailPage_Click-to-add-cart")
        # close the alert window
        time.sleep(1)
        al = self.driver.switch_to.alert
        al.accept()

    def click_ok_button_after_added(self):
        """
        after product added, a popup window, click OK to confirm
        :return:
        """
        pass

    def click_to_cart_detail(self):
        """
        Click to cart detail page
        :return:
        """
        self.click_element(loc.cart_detail_button_loc, "ProductDetailPage_Click-to-cart-detail")

    def get_product_name(self):
        """
        get product name in detail page
        :return:
        """
        return self.get_text(loc.product_name_loc, "ProductDetailPage_Get-product-name")
