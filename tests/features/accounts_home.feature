
Feature: Home page tests

  Background: Access home page
    Given I Navigated to the "automationteststore.com" page

  Scenario: Clicked on account link and then login link
    When I clicked on Accounts link
    When I clicked on Login link

