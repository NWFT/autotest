
from web.PageElementsLocator.cart_detail_locator import CartDetailLocators as loc
from web.Common.basepage import BasePage


class CartDetailPage(BasePage):

    def get_product_name(self):
        return self.get_text(loc.product_name_loc, "CartDetailPage_Get-product-name")

    def delete_product_item(self):
        self.click_element(loc.delete_product_item_loc, "CartPage_Delete-product-item")

    def click_to_select(self):
        pass

    def click_to_deselect(self):
        pass

    def click_to_add(self):
        pass

    def click_to_decrease(self):
        pass

    def click_to_delete(self):
        pass

    def click_to_generate_order(self):
        pass

    def get_product_price(self):
        pass

    def get_product_number(self):
        pass

    def get_product_total_money(self):
        pass

