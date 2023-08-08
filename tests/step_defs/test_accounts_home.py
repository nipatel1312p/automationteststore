import pytest
from pytest_bdd import scenarios, when, then, parsers, given
from pages.base_page import BasePage
from pages.home_automationteststore import HomeAutomationTestStore
from pages.login_automationstore import LoginAutomationTestStore

scenarios('../features/accounts_home.feature')


@pytest.fixture()
def home_page(browser_init):
    return HomeAutomationTestStore(browser_init)


@when(parsers.parse('I clicked on Accounts link'))
def click_accounts_dropdown_link(home_page):
    HomeAutomationTestStore.click_home_account(home_page)


@when(parsers.parse('I clicked on Login link'))
def click_login_dropdown_link(home_page):
    HomeAutomationTestStore.click_login_account(home_page)
