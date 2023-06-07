#   test scenario ID 3: 1) creates a new event in calendar with the title, type, start datetime,
#   end datetime, place and description provided in dictionary "event_data" as a parameter
#   2) then checks that the event created is shown in calendar
#   3) and then opens the event to check that all event data shown is the same as was provided

import time
import pytest
from config import Links
from pages.calendar_page import CalendarPage
from pages.dasboard_page import DashboardPage
from tests.test_data import TestData
import allure
from allure_commons.types import AttachmentType



class TestScenarioCreateEventInCalendar:

    @pytest.mark.parametrize("event_data", TestData.event_data)
    def test_create_event(self, browser, event_data, admin_login):
        dashboard_page = DashboardPage(browser, Links.dashboard_page)
        time.sleep(1)
        dashboard_page.navigate_to_calendar()

        calendar_page = CalendarPage(browser, Links.calendar_page)
        calendar_page.navigate_to_create_event()
        calendar_page.create_event(event_data)
        calendar_page.save_event_created()

        assert calendar_page.event_in_calendar_exists(event_data) is True
        time.sleep(1)

        calendar_page.open_event(event_data)
        time.sleep(2)

        event_title_shown = calendar_page.get_event_title()
        assert event_title_shown == event_data["title"]

        event_place_shown = calendar_page.get_event_place()
        assert event_place_shown == event_data["place"]

        event_desc_shown = calendar_page.get_event_desc()
        assert event_desc_shown == event_data["desc"]

        event_type_shown = calendar_page.get_event_type()
        assert event_type_shown == event_data["type"]

        event_start_date_shown = calendar_page.get_event_start_date()
        start_date_to_compare_with = event_data["start_datetime"].strftime("%d.%m.%Y")
        assert event_start_date_shown == start_date_to_compare_with

        event_end_date_shown = calendar_page.get_event_end_date()
        end_date_to_compare_with = event_data["end_datetime"].strftime("%d.%m.%Y")
        assert event_end_date_shown == end_date_to_compare_with


