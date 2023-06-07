#   test scenario ID 6: 1) creates a new event in calendar with the title, type, start datetime,
#   end datetime, place and description provided in dictionary "event_data" as a parameter
#   2) then opens the event created
#   3) and delete it

import time
import pytest
from config import Links
from pages.calendar_page import CalendarPage
from pages.dasboard_page import DashboardPage
from locators.calendar_page_locators import CalendarPageLocators
from tests.test_data import TestData
import allure
from allure_commons.types import AttachmentType


class TestScenarioDeleteEventInCalendar:

    @pytest.mark.parametrize("event_data", TestData.event_data)
    def test_delete_event_in_calendar(self, browser, admin_login, event_data):
        dashboard_page = DashboardPage(browser, Links.dashboard_page)
        time.sleep(1)
        dashboard_page.navigate_to_calendar()

        calendar_page = CalendarPage(browser, Links.calendar_page)
        calendar_page.navigate_to_create_event()
        calendar_page.create_event(event_data)
        calendar_page.save_event_created()

        calendar_page.choose_date_on_left_picker(event_data["start_datetime"])
        calendar_page.open_event(event_data)
        time.sleep(2)

        #  before deleting the event method delete_event verifies that we opened the right event to delete
        # (by title, place, description, type, start and end dates)
        calendar_page.delete_event(event_data)
        time.sleep(2)

        hamburger_button = browser.find_element(*CalendarPageLocators.HAMBURGER_BUTTON)
        hamburger_button.click()  # rewrite methods. so no locators used in tests
        time.sleep(3)
        assert calendar_page.event_in_calendar_exists(event_data) is False


    # edit methods in calendar_page, so it wouldn't be nessesary to keep specific state of page
    # (like left picker is opened and so on)

    # freeze reqs of the project - done

    # connect allure reports to the project -done

    # run tests and push changes on git

    # add readme on git

    # create a map of the project - done