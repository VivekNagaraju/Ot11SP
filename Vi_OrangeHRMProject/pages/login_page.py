'''
Created on 21-Jan-2026

@author: Vivek
'''
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__username_txtbx_locator = (By.NAME, "username")
        self.__password_txtbx_locator = (By.NAME, "password")
        self.__login_btn_locator = (By.XPATH,"//button[@type='submit']")
        
    def enter_username(self, username):
        # self.enter_text(self.username_txtbx_locator, username) # without encapsulation
        self._enter_text(self.__username_txtbx_locator, username) # with encapsulation
        
    def enter_password(self, password):
        # self.enter_text(self.password_txtbx_locator, password)
        self._enter_text(self.__password_txtbx_locator, password)
        
    def click_on_login_btn(self):
        # self.click_on(self.login_btn_locator)
        self._click_on(self.__login_btn_locator)
        
        
