'''
Created on 02-Jan-2026

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOrangeHRMLogin(unittest.TestCase):


    def test_navigation_to_orangehrm_loginpage(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        current_page_url = driver.current_url
        self.assertEqual(expected_url, current_page_url, "current page url is different from expected url")
    
    
    def test_login_to_orangehrm(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_txtbx = driver.find_element(By.NAME, "username")
        username_txtbx.send_keys("Admin")
        password_txtbx = driver.find_element(By.NAME, "password")
        password_txtbx.send_keys("admin123")
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        current_page_url = driver.current_url
        self.assertEqual(expected_url, current_page_url, "current page url is different from expected url")
    

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
