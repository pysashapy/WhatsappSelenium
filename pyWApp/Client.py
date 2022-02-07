import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from . import getQrUrl, printQrUrl, elements
from .browser import Browser
from .types import selectors_types, MessageTypes, EventTypes


class WhatsApp(Browser):
    def __init__(self, path_download=''):
        Browser.__init__(self, path_download=path_download)
        self.BASE_URL = 'https://web.whatsapp.com/'
        self.browser.get(self.BASE_URL)

    def isLogin(self, wait_time=100):
        element = self.getWaitElement(self.getWait(wait_time), elements.ACCOUNT_ICON)
        return bool(element)

    def login(self, wait_reload=1, wait_qr_code=1) -> bool:
        last_qr = ""
        wait_reload = self.getWait(wait_reload)
        wait_qr_code = self.getWait(wait_qr_code)

        while True:
            self.reloadQr(wait_reload)

            qr_data = self.getQrData(wait_qr_code)
            if qr_data != last_qr:
                printQrUrl(getQrUrl(qr_data))
                last_qr = qr_data

            if self.isLogin(1):
                return True

    def reloadQr(self, wait):
        reload_qr_code = self.getWaitElement(wait, elements.LOGIN_RELOAD_QR)
        if reload_qr_code:
            reload_qr_code.click()

    def getQrData(self, wait):
        qr_code = self.getWaitElement(wait, elements.LOGIN_QR)
        if qr_code is not None:
            return qr_code.get_attribute("data-ref")

    def logout(self):
        self.browser.find_element(*elements.ACCOUNT_MENU).click()
        self.browser.find_element(*elements.ACCOUNT_MENU_EXIT).click()

    def close(self):
        self.browser.close()


class Messenger:
    def __init__(self, client: WhatsApp, wait_chat=5, wait_choose_file=5, wait_attached=5, wait_get_message=5):
        self.client = client
        self.browser = client.browser
        self.wait_open_chat = self.client.getWait(wait_chat)
        self.wait_choose_file = self.client.getWait(wait_choose_file)
        self.wait_attached = self.client.getWait(wait_attached)
        self.wait_get_message = self.client.getWait(wait_get_message)

    def getChatsFromBook(self):
        self.browser.find_element(*elements.ACCOUNT_NEW_CHAT_MENU).click()
        names_chats = []
        for name in self.browser.find_elements(*elements.ACCOUNT_NEW_CHAT_ALL_USERS_NAMES):
            names_chats.append(name.text)
        self.browser.find_element(*elements.ACCOUNT_NEW_CHAT_MENU_EXIT).click()

        return names_chats

    def getAllChats(self):
        chats = self.browser.find_elements(*elements.ACCOUNT_CHATS)
        names_chats = []
        for chat in chats:
            names_chats.append(chat.find_element(*elements.ACCOUNT_CHAT_NAME).text)
        return names_chats

    def getFirstChat(self):
        element = self.browser.find_element(*elements.FIND_NEW_CHAT_MESSAGES)
        name_chat = element.find_element(*elements.GET_NAME_NEW_CHAT).text
        return name_chat, element

    def openChat(self, name, element=None):
        inp_ = self.client.getWaitElement(self.wait_open_chat, elements.FIND_SELECTED_CHAT)
        inp_.send_keys(name, Keys.ENTER)
        return Chat(name, element, self)


class Chat:
    def __init__(self, name: str, element: WebElement, messenger: Messenger):
        self.name = name
        self.element = element
        self.messenger = messenger
        self.browser = self.messenger.browser
        self.client = self.messenger.client
        if element is not None:
            self.id = self.element.id

    def getFirstMessageIn(self):
        message = self.client.getWaitElements(self.messenger.wait_get_message, elements.GET_MESSAGES)
        if message:
            return Message(message[-1], self)
        else:
            return False

    def sendText(self, text):
        inp_ = self.browser.find_element(*elements.CHAT_ENTRY_MESSAGE)
        inp_.send_keys(text, Keys.ENTER)

    def sendFile(self, path_file, type_attachment):
        self.browser.find_element(*elements.CHAT_ADD_FILE).click()
        self.client.getWaitElement(self.messenger.wait_choose_file, type_attachment).send_keys(
            os.path.realpath(path_file))
        self.client.getWaitElement(self.messenger.wait_attached, elements.CHAT_SEND_FILE).click()

    def sendFiles(self, paths_files, type_attachment, delay=0):
        for path in paths_files:
            self.sendFile(path, type_attachment)
            time.sleep(delay)


class Message:
    data = None

    def __init__(self, element: WebElement, chat: Chat):
        self.chat_window = chat
        self.element = element
        self.id = self.element.id

        self.chat_name = chat.name
        self.user_name = chat.name
        self.type = ''
        self.text = ''

        self.setType()
        self.setUser()

    def setType(self):
        for selector_type in selectors_types:
            data = self.element.find_elements(*selector_type[0])
            if data:
                self.data = data[0]
                self.type = selector_type[1]

                if self.type == MessageTypes.TEXT:
                    self.setText()
                break

    def setText(self):
        self.text = self.data.text

    def setUser(self):
        name = self.element.find_elements(*elements.SELECTOR_USER)
        if name:
            self.user_name = name[0]

    def download(self):
        self.element.find_element(*elements.CHAT_MENU).click()
        self.element.find_element(*elements.CHAT_MENU_SELECTED_MESSAGES).click()
        self.element.click()
        self.element.find_element(*elements.CHAT_BOTTOM_MENU_MESSAGES_DOWNLOAD).click()

    def isDownloaded(self):
        return bool(self.chat_window.browser.find_elements(*elements.WAIT_DOWNLOAD))


class LongPoll:
    def __init__(self, client: Messenger, listing_chat=False, chat_name=''):
        self.client = client

        self.chat_name = chat_name
        self.listingChat = listing_chat
        self.chat = None

        if listing_chat:
            self.setListingChat(self.chat_name)

    def setListingChat(self, chat_name):
        self.chat = self.client.openChat(chat_name)
        self.listingChat = True
        self.chat_name = chat_name

    def start(self, delay=0.01, wait=1000):
        last_time = time.time()

        last_chat_id = ''
        last_message_id = ''

        while True:
            if not self.listingChat:
                chat_name, element = self.client.getFirstChat()
                if last_chat_id != element.id:
                    self.chat = self.client.openChat(chat_name, element)
                    last_chat_id = element.id

            message = self.chat.getFirstMessageIn()
            if message:
                if last_message_id != message.id:  # New Message
                    last_time = time.time()
                    last_message_id = message.id
                    yield message, EventTypes.NEW_MESSAGES
            else:
                if time.time() - last_time >= wait:
                    break
            time.sleep(delay)
