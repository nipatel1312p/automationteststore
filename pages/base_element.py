from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        # self.value = value
        # self.by = by
        # self.locator = (self.by, self.value)
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return self.web_element

    def click(self):
        # element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element.click()

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def dom_page_source(self):
        page_source = self.driver.page_source
        return page_source

    def find_elements(self):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.locator))
        return elements

    def right_click_element(self):
        action_chain = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        action_chain.move_to_element(element).context_click().perform()

    def click_alert_element(self):
        alert_element = self.driver.switch_to.alert
        return alert_element

    def accept_alert_element(self):
        alert_element = self.driver.switch_to.alert
        alert_element.switch_to.alert

    def action_chains_item(self):
        action_chain = ActionChains(self.driver)
        return action_chain

    @property
    def select_item(self, element):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        # self.web_element = element
        select_item = Select(self.driver(element))
        return select_item

    def iframe_switch_item(self):
        element = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.locator))
        return element

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

