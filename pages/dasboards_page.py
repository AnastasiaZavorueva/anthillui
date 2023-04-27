import time

from pages.base_page import BasePage
from pages.locators import DashboardsPageLocators


class DashboardPage(BasePage):

    def navigate_to_wiki(self):
        wiki_button = self.browser.find_element(*DashboardsPageLocators.WIKI_BUTTON)
        wiki_button.click()
        time.sleep(4)

