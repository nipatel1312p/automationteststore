from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator


class HomeAutomationTestStore(BasePage):
    url = "https://automationteststore.com/"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def home_account_link(self):
        home_account_link_locator = (By.CSS_SELECTOR, "a[class*=menu_account]")
        return BaseElement(driver=self.driver, locator=home_account_link_locator)

    @property
    def home_login_link(self):
        home_login_link_locator = (By.CSS_SELECTOR, "a[href*=login]")
        return BaseElement(driver=self.driver, locator=home_login_link_locator)

    def click_home_account(self):
        self.home_account_link.click()

    def click_login_account(self):
        self.home_login_link.click()



    @property
    def remove_element_button(self):
        remove_element_button_locator = (By.XPATH, "//button")
        return BaseElement(driver=self.driver, locator=remove_element_button_locator)
