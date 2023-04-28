#  method to create a Wiki-Add-Space-Page object
# contains all basic methods to run on this page
# ! we should provide browser and URL as parameters when creating an instance of that class

from pages.base_page import BasePage
from pages.locators import AddSpacePageLocators
import time
from selenium.webdriver.common.keys import Keys


class WikiAddSpacePage(BasePage):

    # creates a new space with logo, title, description and category provided
    def create_space(self, space_data):
        choose_space_logo_button = self.browser.find_element(*AddSpacePageLocators.CHOOSE_SPACE_LOGO_BUTTON)
        time.sleep(1)
        choose_space_logo_button.click()
        time.sleep(1)
        random_logo = self.browser.find_element(*AddSpacePageLocators.RANDOM_LOGO)
        random_logo.click()
        time.sleep(2)

        title_field = self.browser.find_element(*AddSpacePageLocators.TITLE_FIELD)
        title_field.send_keys(space_data["title"])
        time.sleep(2)

        description_field = self.browser.find_element(*AddSpacePageLocators.DESCRIPTION_FIELD)
        description_field.send_keys(space_data["desc"])
        time.sleep(2)

        category_field = self.browser.find_element(*AddSpacePageLocators.CATEGORY_FIELD)
        category_field.click()
        category_field.send_keys(space_data["category"])
        category_field.send_keys(Keys.RETURN)  # to submit input by typing "Return/Enter"
        time.sleep(2)

        add_button = self.browser.find_element(*AddSpacePageLocators.ADD_SPACE_BUTTON)
        add_button.click()
        time.sleep(2)
