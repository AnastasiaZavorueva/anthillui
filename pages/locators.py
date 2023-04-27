#  file to collect all locators used in page-files

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
    CREATE_SPACE_BUTTON = (By.CSS_SELECTOR, "main nav button.v-btn--elevated")


class AddSpacePageLocators:
    CHOOSE_SPACE_LOGO_BUTTON = (By.ID, "icon")
    RANDOM_LOGO = (By.XPATH, "//body/div[2]/div[2]/div[1]/div[1]/button[58]")  # just some random logo with alien
    TITLE_FIELD = (By.ID, "title")
    DESCRIPTION_FIELD = (By.ID, "description")
    CATEGORY = (By.ID, "category")
    ADD_SPACE_BUTTON = (By.CSS_SELECTOR, "form button.v-btn--elevated")


class EditSpacePageLocators:
    EDIT_SPACE_BUTTON = (By.CSS_SELECTOR, "form button.v-btn--elevated")  # actually used for saving result of edit
    LIST_OF_SPACES = (By.XPATH, "//button[@type='reset']")


class DashboardsPageLocators:  # naming?
    ANALYTICS_BUTTON = (By.XPATH, "//a[@href='/dashboards/analytics']")
    WIKI_BUTTON = (By.XPATH, "//a[@href='/apps/wiki']")
