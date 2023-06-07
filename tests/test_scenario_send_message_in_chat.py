# test scenario ID 8: 1) send a message (provided) to a specific user
# (that already exists in the system and is selected by his/her name)
# 2) check that the message sent is now shown as the last message in the chat with this user

import allure
from pages.chat_page import ChatPage
from pages.dasboard_page import DashboardPage
from config import Links
import time
from tests.test_data import TestData
import pytest


class TestScenarioSendMessageInChat:

    @allure.feature('chat')
    @allure.story('send_a_message_to_a_specific_user_in_chat')
    @allure.severity('critical')
    @pytest.mark.regression
    @pytest.mark.parametrize("username_and_message_to_send", TestData.user_and_message_to_send)
    def test_send_message_to_specific_user_in_chat(self, browser, admin_login, username_and_message_to_send):
        dashboard_page = DashboardPage(browser, Links.dashboard_page)
        time.sleep(1)
        dashboard_page.navigate_to_chats()

        chat_page = ChatPage(browser, Links.chats_page)
        chat_page.open_chat_with_spec_username(username_and_message_to_send["username"])

        chat_page.type_message(username_and_message_to_send["message"])
        chat_page.send_message()

        name_of_the_chat_opened = chat_page.get_name_of_chat_opened()
        assert name_of_the_chat_opened == username_and_message_to_send["username"], f"Wrong result (expected name of " \
                                                                                    f"the chat: \'{username_and_message_to_send['username']}\', actual result: {name_of_the_chat_opened}"

        assert chat_page.message_is_shown_as_the_last_in_chat_opened(
            username_and_message_to_send[
                "message"]), f"Wrong result (expected: the message is shown as the last in the chat, actual: not " \
                             f"shown as the last)"

        # should we add verification of time sending message?
        # should we check whether the last message sent is shown in the preview of the chat?
        # should we open the chat again and verify the same result of sending message? or it's senseless
