# by using object of this class you can select date on date-picker_element
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.locators import DatePickerLocators
from selenium.webdriver.common.by import By

class DatePickerFunctionality:
    def __init__(self, browser: WebDriver, timeout=10):  # that is a class constructor
        self.browser = browser
        self.browser.implicitly_wait(timeout)  # by that browser will implicitly spend 10 seconds to find every


    def select_date_on_picker(self, , picker_locator, date_to_select):
        # all_dates_elements = self.browser.find_elements(By.XPATH, f"{picker_locator} + "





