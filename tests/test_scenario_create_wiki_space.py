#
from pages.wiki_page import WikiPage
from pages.wiki_add_space_page import WikiAddSpacePage
from pages.dasboards_page import DashboardPage
from config import Links
from tests.test_data import TestData
import pytest
import time


class TestScenarioCreateWiki:

    @pytest.mark.parametrize("space_data", TestData.space_data)
    def test_create_and_edit_space(self, browser, space_data, admin_login):  # admin_login here is a fixture to log in first
        dashboard_page = DashboardPage(browser, Links.analytics_page)
        time.sleep(2)
        dashboard_page.navigate_to_wiki()

        wiki_page = WikiPage(browser, Links.wiki_page)
        # TODO: expand wiki menu to be able to click on Add button
        # wiki_page.navigate_to_create_space()
        # assert browser.current_url == Links.wiki_add_space_page
        #
        # wiki_add_space = WikiAddSpacePage(browser, Links.wiki_add_space_page)
        # wiki_add_space.create_space(space_data)
