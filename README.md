
# Automation Test Store

I am using the pytest bdd framework for the Automation.

Test Automation Framework using selenium and Python with the below features:

Framework is based on page object model.
Reporting using Allure report.
Reading locators from Locators.py file.





## Installation

Installation of the selenium, with python

pip install pytest
pip install selenium
pip install allure-pytest
pip install pytest-bdd    
## Pre-requisite

Selenium 3.x
Python 3.x
Allure
pytest-bdd
## Folders



Pages - Locators.py files wither locators and pages present here
Reports - Allure reports with screenshots
tests - Contains step-def and featurs folders

## Tests
Run the Test case
In order to run the test case after creation, use on of the below commands:

py.test --alluredir=allure_report tests/test_login.py

pytest --alluredir=G:\automationteststore_test\automationteststore\tests\step_defs\allure-report test_login.py
