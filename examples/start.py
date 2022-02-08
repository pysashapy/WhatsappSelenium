from pyWAppSel.types import FileTypes
from pyWAppSel.Client import WhatsApp, Messenger

# start selenium and auth
client = WhatsApp(path_download='full path to downloaded files')

# auth
if not client.isLogin(wait_time=100):
    client.login()

# open chat, get names chats, get first chat
messenger = Messenger(client=client)


# if the "chat name" is incomplete then the first chat in the search will be selected
chat = messenger.openChat(name='CHAT NAME')

# send text message
chat.sendText(text='Hello, world!')
# send photo
chat.sendFile(path_file='data/test.jpg', type_attachment=FileTypes.PHOTO_VIDEO)
# send video
chat.sendFile(path_file='data/test.mp4', type_attachment=FileTypes.PHOTO_VIDEO)
# send document
chat.sendFile(path_file='data/test.jpg', type_attachment=FileTypes.DOCUMENT)
# send sticker
chat.sendFile(path_file='data/test.jpg', type_attachment=FileTypes.STICKER)

# returns a sheet with the name of the chats that have been added to the number book
names_chats = messenger.getChatsFromBook()
print(names_chats)

# returns a list with the names of all chats
names_all_chats = messenger.getAllChats()
print(names_all_chats)

# close WebDriver
client.close()
