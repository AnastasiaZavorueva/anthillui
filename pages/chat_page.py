from pages.base_page import BasePage
import time
from locators.chat_page_locators import ChatPageLocators


class ChatPage(BasePage):

    def expand_chats(self):
        """used in case of small browser window
         when only the button "Start dialog" is shown in the center of the page Chats"""
        start_chat_button = self.browser.find_element(*ChatPageLocators.START_CHAT_BUTTON)
        start_chat_button.click()
        time.sleep(2)

    # TODO: method collapse_chats

    def open_chat_with_spec_username(self, username):
        """finds a specific user (by the name provided) and opens chat with him/her
        :param:
        - "username" - should be a string containing user's name to open chat with
        (in form "LastName FirstName"), user should already exist in the system"""
        users_search_field = self.browser.find_element(*ChatPageLocators.USERS_SEARCH_FIELD)
        users_search_field.click()
        users_search_field.send_keys(username)
        time.sleep(3)
        chats_shown = self.browser.find_elements(*ChatPageLocators.CHATS_SHOWN)
        for chat in chats_shown:
            if chat.text == username:
                chat.click()
                time.sleep(2)
                break

    def type_message(self, message):
        """types a message (provided) in a chat that is already opened
        :param:
        - message - should be a string (with message to send)"""
        message_input_field = self.browser.find_element(*ChatPageLocators.MESSAGE_INPUT_FIELD)
        message_input_field.send_keys(message)

    def send_message(self):
        """sends a message
        ! - specific chat should already be opened (by using the method 'open_chat_with_spec_username')
        ! - the message to send should already be typed (by using the method 'type_message')"""
        message_form = self.browser.find_element(*ChatPageLocators.MESSAGE_FORM)
        message_form.submit()
        time.sleep(2)

    def message_is_shown_as_the_last_in_chat_opened(self, message_to_find):
        """checks that the message (provided) is shown as the last message in chat opened
        :param
        - "message_to_find" - should be a string with a message to look for
        :return: boolean"""
        messages_in_chat_shown = self.browser.find_elements(*ChatPageLocators.ALL_CHAT_MESSAGES_SHOWN)
        last_message_in_chat = messages_in_chat_shown[len(messages_in_chat_shown) - 1]
        if last_message_in_chat.text == message_to_find:
            return True
        return False

    def number_of_chats_shown(self):
        """counts number of chats shown in the left part of the page Chats
        :return: int with the number of chats detected"""
        chats_shown = self.browser.find_elements(*ChatPageLocators.CHATS_SHOWN)
        return len(chats_shown)

    def open_chat_group_creation(self):
        """clicks on the button (at the top of chats list) to start creating group in chats"""
        create_group_button = self.browser.find_element(*ChatPageLocators.CREATE_GROUP_BUTTON)
        create_group_button.click()
        time.sleep(2)

    def open_dropdown_with_participants_to_chose(self):
        """activates the field and opens dropdown list
        used to select participants for chat group"""
        select_group_participants_field = self.browser.find_element(*ChatPageLocators.SELECT_GROUP_PARTICIPANTS_FIELD)
        select_group_participants_field.click()
        time.sleep(3)

    def select_participant_for_chat_group(self, user_name):
        """selects user (by the name provided) as a participant of a chat group
        ! before using this method the dropdown list of all possible participants should be
        opened by using another method 'open_dropdown_with_participants_to_chose
        ! can be used to select multiple users (but for that the method should be called multiple times
        with different users' names)
        :param:
        - 'username' - should be a string with a user's name to select (in the form 'LastName FirstName')"""
        participants_shown_in_dropdown_to_select_from = self.browser.find_elements(
            *ChatPageLocators.PARTICIPANTS_SHOWN_IN_DROPDOWN_TO_SELECT_FROM)
        for participant in participants_shown_in_dropdown_to_select_from:
            if participant.text == user_name:
                participant.click()
        time.sleep(1)

    def save_participants_selected_for_group_chat(self):
        """saves participants for a new group in chat (selected before by
        another method - 'select_participant_for_chat_group')
        - ! this particular method doesn't save the group itself yet"""
        save_participants_button = self.browser.find_element(*ChatPageLocators.SAVE_GROUP_PARTICIPANTS_SELECTED)
        save_participants_button.click()
        time.sleep(2)

        # OR
        # participants_selection_form = self.browser.find_element(*ChatPageLocators.CHAT_GROUP_CREATION_FORM)
        # participants_selection_form.submit()

    def save_group(self):
        """saves a new group in chat (after selecting group participants by other methods
        (and optional group title and icon)"""
        save_group_button = self.browser.find_element(*ChatPageLocators.SAVE_GROUP_PARTICIPANTS_SELECTED)
        save_group_button.click()
        time.sleep(2)

        # OR
        # group_creation_form = self.browser.find_element(*ChatPageLocators.CHAT_GROUP_CREATION_FORM)
        # group_creation_form.submit()

    def get_name_of_chat_opened(self):
        """returns the last message shown in specific chat
        ! specific chat should already be opened to use this method
        :return
        - string with the last message shown in the chat opened"""
        name_shown = self.browser.find_element(*ChatPageLocators.NAME_OF_CHAT_OPENED)
        return name_shown.text

    def get_number_of_group_chat_participants(self):
        """! specific group chat should already be opened to use this method
        :return: int - number of participants shown"""
        participants_number_info_element = self.browser.find_element(*ChatPageLocators.PARTICIPANTS_NUMBER_INFO)
        all_info_from_element = participants_number_info_element.text
        number_shown = int(all_info_from_element.split()[0])
        return number_shown

    # def correct_title_and_participants_number_shown(self):

