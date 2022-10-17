from selenium.webdriver import ActionChains

from web_gnews.PageElementsLocator.hot_people_page_locator import HotPeopleLocators as loc
from web_gnews.Common.basepage import BasePage


class HotPeoplePage(BasePage):

    def is_title_exist(self):
        """
        if title exists, return True
        :return: True/False
        """
        try:
            self.wait_element_visible(loc.title_loc, "Hot-People_Check-title-exist")
        except:
            return False
        else:
            return True

    def get_hot_people_title_text(self):
        """
        get hot people title text
        :return:
        """
        return self.get_text(loc.title_loc, "Hot-People_Get-hot-people-title-text")
