#  file to collect all fixtures
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Links
from tests.test_data import TestData
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    """fixture to open Chrome browser before running tests, and to quit browser after that;
    automatically & implicitly started (by "autouse" parameter)
    for every test where this fixture is mentioned as a parameter of test"""
    browser = webdriver.Chrome(service=Service(executable_path='.chromedriver'))
    now = datetime.now()
    yield browser
    # browser.save_screenshot(f"screenshot_{now}.png")
    browser.quit()

@pytest.fixture()
def admin_login(browser):
    """fixture to login in with ADMIN TEST credentials;
       starts from opening login page and finishes on the Analytics page (which is a homepage by default)"""
    login_page = LoginPage(browser, Links.login_page)
    login_page.open_page()
    login_page.login(TestData.valid_login_credentials_admin[0])
