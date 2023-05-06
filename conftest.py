#  file to collect all fixtures
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Links
from tests.test_data import TestData
from pages.login_page import LoginPage


#  fixture to open Chrome browser for running tests
#  automatically & implicitly started for every test (by "autouse" parameter)
#  where this fixture is mentioned as a parameter of test
@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome(service=Service(executable_path='.chromedriver'))
    now = datetime.now()
    yield browser
    # browser.save_screenshot(f"screenshot_{now}.png")
    browser.quit()


#  fixture to login in with ADMIN credentials - starts from login page and finishes on the Analytics page
@pytest.fixture()
def admin_login(browser):
    login_page = LoginPage(browser, Links.login_page)
    login_page.open_page()
    login_page.login(TestData.valid_login_credentials_admin[0])
