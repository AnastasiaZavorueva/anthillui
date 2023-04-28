#  method to create a Dashboard-Page object
# contains all basic methods to run on this page
# ! we should provide browser and URL as parameters when creating an instance of that class

import time

from pages.base_page import BasePage
from pages.locators import DashboardsPageLocators


class DashboardPage(BasePage):

    def navigate_to_wiki(self):
        wiki_button = self.browser.find_element(*DashboardsPageLocators.WIKI_BUTTON)
        wiki_button.click()
        time.sleep(4)

