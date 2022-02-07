from . import elements
from .elements import CHAT_ADD_FILE_PHOTO_VIDEO, CHAT_ADD_FILE_STICKER, CHAT_ADD_FILE_DOCUMENT


class EventTypes:
    NEW_MESSAGES = "new message"
    NEW_CHAT = "new chat"
    UNKNOWN = "unknown"


class MessageTypes:
    TEXT = "text"
    PHOTO = "photo"
    VIDEO = "video"
    FILE = "file"
    STICKER = "sticker"
    VOICE = "voice"
    DELETE_MESSAGE = "delete message"

    UNKNOWN = "unknown"


class FileTypes:
    PHOTO_VIDEO = CHAT_ADD_FILE_PHOTO_VIDEO
    STICKER = CHAT_ADD_FILE_STICKER
    DOCUMENT = CHAT_ADD_FILE_DOCUMENT


selectors_types = [
    [elements.SELECTOR_TEXT, MessageTypes.TEXT],
    [elements.SELECTOR_PHOTO, MessageTypes.PHOTO],
    [elements.SELECTOR_FILE, MessageTypes.FILE],
    [elements.SELECTOR_VIDEO, MessageTypes.VIDEO],
    [elements.SELECTOR_STICKER, MessageTypes.STICKER],
    [elements.SELECTOR_VOICE, MessageTypes.VOICE],
    [elements.SELECTOR_DELETE_MESSAGE, MessageTypes.DELETE_MESSAGE],
    [None, MessageTypes.UNKNOWN]
]
