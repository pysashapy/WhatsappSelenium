from pyWAppSel.Client import WhatsApp, Messenger, LongPoll
from pyWAppSel.types import EventTypes, MessageTypes

# start selenium and auth
client = WhatsApp(path_download='full path to downloaded files')

# auth
if not client.isLogin(wait_time=100):
    client.login()

# open chat, get names chats
messenger = Messenger(client=client)

# listening for bot
longpoll = LongPoll(messenger=messenger)

chat = None

# start listening chats
for element, type_ in longpoll.listen(delay=0.1, wait=100):
    if type_ == EventTypes.NEW_CHAT:
        chat = element

    if type_ == EventTypes.NEW_MESSAGES:
        if element.type == MessageTypes.TEXT:
            if element.text == "/start":
                chat.sendText(text=f'Hello, {element.user_name}!')
        elif element.type not in (MessageTypes.TEXT, MessageTypes.UNKNOWN):
            path_file = element.download(auto_rename=True, wait=5)
            print(path_file)
# close WebDriver
client.close()
