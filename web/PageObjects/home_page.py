from selenium.webdriver import ActionChains

from web.PageElementsLocator.home_page_locator import HomePageLocators as loc
from web.Common.basepage import BasePage


class HomePage(BasePage):

    def is_exit_exist(self):
        """
        if exit exists, return True
        :return: True/False
        """
        try:
            self.wait_element_visible(loc.exit_loc, "Homepage_Check_exist_button")
        except:
            return False
        else:
            return True

    def click_product_list(self):
        """
        Mouse over level1 item, when level2 appear, move to and click
        :return:
        """
        ele = self.get_element(loc.product_list_level1, "Homepage_Product-list-level1")
        # mouse over the element
        # 1. ActionChains instance
        ta = ActionChains(self.driver)
        # 2、mouse action
        ta.move_to_element(ele).perform()

        # waiting for leverl-3 menu item visible, and click
        self.click_element(loc.product_list_mobile, "Homepage_Click-to-product-list")


