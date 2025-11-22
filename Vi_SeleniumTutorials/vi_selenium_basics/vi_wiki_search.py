'''
Created on 19-Nov-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(20)
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

# time.sleep(5) # Hard wait 
windows = driver.window_handles
print("windows:", windows)

print("Before clicking on search result:",driver.title)

time.sleep(50)
# 5. Click on a search result
# Locate using link text
wiki_search_result = driver.find_element(By.LINK_TEXT, "Selenium (software)")

# Click action
wiki_search_result.click()

print("After clicking on search result:",driver.title)

# 6. Switch the tab/ window
windows = driver.window_handles
print("windows:", windows)

driver.switch_to.window(windows[1])

'''
# 7. Click on History
history_link = driver.find_element(By.ID, "toc-History")
history_link.click()
'''