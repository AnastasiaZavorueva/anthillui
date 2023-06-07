from selenium.webdriver.common.by import By


class EditWikiSpacePageLocators:
    EDIT_SPACE_BUTTON = (By.CSS_SELECTOR, "form button.v-btn--elevated")  # actually used for saving result of editing
    LIST_OF_SPACES = (By.XPATH, "//button[@type='reset']")
    CHANGES_SAVED_POPUP = (By.XPATH, "//div[@class='notification-title']")