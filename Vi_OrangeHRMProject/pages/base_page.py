'''
Created on 20-Jan-2026

@author: Vivek
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)
        
    def navigate_to_url(self, url):
        self.driver.get(url)
        
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of(locator))
        element.send_keys(text)
        
    def click_on(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
    def get_page_url(self):
        current_page_url = self.driver.current_url
        return current_page_url
        
        