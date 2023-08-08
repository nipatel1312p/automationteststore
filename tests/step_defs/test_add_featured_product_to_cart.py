import pytest
from pytest_bdd import scenarios, when, then, parsers, given
from pages.base_page import BasePage
from pages.add_featured_product_to_cart import AddFeaturedProductToCart

scenarios('../features/add_featured_product_to_cart.feature')


@pytest.fixture()
def add_ftrd_pdt_to_cart(browser_init):
    return AddFeaturedProductToCart(browser_init)


@when(parsers.parse('I clicked on the add to cart for the first featured product'))
def click_fst_ftrd_pdt_cart_button(add_ftrd_pdt_to_cart):
    AddFeaturedProductToCart.click_fst_ftrd_pdt_thbnl(add_ftrd_pdt_to_cart)


@when(parsers.parse('I clicked on the Cart'))
def click_quick_basket_thumbnail(add_ftrd_pdt_to_cart):
    AddFeaturedProductToCart.click_quick_bskt_thbnl(add_ftrd_pdt_to_cart)


@when(parsers.parse('I clicked on Checkout button'))
def click_checkout_button(add_ftrd_pdt_to_cart):
    AddFeaturedProductToCart.click_checkout_button(add_ftrd_pdt_to_cart)


@then('I am being directed to login page')
def click_login_button(login_page):
    pass


