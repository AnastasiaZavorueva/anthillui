#  method to create a Wiki-Edit-Space-Page object
# contains all basic methods to run on this page
# ! we should provide browser and URL of the page as parameters when creating an instance of that class

from pages.base_page import BasePage
from pages.locators import EditSpacePageLocators
import time


class WikiEditSpacePage(BasePage):

    # saves the result of editing some space
    def save_edit_space_result(self):
        save_edit_button = self.browser.find_element(*EditSpacePageLocators.EDIT_SPACE_BUTTON)
        save_edit_button.click()
        time.sleep(1)

    #  navigates to the list of spaces on Wiki page
    def navigate_to_spaces_list(self):
        list_of_spaces_button = self.browser.find_element(*EditSpacePageLocators.LIST_OF_SPACES)
        list_of_spaces_button.click()
        time.sleep(1)