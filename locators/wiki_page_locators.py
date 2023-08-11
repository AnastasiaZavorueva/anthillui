from selenium.webdriver.common.by import By


class WikiPageLocators:
    HAMBURGER_BUTTON = (By.CSS_SELECTOR, "//div[@class='v-toolbar__prepend']/button[@type='button'][1]")
    SPACES_LIST_BUTTON = (By.XPATH, "//div[@class='v-toolbar__prepend']/button[@type='button'][2]")  # button "Разделы"
    CREATE_SPACE_BUTTON = (By., "main nav button.v-btn--elevated")
    ALL_SPACE_TITLES = (By.XPATH, "//main[@class='v-main']//div[@class='v-list-item-title']")
    ALL_SPACE_DESCRIPTIONS = (By.CSS_SELECTOR, "//main[@class='v-main']//div[@class='v-list-item-subtitle']")
