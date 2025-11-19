'''
Created on 19-Nov-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")
print("Navigated to practice site")

# 3. Enter text in wiki search text box
# Locate the element
wiki_search_bx = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")

# Action
wiki_search_bx.send_keys("Selenium")

# 4. Click on wiki search button
# Locate
wiki_search_button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")

# Action
wiki_search_button.click()