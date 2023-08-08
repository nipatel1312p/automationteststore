import pytest
from pytest_bdd import scenarios, when, then, parsers, given
from pages.base_page import BasePage
from pages.login_automationstore import LoginAutomationTestStore

scenarios('../features/login.feature')


@pytest.fixture()
def login_page(browser_init):
    return LoginAutomationTestStore(browser_init)


@when(parsers.parse('I click on Login link'))
def click_login_link(login_page):
    LoginAutomationTestStore.load_login_page(login_page)


@when(parsers.parse('I enter a username of "{username}"'))
def enter_username(login_page, username):
    LoginAutomationTestStore.enter_user_name(login_page, username)


@when(parsers.parse('I enter a password of "{password}"'))
def enter_password(login_page, password):
    LoginAutomationTestStore.enter_password(login_page, password)


@when('I click the Login button')
def click_login_button(login_page):
    LoginAutomationTestStore.click_login(login_page)


