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


@when(u'User enters username')
def enter_username(context):
    username_txtbx = context.driver.find_element(By.NAME, "username")
    username_txtbx.send_keys("Admin")


@when(u'User enters password')
def enter_password(context):
    password_txtbx = context.driver.find_element(By.NAME, "password")
    password_txtbx.send_keys("admin123")

@when(u'User clicks on login button')
def click_on_login_button(context):
    login_button = context.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

@then(u'User should see dashboard/index in current page URL')
def validate_dashboard_url(context):
    expected_url = "dashboard/index"
    current_page_url = context.driver.current_url
    assert expected_url in current_page_url, "'dashboard/index' is not present in current page URL"

@when(u'User enters username "{text}"')
def enter_username_parameter(context, text):
    username_txtbx = context.driver.find_element(By.NAME, "username")
    username_txtbx.send_keys(text)


@when(u'User enters password "{text}"')
def enter_password_parameter(context, text):
    password_txtbx = context.driver.find_element(By.NAME, "password")
    password_txtbx.send_keys(text)

@then(u'User should see "{text}" in current page URL')
def validate_url_parameter(context, text):
    expected_url = text
    current_page_url = context.driver.current_url
    assert expected_url in current_page_url, f"'{text}' is not present in current page URL"
