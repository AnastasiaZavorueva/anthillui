# by using object of this class you can select date on date-picker_element
from selenium.webdriver.chrome.webdriver import WebDriver


class DatePickerFunctionality:
    def __init__(self, browser: WebDriver, timeout=10):  # that is a class constructor
        self.browser = browser
        self.browser.implicitly_wait(timeout)  # by that browser will implicitly spend 10 seconds to find every
