from pages.base_page import BasePage
from pages.locators import AddSpacePageLocators
from tests.test_data import TestData


class WikiAddSpacePage(BasePage):

    def create_space(self, space_data):
        choose_space_logo_button = self.browser.find_element(*AddSpacePageLocators.CHOOSE_SPACE_LOGO_BUTTON)
        choose_space_logo_button.click()
        random_logo = self.browser.find_element(*AddSpacePageLocators.RANDOM_LOGO)
        random_logo.click()
        title_field = self.browser.find_element(*AddSpacePageLocators.TITLE_FIELD)
        title_field.send_keys(TestData.space_data[0])
        description_field = self.browser.find_element(*AddSpacePageLocators.DESCRIPTION_FIELD)
        description_field.send_keys(TestData.space_data[1])

        # CAN'T FINISH THIS PART because of not being able to retrieve a locator for button "Add"
        # category_field = self.browser.find_element(*AddSpacePageLocators.CATEGORY_FIELD)
        # category_field.click()
        # category_field.send_keys(TestData.space_category)

        add_button = self.browser.find_element(*AddSpacePageLocators.ADD_SPACE_BUTTON)
        add_button.click()
