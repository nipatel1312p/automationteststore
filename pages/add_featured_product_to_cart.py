from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage


class AddFeaturedProductToCart(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    # def access_url(self):
    #     self.driver.get(self.url)

    @property
    def first_featured_product_cart_thumbnail(self):
        first_featured_product_cart_thumbnail_locator = (By.CSS_SELECTOR, "div[class*=pricetag] a[class='productcart']")
        return BaseElement(driver=self.driver, locator=first_featured_product_cart_thumbnail_locator)

    @property
    def quick_basket_thumbnail(self):
        quick_basket_locator = (By.CSS_SELECTOR, "div[class*=added_to_cart] div[class='quick_basket']")
        return BaseElement(driver=self.driver, locator=quick_basket_locator)

    @property
    def checkout_button(self):
        checkout_button_locator = (By.ID, "cart_checkout1")
        return BaseElement(driver=self.driver, locator=checkout_button_locator)

    def click_fst_ftrd_pdt_thbnl(self):
        self.first_featured_product_cart_thumbnail.click()

    def click_quick_bskt_thbnl(self):
        self.quick_basket_thumbnail.click()

    def click_checkout_button(self):
        self.checkout_button.click()
