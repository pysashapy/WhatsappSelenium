from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

'''=============AUTH============='''

LOGIN_QR = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div')
LOGIN_RELOAD_QR = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div/span/button')
LOGIN_USE_HERE = (By.XPATH, '//span[@data-testid="default-user"]')

'''=========TOP NEW CHAT========='''

ACCOUNT_NEW_CHAT_MENU = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[2]/div')
ACCOUNT_NEW_CHAT_ALL_USERS_NAMES = (By.XPATH, '//div[@class="_3ArsE"]//div[@class="_3uIPm '
                                              'WYyr1"]//span[@class="ggj6brxn gfz4du6o '
                                              'r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr '
                                              'i0jNr"]')
ACCOUNT_NEW_CHAT_MENU_EXIT = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div['
                                        '1]/header/div/div[1]/button')
ACCOUNT_NEW_CHAT_MENU_NEW_GROUP = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div['
                                             '2]/div[1]')
ACCOUNT_NEW_CHAT_MENU_NEW_GROUP_FIND_SELECTED_USER = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div['
                                                                '1]/span/div[1]/div[1]/div/label/div')

'''=========ACCOUNT ICON========='''

ACCOUNT_ICON = (By.XPATH, '//*[@id="side"]/header/div[1]/div/div/span')

'''==============CHATS==========='''

ACCOUNT_CHATS = (By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div')
ACCOUNT_CHAT_NAME = (By.XPATH, './/div[@role="gridcell"]/div')

'''====TOP MAIN MENU ACCOUNT====='''

ACCOUNT_MENU = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
ACCOUNT_MENU_NEW_GROUP = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[1]')
ACCOUNT_MENU_FAVORITE_MESSAGES = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[2]')
ACCOUNT_MENU_SETTINGS = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[3]')
ACCOUNT_MENU_EXIT = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]')

'''=====FIND CHAT AND GROUP======'''

FIND_SELECTED_CHAT = (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')

'''===========Long Poll=========='''

FIND_NEW_CHAT_MESSAGES = (By.CSS_SELECTOR, 'div[style*="transform: translateY(0px);"]')
GET_NAME_NEW_CHAT = (By.XPATH, './/span[@dir="auto"]')
GET_MESSAGES = (By.CSS_SELECTOR, 'div[class*="message-in"]')

'''=========WINDOW_CHAT_OR_GROUP=========='''

CHAT_MENU = (By.XPATH, '//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')
CHAT_MENU_DATA_USER = (By.XPATH, '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]')
CHAT_MENU_SELECTED_MESSAGES = (By.XPATH, '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[2]')
CHAT_MENU_EXIT = (By.XPATH, '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[3]')
CHAT_MENU_CLEAR = (By.XPATH, '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[5]')
CHAT_MENU_DELETE = (By.XPATH, '//*[@id  ="app"]/div[1]/span[4]/div/ul/div/div/li[6]')

CHAT_BOTTOM_MENU_MESSAGES_DOWNLOAD = (By.XPATH, '//*[@id="main"]//button[@title="Загрузить"]')

CHAT_ENTRY_MESSAGE = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
CHAT_SEND_MESSAGE = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')

CHAT_ADD_FILE = (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..')
CHAT_ADD_FILE_PHOTO_VIDEO = (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input')
CHAT_ADD_FILE_STICKER = (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-sticker"]/../input')
CHAT_ADD_FILE_DOCUMENT = (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input')
CHAT_WINDOW_FILE_ADD_FILE = (By.XPATH, '//span[@data-testid="add-alt"]/../input')
CHAT_WINDOW_FILE_ADD_FILE_CLICK = (By.XPATH, '//span[@data-testid="add-alt"]/..')

CHAT_WINDOW_FILE_ADD_TEXT = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div['
                                       '2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
CHAT_WINDOW_FILE_SET_VIEW_ONCE = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div['
                                            '1]/div/div[2]/div/div[1]/div[3]/div/div/div[3]/button')
CHAT_SEND_FILE = (By.XPATH, '//span[@data-testid="send"]/..')

CHAT_GET_All_MESSAGES_DIV = (By.XPATH, '//*[@id="main"]/div[3]/div/div[@class="_33LGR"]/div[@tabindex="-1"]')
CHAT_GET_All_MESSAGES = (By.XPATH, CHAT_GET_All_MESSAGES_DIV[1] + '/*')
CHAT_GET_LAST_MESSAGES = (By.XPATH, CHAT_GET_All_MESSAGES_DIV[1] +
                          '/div[@class="_2wUmf message-in focusable-list-item"]')  # messages[-1]

'''=========Message=========='''

SELECTOR_TEXT = (By.XPATH, './/div[@class="copyable-text"]')
SELECTOR_FILE = (By.XPATH, './/div[@class="M_gdf"]')
SELECTOR_PHOTO = (By.XPATH, './/img[@class="jciay5ix tvf2evcx oq44ahr5 lb5m6g5c"]')
SELECTOR_VIDEO = (By.XPATH, './/div[@data-testid="video-content"]')
SELECTOR_DELETE_MESSAGE = (By.XPATH, './/div[@class="_1Gy50 _3TjU1"]')
SELECTOR_STICKER = (By.XPATH, './/img[@class="_3mPXD _9QB_N _1V-dP"]')
SELECTOR_VOICE = (By.XPATH, './/span[@aria-label="Голосовое сообщение"]')

SELECTOR_USER = (By.XPATH, './/span[@class="_1BUvv" and @role="button"]')

WAIT_DOWNLOAD = (By.XPATH, '//div[@class="gndfcl4n cqvkqxai cynldqnp l5pmshjt ecxr5yey lysxvg3k k17s6i4e p357zi0d '
                           'f8jlpxt4 a4ywakfo b7n2qyd4 ekpn4oxx l9g3jx6n lyvj5e2u"]')