'''
Created on 03-Jan-2026

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSetUpTearDown(unittest.TestCase):


    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options)
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    def tearDown(self):
        pass


    def test_navigation_to_orangehrm_loginpage(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        current_page_url = self.driver.current_url
        self.assertEqual(expected_url, current_page_url, "current page url is different from expected url")
    
    
    def test_login_to_orangehrm(self):
        username_txtbx = self.driver.find_element(By.NAME, "username")
        username_txtbx.send_keys("Admin")
        password_txtbx = self.driver.find_element(By.NAME, "password")
        password_txtbx.send_keys("admin123")
        login_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_btn.click()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        current_page_url = self.driver.current_url
        self.assertEqual(expected_url, current_page_url, "current page url is different from expected url")
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()