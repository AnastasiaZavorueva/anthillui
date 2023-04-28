#  file to collect all locators

from selenium.webdriver.common.by import By  # package with By-methods to use in locators


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@type = 'checkbox']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Forgot Password?')]")
    CREATE_ACCOUNT_LINK = (By.PARTIAL_LINK_TEXT, "Create an account")
    LOG_BUTTON_WITH_FACEBOOK = (By.XPATH, "//div[@class='d-flex justify-center flex-wrap gap-3']/button[1]")
    LOG_BUTTON_WITH_GOOGLE = (By.XPATH, "//div[@class='d-flex justify-center flex-wrap gap-3']/button[2]")
    LOG_BUTTON_WITH_TWITTER = (By.XPATH, "//div[@class='d-flex justify-center flex-wrap gap-3']/button[3]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//div[text() = 'Email or Password is Invalid']")


class WikiPageLocators:
    HAMBURGER_BUTTON = (By.XPATH, "//div[@class='v-toolbar__prepend']/button[@type='button'][1]")
    SPACES_LIST_BUTTON = (By.XPATH, "//div[@class='v-toolbar__prepend']/button[@type='button'][2]")  # button "Разделы"
    CREATE_SPACE_BUTTON = (By.CSS_SELECTOR, "main nav button.v-btn--elevated")
    ALL_SPACE_TITLES = (By.XPATH, "//main[@class='v-main']//div[@class='v-list-item-title']")
    ALL_SPACE_DESCRIPTIONS = (By.XPATH, "//main[@class='v-main']//div[@class='v-list-item-subtitle']")


class AddSpacePageLocators:
    CHOOSE_SPACE_LOGO_BUTTON = (By.XPATH, "//button[@id='icon']")
    RANDOM_LOGO = (By.XPATH, "//body/div[2]/div[2]/div[1]/div[1]/button[58]")  # just some random logo with alien
    TITLE_FIELD = (By.ID, "title")
    DESCRIPTION_FIELD = (By.ID, "description")
    CATEGORY_FIELD = (By.ID, "category")
    ADD_SPACE_BUTTON = (By.CSS_SELECTOR, "form button.v-btn--elevated")


# locators for the main page of any Wiki space
class SpaceHomePageLocators:
    space_title = (By.XPATH, "//ul[@class='leftSidebarUL']//li[1]//div[@class='text-bold']")
    default_page_for_space_field_label = (By.XPATH, "//div//label[contains(text(), 'Страница по умолчанию')]")
    favorite_pages_area_label = (By.XPATH, "//div//li[contains(text(), 'Избранное')]")
    all_pages_label = (By.XPATH, "//div//li[contains(text(), 'Страницы')]")
    ANALYTICS_BUTTON = (By.XPATH, "//a[@href='/dashboards/analytics']")
    WIKI_BUTTON = (By.XPATH, "//a[@href='/apps/wiki']")


class EditSpacePageLocators:
    EDIT_SPACE_BUTTON = (By.CSS_SELECTOR, "form button.v-btn--elevated")  # actually used for saving result of editing
    LIST_OF_SPACES = (By.XPATH, "//button[@type='reset']")
    CHANGES_SAVED_POPUP = (By.XPATH, "//div[@class='notification-title']")


class DashboardsPageLocators:  # naming?
    ANALYTICS_BUTTON = (By.XPATH, "//a[@href='/dashboards/analytics']")
    WIKI_BUTTON = (By.XPATH, "//a[@href='/apps/wiki']")

