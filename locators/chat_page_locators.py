from selenium.webdriver.common.by import By


class ChatPageLocators:
    START_CHAT_BUTTON = (By.CSS_SELECTOR, "p.cursor-pointer")

    USERS_SEARCH_FIELD = (By.CSS_SELECTOR, "div.chat-list-header input")

    # returns span elements that contains contacts shown in chat
    # specific contact can be chosen from it by checking text (name) inside it:
    CHATS_SHOWN = (By.CSS_SELECTOR, "li.chat-contact div.overflow-hidden span:nth-child(1)")
    MESSAGE_INPUT_FIELD = (By.CSS_SELECTOR, "form.chat-log-message-form textarea[placeholder='Введите сообщение...']")
    MESSAGE_FORM = (By.CSS_SELECTOR, 'form')

    # locator returns collection of elements - messages from one chat that is opened
    # to get text of specific chat message (for example, text of the last message) in the collection:
    # last_message = list_of_elements[-1].text'
    ALL_CHAT_MESSAGES_SHOWN = (By.CSS_SELECTOR, 'div.chat-log p.chat-content')

    CREATE_GROUP_BUTTON = (By.CSS_SELECTOR, 'div.chat-list-header button.addGroup')
    # HIDE_LEFT_CHAT_MENU =
    SELECT_GROUP_PARTICIPANTS_FIELD = (By.CSS_SELECTOR, 'div.v-field__input')

    # returns collection of elements that can be used to select
    # specific user by his/her name (by 'element.text')
    PARTICIPANTS_SHOWN_IN_DROPDOWN_TO_SELECT_FROM = (By.CSS_SELECTOR, 'div.v-overlay-container div.v-list-item-title')
    SAVE_GROUP_PARTICIPANTS_SELECTED = (By.CSS_SELECTOR, 'div form button:nth-child(3)')

    # to use this selector creation of chat group should be started
    CHAT_GROUP_CREATION_FORM = (By.CSS_SELECTOR, 'div form')

    NAME_OF_CHAT_OPENED = (By.CSS_SELECTOR, 'div.active-chat-header h6')
    PARTICIPANTS_NUMBER_INFO = (By.CSS_SELECTOR, 'div.active-chat-header h6 + span')
