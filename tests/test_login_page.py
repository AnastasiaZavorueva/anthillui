#  file to collect tests created for login page

from pages.login_page import LoginPage
from config import Links
from tests.test_data import TestData
import pytest
import time


class TestLoginPage:

    @pytest.mark.parametrize("credentials", TestData.valid_login_credentials_admin)
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_with_valid(self, browser, credentials):
        login_page = LoginPage(browser, Links.login_page)
        login_page.login(credentials)
        time.sleep(2)
        assert browser.current_url == Links.analytics_page, f"Wrong result, expected to be on Analytics page"

    @pytest.mark.parametrize("invalid_credentials", TestData.invalid_login_credentials_admin)
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_with_invalid(self, browser, invalid_credentials):
        login_page = LoginPage(browser, Links.login_page)
        login_page.login(invalid_credentials)
        # time.sleep(2)
        assert browser.current_url == Links.login_page, f"Wrong result, expected to stay on Login page"
        assert login_page.login_error_message_shown(), f"Wrong result, no error message shown"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_navigation_elements(self, browser):
        login_page = LoginPage(browser, Links.login_page)

        assert login_page.forgot_password_link_exists()
        login_page.navigate_to_forgot_password()
        assert browser.current_url == Links.forgot_password, f"Wrong result, expected to be on Forgot Password page"
        login_page.open_page()

        assert login_page.remember_me_checkbox_exists(), f"Wrong result, no 'Remember me' checkbox found"
        login_page.check_remember_me()
        assert login_page.remember_me_checked(), f"Wrong result, 'Remember me' is not checked"
        login_page.check_remember_me()
        assert login_page.remember_me_unchecked(), f"Wrong result, 'Remember me' is still checked"

        assert login_page.create_account_link_exists()
        login_page.navigate_to_create_account()
        time.sleep(2)
        assert browser.current_url == Links.register_page, f"Wrong result, expected to be on Create an account page"
        login_page.open_page()

        #  AFTER DEVELOPING FUNCTIONALITY TO LOG IN WITH GOOGLE, FACEBOOK OR TWITTER ACCOUNT
        # this test could be updated with assertions
        # for page redirection after clicking on these buttons
        assert login_page.login_with_facebook_exists(), f"Wrong result, no button to log in with Facebook account found"
        assert login_page.login_with_google_exists(), f"Wrong result, no button to log in with Google account found"
        assert login_page.login_with_twitter_exists(), f"Wrong result, no button to log in with Twitter account found"
