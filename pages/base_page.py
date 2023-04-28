#  basic class for every page in the project
#  methods of base page will be inherited by every child class (=any page of the website that extends BasePage)
# ! we should provide browser and URL as parameters when creating an instance of that class

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys  # package to use some keys from keyboard for inputs


class BasePage:
    def __init__(self, browser: WebDriver, url, timeout=10):  # that is a class constructor
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # by that browser will implicitly spend 10 seconds to find every

    # web-element

    def open_page(self):
        self.browser.get(self.url)  # by that we open the specific website page that implements BasePage

    # method to clear any text field that has autofill
    def clear_text_field(self, element):
        while (element.get_attribute("value") == "") is False:
            element.send_keys(Keys.BACKSPACE)
