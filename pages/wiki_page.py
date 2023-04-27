import time
from pages.locators import WikiPageLocators
from pages.base_page import BasePage
from tests.test_data import TestData


class WikiPage(BasePage):

    def navigate_to_create_space(self):
        create_space_button = self.browser.find_element(*WikiPageLocators.CREATE_SPACE_BUTTON)
        create_space_button.click()
        time.sleep(2)








