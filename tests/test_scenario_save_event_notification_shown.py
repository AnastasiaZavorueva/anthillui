#   test scenario ID 7: 1) starts to create a new event in calendar with the title, type, start datetime,
#   end datetime, place and description provided in dictionary "event_data" as a parameter
#   2) taps outside the form with event data entered before
#   3) checks that the notification window is shown after such action
#   (with 2 options: to save event or cancel process of creation)

import time
import pytest
from config import Links
from pages.calendar_page import CalendarPage
from pages.dasboard_page import DashboardPage
from tests.test_data import TestData
import allure
from allure_commons.types import AttachmentType


class TestScenarioSaveEventNotificationShown:
    @pytest.mark.parametrize("event_data", TestData.event_data)
    def test_start_creating_event_in_calendar(self, browser, admin_login, event_data):
        dashboard_page = DashboardPage(browser, Links.dashboard_page)
        time.sleep(1)
        dashboard_page.navigate_to_calendar()

        calendar_page = CalendarPage(browser, Links.calendar_page)
        calendar_page.navigate_to_create_event()
        calendar_page.create_event(event_data)

        # TODO: test creation is on pause - feature doesn't work for now


