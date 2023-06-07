from selenium.webdriver.common.by import By


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
                                  "div.flatpickr-calendar.open div.dayContainer span.flatpickr-day:not("
                                  ".prevMonthDay):not(.nextMonthDay)")

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
                                        "nav.v-navigation-drawer--left.v-navigation-drawer--temporary "
                                        "span.flatpickr-day:not(.prevMonthDay):not(.nextMonthDay)")
    LEFT_PICKER_MONTH_DROPDOWN = (By.CSS_SELECTOR,
                                  "nav.v-navigation-drawer--left.v-navigation-drawer--temporary "
                                  "select.flatpickr-monthDropdown-months")
    LEFT_PICKER_NEXT_MONTH_BUTTON = (
        By.CSS_SELECTOR, "nav.v-navigation-drawer--left.v-navigation-drawer--temporary span.flatpickr-next-month")

    # ! ----------- END OF LOCATORS FOR ELEMENTS IN LEFT DATE PICKER

    LIST_ALL_MONTH_EVENTS_BUTTON = (By.XPATH,
                                    "//button[contains(text(),'список')]")
    ALL_ROWS_IN_MONTH_EVENTS_LIST = (By.CSS_SELECTOR, "table.fc-list-table  tbody tr")
    ALL_EVENT_TITLES_IN_MONTH = (By.CSS_SELECTOR, "table.fc-list-table  tbody tr.fc-list-event a")

    DELETE_EVENT_BUTTON = (By.CSS_SELECTOR, "nav.v-navigation-drawer--temporary button.text-error")
