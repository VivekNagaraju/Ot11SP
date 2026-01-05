'''
Created on 05-Jan-2026

@author: Vivek
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Chrome browser is launched')
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    context.driver = webdriver.Chrome(options)
    context.driver.implicitly_wait(5)

@when(u'User navigates to OrangeHRM Login page')
def navigate_to_orangehrm(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'User should see auth/login in current page URL')
def validate_login_page(context):
    expected_url = "auth/login"
    current_page_url = context.driver.current_url
    assert expected_url in current_page_url, "'auth/login' is not present in current page URL"
