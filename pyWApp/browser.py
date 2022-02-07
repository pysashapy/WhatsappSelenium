import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, path_download='', browser=None):
        self.path_download = path_download

        if not browser:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=self.getChromeOptions(),
            )

        self.browser = browser

    def getChromeOptions(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": self.path_download,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        if sys.platform == "win32":
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument(
                '--user-data-dir=C:/Temp/ChromeProfile')
        else:
            chrome_options.add_argument('--user-data-dir=./User_Data')
        return chrome_options

    def getWait(self, time_: int):
        return WebDriverWait(self.browser, time_)

    def getWaitElement(self, wait: WebDriverWait, selector):
        try:
            return wait.until(EC.presence_of_element_located(selector))
        except:
            return None

    def getWaitElements(self, wait: WebDriverWait, selector):
        try:
            return wait.until(EC.presence_of_all_elements_located(selector))
        except:
            return None
