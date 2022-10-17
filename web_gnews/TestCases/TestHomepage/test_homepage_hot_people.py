
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
from web_gnews.PageElementsLocator.home_page_locator import HomePageLocators
from web_gnews.PageObjects.home_page import HomePage
from web_gnews.PageObjects.hot_people_page import HotPeoplePage


@pytest.mark.usefixtures("init")
class TestHotPeople:

    @pytest.mark.test
    @pytest.mark.parametrize("loc, loc_txt", HomePageLocators.loc_lst)
    @pytest.mark.usefixtures("back_to_home_page")
    def test_click_hot_people_link(self, init, loc, loc_txt):
        """
        1 home page;
            homepage, -click-hot-people-link;
            hot people page, check title text match the 'homepage' link text
        :return:
        """
        # instances all should be used in this case.
        homepage = HomePage(init)
        hot_people_page = HotPeoplePage(init)

        logger.info("======== test start =======")
        # homepage, -click-hot-people;
        homepage_text = homepage.get_hot_people_link_text(loc_txt)
        logger.info(f"Hot people text in Homepage is: {homepage_text}")
        homepage.click_hot_people_link(loc)
        # hot people detail page, waiting for title and page content
        if hot_people_page.is_title_exist():
            title_text = hot_people_page.get_hot_people_title_text()
            logger.info(f"Hot people title text is: {title_text}")
            assert title_text == homepage_text
        else:
            logger.info("Hot people page load timeout(20s).")
            assert False, "Hot people page load timeout(20s)."



