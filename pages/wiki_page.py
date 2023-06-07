#  method to create a Wiki-Page object
# contains all basic methods to run on this page
# ! we should provide browser and URL of the page as parameters when creating an instance of that class

import time
from locators.wiki_page_locators import WikiPageLocators
from pages.base_page import BasePage

class WikiPage(BasePage):

    def navigate_to_create_space(self):
        hamburger_button = self.browser.find_element(*WikiPageLocators.HAMBURGER_BUTTON)
        hamburger_button.click()
        time.sleep(2)
        create_space_button = self.browser.find_element(*WikiPageLocators.CREATE_SPACE_BUTTON)
        create_space_button.click()
        time.sleep(2)

    # checks that some space (with the title provided) is present in the list of spaces
    def space_with_some_title_listed(self, title_to_find):
        all_space_titles = self.browser.find_elements(*WikiPageLocators.ALL_SPACE_TITLES)
        for title in all_space_titles:
            if title.text == title_to_find:
                return True
        return False

    # checks that some space (with the description provided) is present in the list of spaces
    def space_with_description_listed(self, description_to_find):
        all_space_desc = self.browser.find_elements(*WikiPageLocators.ALL_SPACE_DESCRIPTIONS)
        for desc in all_space_desc:
            if desc.text == description_to_find:
                return True
        return False

    # opens a specific space page (by the title provided)
    def navigate_to_space_with_title(self, title_to_find):
        all_space_titles = self.browser.find_elements(*WikiPageLocators.ALL_SPACE_TITLES)
        for title in all_space_titles:
            if title.text == title_to_find:
                title.click()

    # TODO:
    # def delete_space_with_title(self, title_to_find):
    #     all_space_titles = self.browser.find_elements(*WikiPageLocators.ALL_SPACE_TITLES)
    #     for title in all_space_titles:
    #         if title.text == title_to_find:






