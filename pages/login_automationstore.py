from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .home_automationteststore import HomeAutomationTestStore


class LoginAutomationTestStore(BasePage):
    url = "https://automationteststore.com/index.php?rt=account/login"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    # def access_url(self):
    #     self.driver.get(self.url)

    @property
    def home_account_login_link(self):
        home_account_login_link_locator = (By.CSS_SELECTOR, "a[href*=login]")
        return BaseElement(driver=self.driver, locator=home_account_login_link_locator)

    @property
    def username_inputbox(self):
        username_inputbox_locator = (By.ID, "loginFrm_loginname")
        return BaseElement(driver=self.driver, locator=username_inputbox_locator)

    @property
    def password_inputbox(self):
        password_inputbox_locator = (By.ID, "loginFrm_password")
        return BaseElement(driver=self.driver, locator=password_inputbox_locator)

    @property
    def login_button(self):
        login_button_locator = (By.CSS_SELECTOR, "button[title='Login']")
        return BaseElement(driver=self.driver, locator=login_button_locator)

    def load_login_page(self):
        self.home_account_login_link.click()

    def enter_user_name(self, username):
        self.username_inputbox.input_text(username)

    def enter_password(self, password):
        self.password_inputbox.input_text(password)

    def click_login(self):
        self.login_button.click()

    def login_standard_user(self):
        self.load_login_page()
        self.enter_user_name(username)
        self.enter_password()
        self.login_button.click()

    @property
    def remove_element_button(self):
        remove_element_button_locator = (By.XPATH, "//button")
        return BaseElement(driver=self.driver, locator=remove_element_button_locator)

