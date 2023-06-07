from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.calendar_page_locators import CalendarPageLocators
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class CalendarPage(BasePage):
    def navigate_to_create_event(self):
        """redirects user from Calendar page (which should already be opened)
        to the create event form"""
        hamburger_button = self.browser.find_element(*CalendarPageLocators.HAMBURGER_BUTTON)
        time.sleep(1)
        hamburger_button.click()
        time.sleep(2)
        add_event_button = self.browser.find_element(*CalendarPageLocators.ADD_EVENT_BUTTON)
        add_event_button.click()
        time.sleep(2)

    def create_event(self, event_data):
        """fill outs the form (which should already be opened by method navigate_to_create_event)
         to the create an event with the data provided in event_data parameter;
         :param: event_data should be a dictionary with the next keys and its values inside:
         - "title" - should be string
         - "type" - should be string (either "event", "meeting", "personal", or "task")
         - "start_datetime" - should be a datetime stamp
         - "end_datetime" - should be a datetime stamp
         - "place" - should be string
         - "desc" - description of event, should be string"""
        event_title_field = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[1]
        event_title_field.click()
        time.sleep(1)
        event_title_field.send_keys(event_data["title"])
        time.sleep(1)

        event_type_field = self.browser.find_elements(*CalendarPageLocators.EVENT_TYPE_FIELD)[2]
        event_type_field.click()
        time.sleep(1)

        type_needed = event_data["type"]
        event_type_to_choose = self.browser.find_element(*CalendarPageLocators.EVENT_TYPES[type_needed])
        event_type_to_choose.click()

        start_date_and_time_picker = self.browser.find_elements(*CalendarPageLocators.EVENT_DATE_AND_TIME_FIELDS)[0]
        start_date_and_time_picker.click()
        self.set_event_datetime(event_data["start_datetime"])
        time.sleep(2)

        end_date_and_time_picker = self.browser.find_elements(*CalendarPageLocators.EVENT_DATE_AND_TIME_FIELDS)[1]
        time.sleep(1)
        end_date_and_time_picker.click()
        self.set_event_datetime(event_data["end_datetime"])
        time.sleep(1)

        place_field = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[5]
        place_field.click()
        time.sleep(1)
        place_field.send_keys(event_data["place"])

        description_field = self.browser.find_element(*CalendarPageLocators.DESCRIPTION_FIELD)
        description_field.click()
        description_field.send_keys(event_data["desc"])
        time.sleep(1)

        # TODO: choosing participants (this field exists only for the type of event "meeting")
        # participants_field = self.browser.find_element(*CalendarPageLocators.PARTICIPANTS_FIELD)
        # participants_field.click()
        # some_participant =
        # some_participant.click()
        # somehow submit this input to move on to the next field

    def save_event_created(self):
        save_button = self.browser.find_element(*CalendarPageLocators.SAVE_BUTTON)
        save_button.submit()
        time.sleep(3)

    def set_event_datetime(self, datetime_to_set):
        """helper method (used in create_event method) to choose
        specific date and time on picker while creating an event
        ! the form for creating event should already be opened
        :param datetime_to_set: should be a timestamp"""
        day_to_choose = datetime_to_set.day
        month_to_choose = datetime_to_set.month
        year_to_choose = datetime_to_set.year
        hour_to_choose = datetime_to_set.hour
        minutes_to_choose = datetime_to_set.minute

        year_shown_in_form = self.browser.find_element(*CalendarPageLocators.CURRENT_YEAR_SHOWN).get_attribute("value")
        while int(year_shown_in_form) != year_to_choose:
            next_month_arrow_button = self.browser.find_element(*CalendarPageLocators.NEXT_MONTH_ARROW_BUTTON)
            next_month_arrow_button.click()
            year_shown_in_form = self.browser.find_element(*CalendarPageLocators.CURRENT_YEAR_SHOWN).get_attribute(
                "value")

        month_dropdown = Select(self.browser.find_element(*CalendarPageLocators.MONTH_DROPDOWN_LIST))
        month_dropdown.select_by_value(
            str(month_to_choose - 1))  # -1 because on the website January goes under index 0, and so on
        # and then converts the value to select into a string, because that's the type of data in HTML elements

        all_days_of_selected_month = self.browser.find_elements(*CalendarPageLocators.ALL_DAYS_OF_SELECTED_MONTH)
        day_needed = all_days_of_selected_month[
            day_to_choose - 1]  # -1 because in the collection of web elements (all_days_of_selected_month)
        # the 1st day of the month goes under index 0, and so on
        day_needed.click()

        hour_input_field = self.browser.find_element(*CalendarPageLocators.EVENT_HOUR_FIELD)
        hour_input_field.click()
        hour_input_field.send_keys(hour_to_choose)

        minutes_input_field = self.browser.find_element(*CalendarPageLocators.EVENT_MINUTES_FIELD)
        minutes_input_field.click()
        minutes_input_field.send_keys(minutes_to_choose, Keys.RETURN)

    def event_in_calendar_exists(self, event_to_search):
        """checks whether some event (with specific title and start date) is present on Calendar page
        ! the left date picker should already be opened
        :param: event_data - should be a dictionary with the next keys and its values inside:
         - "title" - should be string
         - "type" - should be string (either "event", "meeting", "personal", or "task")
         - "start_datetime" - should be a datetime stamp
         - "end_datetime" - should be a datetime stamp
         - "place" - should be string
         - "desc" - description of event, should be a string
        :return: True (if event was found in Calendar) or False"""
        self.choose_date_on_left_picker(event_to_search["start_datetime"])
        time.sleep(2)

        # self.browser.find_element(By.XPATH, "//body").click()  # to deactivate picker window, so it will be closed
        # time.sleep(3)
        #
        # list_of_events_this_month_button = WebDriverWait(self.browser, 10).until(
        #     expected_conditions.element_to_be_clickable(CalendarPageLocators.LIST_ALL_MONTH_EVENTS_BUTTON))
        # actions = ActionChains(self.browser)
        # actions.move_to_element(list_of_events_this_month_button).perform()
        # list_of_events_this_month_button.click()
        # time.sleep(2)

        all_events_detected_in_list = self.parce_all_month_events()  # list with dictionary for every event detected
        date_to_search = event_to_search["start_datetime"].strftime("%Y-%m-%d")
        title_to_search = event_to_search["title"]
        for event in all_events_detected_in_list:
            event_title = event["title"]
            event_date = event["date"]
            if (event_date == date_to_search) and (event_title == title_to_search):
                return True
        return False

    def choose_date_on_left_picker(self, datetime_to_set):
        """helper method (used in the method event_in_calendar_exists) for
        choosing date on left picker while navigating on Calendar page
        - so that the page is automatically updated with the list of all events in specific month;
        in the end of method picker window is closed, so the Calendar is shown in a whole
        ! left picker should already be opened to use this method
        :param datetime_to_set should be a datestamp"""
        day_to_choose = datetime_to_set.day
        month_to_choose = datetime_to_set.month
        year_to_choose = datetime_to_set.year

        year_shown_in_form = self.browser.find_element(*CalendarPageLocators.LEFT_PICKER_YEAR_SHOWN).get_attribute(
            "value")
        while int(year_shown_in_form) != year_to_choose:
            next_month_arrow_button = self.browser.find_element(*CalendarPageLocators.LEFT_PICKER_NEXT_MONTH_BUTTON)
            next_month_arrow_button.click()
            year_shown_in_form = self.browser.find_element(*CalendarPageLocators.LEFT_PICKER_YEAR_SHOWN).get_attribute(
                "value")

        month_dropdown = Select(self.browser.find_element(*CalendarPageLocators.LEFT_PICKER_MONTH_DROPDOWN))
        month_dropdown.select_by_value(str(month_to_choose - 1))

        all_days_of_selected_month = self.browser.find_elements(*CalendarPageLocators.LEFT_PICKER_ALL_MONTH_DAYS_SHOWN)
        day_needed = all_days_of_selected_month[day_to_choose - 1]
        day_needed.click()

        self.browser.find_element(By.XPATH, "//body").click()  # to deactivate picker window, so it will be closed
        time.sleep(3)

        list_of_events_this_month_button = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(CalendarPageLocators.LIST_ALL_MONTH_EVENTS_BUTTON))
        actions = ActionChains(self.browser)
        actions.move_to_element(list_of_events_this_month_button).perform()
        list_of_events_this_month_button.click()
        time.sleep(2)

    def parce_all_month_events(self):
        """helper method (used in event_in_calendar_exists) for
        parsing data from the table (where all events of specific month shown) into
        :return: a list with dictionary for every event detected
        (each dictionary contains keys "title" and "date" with its values in form of
        strings; date is represented as a string in this format: "YYYY-MM-DD")
        ! the list of all events in selected month should already be opened to run this method"""
        all_elements_in_list_of_events = self.browser.find_elements(*CalendarPageLocators.ALL_ROWS_IN_MONTH_EVENTS_LIST)
        results_with_event_date_and_title = []
        date = ""
        for element in all_elements_in_list_of_events:
            if element.get_attribute("data-date") is not None:
                date = element.get_attribute("data-date")
            else:
                title = element.find_element(By.CSS_SELECTOR, "a").text
                results_with_event_date_and_title.append({"date": date, "title": title})
        return results_with_event_date_and_title

    def open_event(self, event_data):
        """opens a specific event after detecting it by the title provided
        :param: event_data should be a dictionary with the next keys and its values inside:
        - "title" - should be string
        ! the page with the list of all events in specific month should already be opened"""
        # TODO: add event time check in case there are multiple events with the same title on the same day
        # (then add to :params: - "start_datetime" - should be a datetime stamp)
        all_event_titles_this_month = self.browser.find_elements(*CalendarPageLocators.ALL_EVENT_TITLES_IN_MONTH)
        for event in all_event_titles_this_month:
            if event.text == event_data["title"]:
                time.sleep(2)
                event.click()
                time.sleep(2)
                return

    # what about adding navigation to the list of all events in month in the beginning od method?
    # although by that the test event created could be automatically deleted

    # maybe methods to navigate to list of all month events?

    def get_event_title(self):
        """! for running this method a specific event should already be opened!
        :return: event_title_shown - string with the title of event found on page"""
        event_title_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[1].get_attribute(
            "value")
        return event_title_shown

    def get_event_type(self):
        """! for running this method a specific event should already be opened!
        :return: a string with the type of event found on page
        (could be either "event", "personal", "task", or "meeting" """
        event_type_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_TYPE_FIELD)[2].find_element(
            By.CSS_SELECTOR, 'span:not(.v-badge__badge)').text
        if event_type_shown == "Мероприятие":
            return "event"
        elif event_type_shown == "Личное":
            return "personal"
        elif event_type_shown == "Встеча":
            return "meeting"
        elif event_type_shown == "Задача":
            return "task"

    def get_event_start_date(self):
        """! for running this method a specific event should already be opened!
        :return: event_start_date_shown - a string with the start date of event found on page
        (in form "YYYY-MM-DD")"""
        event_start_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[3].get_attribute(
            "value")
        event_start_date_shown = event_start_shown[0:10]
        return event_start_date_shown

    def get_event_end_date(self):
        """! for running this method a specific event should already be opened!
        :return: event_end_date_shown - a string with the end date of event found on page
        (in form "YYYY-MM-DD")"""
        event_end_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[4].get_attribute(
            "value")
        event_end_date_shown = event_end_shown[0:10]
        return event_end_date_shown

    def get_event_place(self):
        """! for running this method a specific event should already be opened!
        :return: event_place_shown - a string with the event place found on page"""
        event_place_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[5].get_attribute(
            "value")
        return event_place_shown

    def get_event_desc(self):
        """! for running this method a specific event should already be opened!
        :return: event_desc_shown - a string with the event description found on page"""
        event_desc_shown = self.browser.find_element(*CalendarPageLocators.DESCRIPTION_FIELD).get_attribute("value")
        return event_desc_shown

    def delete_event(self, event_data):
        """! for running this method a specific event should already be opened!
        - firstly checks whether the event opened is the same as we want to delete
         (by title, place, description, type, start and end dates)
        - and then deletes this event
         :param: event_data - should be a dictionary with the next keys and its values inside:
         - "title" - should be string
         - "type" - should be string (either "event", "meeting", "personal", or "task")
         - "start_datetime" - should be a datetime stamp
         - "end_datetime" - should be a datetime stamp
         - "place" - should be string
         - "desc" - description of event, should be a string """
        delete_event_button = self.browser.find_element(*CalendarPageLocators.DELETE_EVENT_BUTTON)
        if (self.get_event_title() == event_data["title"] and
                self.get_event_place() == event_data["place"] and
                self.get_event_desc() == event_data["desc"] and
                self.get_event_type() == event_data["type"] and
                self.get_event_start_date() == event_data["start_datetime"].strftime("%d.%m.%Y") and
                self.get_event_end_date() == event_data["end_datetime"].strftime("%d.%m.%Y")):
            delete_event_button.click()

    # def main_elements_exist(self):

    # def all_day_checkbox_checked(self):

    def click_outside_create_event_form(self):
        self.browser.click
