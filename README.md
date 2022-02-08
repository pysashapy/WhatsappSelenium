# pyWAppSel
[![image](https://flat.badgen.net/badge/release/1.0.4/blue)](https://github.com/pysashapy/pyWAppSel)
[![image](https://flat.badgen.net/badge/python/3.10/orange)](https://www.python.org/downloads/release/python-3102/)

[pyWAppSel](https://pypi.org/project/pyWAppSel/) is a Python library with various helpful features.
It's easy-to-use and does not require you to do any additional setup.

# Whatsapp
Package [pysashapy/pyWAppSel](https://github.com/pysashapy/pyWAppSel) implements the WhatsApp Web API to provide a clean interface for developers. The official WhatsApp Business API was released in August 2018. You can check it out [here](https://www.whatsapp.com/business/api).

## Installation and Supported Versions

pyWAppSel is available on PyPi:

```bash
pip install pyWAppSel
```

pyWAppSel officially supports Python 3.8+.

## Cloning the Repository

```bash
git clone https://github.com/pysashapy/pyWAppSel.git
pip install selenium webdriver_manager
```

## Features

- Sending Message to a WhatsApp Group or Contact
- Sending Image/Video/Document/Sticker/ to a WhatsApp Group or Contact
- Downloading Videos/Photos/Sticker/Voice Message from Group and Contact
- Listening to one or all Group or Contact
- get a qr code link for authorization from the console
- Install and Use

## Usage

### Quick Start
```py
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
```

For more Examples and Functions, have a look at the [Example](https://github.com/pysashapy/pyWAppSel/tree/main/examples).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its
affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk.

## License

Apache Software License (Apache 2.0).
For more information see [this](https://github.com/pysashapy/pyWAppSel/blob/main/LICENSE)

NOTICE [this](https://github.com/pysashapy/pyWAppSel/blob/main/NOTICE)