from selenium.webdriver import ActionChains

from web_gnews.PageElementsLocator.home_page_locator import HomePageLocators as loc
from web_gnews.Common.basepage import BasePage


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

    def click_hot_people_link(self, locator=loc.hot_people_list_loc):
        """
        Mouse over 'hot people' item, click the item
        :return:
        """
        self.click_element(locator, "Homepage_Hot-people-link")
        # # mouse over the element
        # # 1. ActionChains instance
        # ta = ActionChains(self.driver)
        # # 2、mouse action
        # ta.move_to_element(ele).perform()

    def get_hot_people_link_text(self, locator=loc.hot_people_list_text_loc):
        """
        get hot people link text
        :return:
        """
        return self.get_text(locator, "Homepage_Get-hot-people-link-text")
