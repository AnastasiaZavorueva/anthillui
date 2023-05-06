from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import CalendarPageLocators
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class CalendarPage(BasePage):

    # def main_elements_exist(self):
    #
    # def all_day_checkbox_checked(self):

    def navigate_to_create_event(self):
        hamburger_button = self.browser.find_element(*CalendarPageLocators.HAMBURGER_BUTTON)
        time.sleep(1)
        hamburger_button.click()
        time.sleep(2)
        add_event_button = self.browser.find_element(*CalendarPageLocators.ADD_EVENT_BUTTON)
        add_event_button.click()
        time.sleep(2)

    def create_event(self, event_data):
        event_title_field = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[1]
        event_title_field.click()
        time.sleep(1)
        event_title_field.send_keys(event_data["title"])
        time.sleep(1)

        event_type_field = self.browser.find_elements(*CalendarPageLocators.EVENT_TYPE_FIELD)[2]
        event_type_field.click()
        time.sleep(1)

        type_needed = event_data["type"]  # could be "event", "meeting", "personal", "task"
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

        save_button = self.browser.find_element(*CalendarPageLocators.SAVE_BUTTON)
        save_button.submit()
        time.sleep(3)

        # not developed yet - choosing participants (but this field exists only for the type of event "meeting")
        # participants_field = self.browser.find_element(*CalendarPageLocators.PARTICIPANTS_FIELD)
        # participants_field.click()
        # some_participant = self.browser.find_element(*CalendarPageLocators.RANDOM_PARTICIPANT)
        # some_participant.click()
        # somehow submit this input to move to the next field then

    # helper method to choose date and time on picker based on
    # specific timestamp that is passed as a parameter "date_time_to_set)
    # just be sure that the picker needed is already opened (done in create_even, where the helper method is used)
    def set_event_datetime(self, datetime_to_set):
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
            str(month_to_choose - 1))  # -1 because on the website January go under index 0, and so on
        # and converting the value to select into a string because it's type of data in HTML page

        all_days_of_selected_month = self.browser.find_elements(*CalendarPageLocators.ALL_DAYS_OF_SELECTED_MONTH)
        day_needed = all_days_of_selected_month[
            day_to_choose - 1]  # -1 because in the collection of web-elements (all_days_of_selected_month) the 1st day of the month goes under index 0, and so on
        day_needed.click()

        hour_input_field = self.browser.find_element(*CalendarPageLocators.EVENT_HOUR_FIELD)
        hour_input_field.click()
        hour_input_field.send_keys(hour_to_choose)

        minutes_input_field = self.browser.find_element(*CalendarPageLocators.EVENT_MINUTES_FIELD)
        minutes_input_field.click()
        minutes_input_field.send_keys(minutes_to_choose, Keys.RETURN)

    def event_in_calendar_exists(self, event_to_search):
        self.set_date_on_left_picker(event_to_search["start_datetime"])
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//body").click()  # to deactivate picker window, so it will be closed
        time.sleep(3)

        list_of_events_this_month_button = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(CalendarPageLocators.LIST_ALL_MONTH_EVENTS_BUTTON))
        actions = ActionChains(self.browser)
        actions.move_to_element(list_of_events_this_month_button).perform()
        list_of_events_this_month_button.click()
        time.sleep(2)

        all_events_detected_in_list = self.parce_all_month_events()  # its a dictionary with tuples inside for each event detected
        date_to_search = event_to_search["start_datetime"].strftime("%Y-%m-%d")
        title_to_search = event_to_search["title"]
        for event in all_events_detected_in_list:
            event_title = event["title"]
            event_date = event["date"]
            if (event_date == date_to_search) and (event_title == title_to_search):
                return True
        return False

    # helper method (for the method event_in_calendar_exists)
    #  chooses date on left picker, so that it automatically shows all events in specific month
    def set_date_on_left_picker(self, datetime_to_set):
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

        all_days_of_selected_month = self.browser.find_elements(*CalendarPageLocators.ALL_MONTH_DAYS_SHOWN)
        day_needed = all_days_of_selected_month[day_to_choose - 1]
        day_needed.click()

    # helper method (for the method event_in_calendar_exists)
    # the list with all month events should be open before running it
    def parce_all_month_events(self):
        #  to check that there is an element with the title of event we search
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
        all_event_titles_this_month = self.browser.find_elements(*CalendarPageLocators.ALL_EVENT_TITLES_IN_MONTH)
        for event in all_event_titles_this_month:
            if event.text == event_data["title"]:
                time.sleep(2)
                event.click()
                time.sleep(2)
                return

    #  for running this method specific event should be already opened!
    def get_event_title(self):
        event_title_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[1].get_attribute(
            "value")
        return event_title_shown

    #  for running this method specific event should be already opened!
    def get_event_type(self):
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

    #  for running this method specific event should be already opened!
    def get_event_start_date(self):
        event_start_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[3].get_attribute(
            "value")
        event_start_date_shown = event_start_shown[0:10]
        return event_start_date_shown

    #  for running this method specific event should be already opened!
    def get_event_end_date(self):
        event_end_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[4].get_attribute(
            "value")
        event_end_date_shown = event_end_shown[0:10]
        return event_end_date_shown

    #  for running this method specific event should be already opened!
    def get_event_place(self):
        event_place_shown = self.browser.find_elements(*CalendarPageLocators.EVENT_FORM_TEXT_FIELDS)[5].get_attribute(
            "value")
        return event_place_shown

    #  for running this method specific event should be already opened!
    #  returns event description
    def get_event_desc(self):
        event_desc_shown = self.browser.find_element(*CalendarPageLocators.DESCRIPTION_FIELD).get_attribute("value")
        return event_desc_shown
