#  file to collect all locators

from selenium.webdriver.common.by import By


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
    SPACE_TITLE = (By.XPATH, "//ul[@class='leftSidebarUL']//li[1]//div[@class='text-bold']")
    DEFAULT_PAGE_FOR_SPACE_FIELD_LABEL = (By.XPATH, "//div//label[contains(text(), 'Страница по умолчанию')]")
    FAVORITE_PAGES_AREA_LABEL = (By.XPATH, "//div//li[contains(text(), 'Избранное')]")
    ALL_PAGES_LABEL = (By.XPATH, "//div//li[contains(text(), 'Страницы')]")
    ANALYTICS_BUTTON = (By.XPATH, "//a[@href='/dashboards/analytics']")
    WIKI_BUTTON = (By.XPATH, "//a[@href='/apps/wiki']")


class EditSpacePageLocators:
    EDIT_SPACE_BUTTON = (By.CSS_SELECTOR, "form button.v-btn--elevated")  # actually used for saving result of editing
    LIST_OF_SPACES = (By.XPATH, "//button[@type='reset']")
    CHANGES_SAVED_POPUP = (By.XPATH, "//div[@class='notification-title']")


class DashboardsPageLocators:  # naming?
    ANALYTICS_BUTTON = (By.XPATH, "//a[@href='/dashboards/analytics']")
    WIKI_BUTTON = (By.XPATH, "//a[@href='/apps/wiki']")
    CALENDAR_BUTTON = (By.XPATH, "//a[@href='/apps/calendar']")


class CalendarPageLocators:
    HAMBURGER_BUTTON = (By.XPATH, "//button[@title='calendarDrawerToggler']")
    ADD_EVENT_BUTTON = (By.CSS_SELECTOR, "nav.v-navigation-drawer--left button.v-btn--elevated")
    ADD_EVENT_FORM = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary")


    # ! ----------- LOCATORS FOR ELEMENTS IN CREATE/EDIT EVENT FORM

    # by using the next locator we get a collection of web elements
    # that will contain these keys and its values (use these indices to get a specific element from collection):
    # 1 - EVENT_TITLE_FIELD, 2 - EVENT_TYPE_FIELD, 3 - START_DATE_AND_TIME_FIELD
    # 4 - END_DATE_AND_TIME_FIELD, 5 - PLACE_FIELD
    # (in case of the event type "meeting" also: 5 - PARTICIPANTS_FIELD, 6 - PLACE_FIELD)
    EVENT_FORM_TEXT_FIELDS = (
        By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary div[role='textbox'] input[type='text']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary div[role='textbox'] textarea")

    # by using the next locator we get a collection of web elements
    # (use these indices to get a specific element from collection):
    # 2 - EVENT_TYPE_FIELD
    EVENT_TYPE_FIELD = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary div[role='textbox']")

    CURRENT_YEAR_SHOWN = (By.CSS_SELECTOR, "div.flatpickr-calendar.open input.cur-year")
    NEXT_MONTH_ARROW_BUTTON = (By.CSS_SELECTOR, "div.flatpickr-calendar.open span.flatpickr-next-month")
    MONTH_DROPDOWN_LIST = (By.CSS_SELECTOR, "div.flatpickr-calendar.open select.flatpickr-monthDropdown-months")
    EVENT_HOUR_FIELD = (By.CSS_SELECTOR, "div.flatpickr-calendar.open input.flatpickr-hour")
    EVENT_MINUTES_FIELD = (By.CSS_SELECTOR, "div.flatpickr-calendar.open input.flatpickr-minute")

    ALL_DAYS_OF_SELECTED_MONTH = (By.CSS_SELECTOR,
                                  "div.flatpickr-calendar.open div.dayContainer span.flatpickr-day:not(.prevMonthDay):not(.nextMonthDay)")

    # using the next locator we get collection of 2 elements
    # (use these indices to get a specific element from collection):
    # 0 - START_DATE_FIELD, 1 - END_DATE_FIELD
    EVENT_DATE_AND_TIME_FIELDS = (
        By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary input.flat-picker-custom-style.form-control")

    EVENT_TYPES = {
        "event": (By.XPATH, "//div[@class='v-list-item__content']//div[contains(text(),'Мероприятие')]"),
        "meeting": (By.XPATH, "//div[@class='v-list-item__content']//div[contains(text(),'Встеча')]"),
        "task": (By.XPATH, "//div[@class='v-list-item__content']//div[contains(text(),'Задача')]"),
        "personal": (By.XPATH, "//div[@class='v-list-item__content']//div[contains(text(),'Личное')]")
    }

    SAVE_BUTTON = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary button[type='submit']")
    # CANCEL_BUTTON =
    # ALL_DAY_EVENT_TOGGLER =

    # ! ----------- END OF LOCATORS FOR ELEMENTS IN CREATE EVENT FORM


    # ! ----------- LOCATORS FOR ELEMENTS IN LEFT DATE PICKER

    LEFT_DATEPICKER_IN_CALENDAR = (By.CSS_SELECTOR, "nav.v-navigation-drawer--left.v-navigation-drawer--temporary")
    LEFT_PICKER_YEAR_SHOWN = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary input.cur-year")
    LEFT_PICKER_ALL_MONTH_DAYS_SHOWN = (By.CSS_SELECTOR,
                                        "nav.v-navigation-drawer--left.v-navigation-drawer--temporary span.flatpickr-day:not(.prevMonthDay):not(.nextMonthDay)")
    LEFT_PICKER_MONTH_DROPDOWN = (By.CSS_SELECTOR,
                                  "nav.v-navigation-drawer--left.v-navigation-drawer--temporary select.flatpickr-monthDropdown-months")
    LEFT_PICKER_NEXT_MONTH_BUTTON = (
        By.CSS_SELECTOR, "nav.v-navigation-drawer--left.v-navigation-drawer--temporary span.flatpickr-next-month");

    # ! ----------- END OF LOCATORS FOR ELEMENTS IN LEFT DATE PICKER

    LIST_ALL_MONTH_EVENTS_BUTTON = (By.XPATH,
                                    " //button[contains(text(),'список')]")  # button.fc-listMonth-button # button[title='список']  #div.fc-button-group button[title='список']  # div.fc-button-group button.fc-listMonth-button
    ALL_ROWS_IN_MONTH_EVENTS_LIST = (By.CSS_SELECTOR, "table.fc-list-table  tbody tr")
    ALL_EVENT_TITLES_IN_MONTH = (By.CSS_SELECTOR, "table.fc-list-table  tbody tr.fc-list-event a")

    DELETE_EVENT_BUTTON = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary button.text-error")
