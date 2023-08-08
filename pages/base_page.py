import pytest
from selenium import webdriver
import logging


@pytest.mark.usefixtures("browser_init")
class BasePage:

    BASE_URL = "https://automationteststore.com/index.php?rt=account/login"

    def access_url(self):
        self.driver.get(self.url)

    # self.browser.current_url

    def pge_src(self):
        page_src = self.driver.page_source
        return page_src

    def get_logger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
