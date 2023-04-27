#  file to collect all fixtures

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Links
from pages.locators import LoginPageLocators
from tests.test_data import TestData
from pages.login_page import LoginPage
import time


#  fixture to create a browser window
#  automatically & implicitly run for every test-function (done by "autouse" parameter)
@pytest.fixture(autouse=True)  # by parameter "autouse" the fixture is executed automatically and implicitly in the
# beginning of every test
def browser():
    browser = webdriver.Chrome(service=Service(executable_path='.chromedriver'))
    yield browser
    browser.quit()


#  fixture to login on the website - starts from login page and finishes on the Analytics page
@pytest.fixture()
def admin_login(browser):
    login_page = LoginPage(browser, Links.login_page)
    login_page.open_page()
    login_page.login(TestData.valid_login_credentials_admin[0])
