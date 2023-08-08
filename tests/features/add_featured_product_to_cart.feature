Feature: Add featured product to cart


  Background: Access home page
    Given I have navigated to the "automationteststore.com" page

  Scenario: Scroll to featured product list
    When I clicked on the add to cart for the first featured product
    When I clicked on the Cart
    When I clicked on Checkout button
    Then I am being directed to login page
