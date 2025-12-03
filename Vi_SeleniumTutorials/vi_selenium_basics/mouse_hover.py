'''
Created on 03-Dec-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# 2. Navigating to application URL

driver.get("https://demo.automationtesting.in/Frames.html")

# 3. Create ActionChains object
actions = ActionChains(driver)

# 4. Mouse hover on WebTable menu item
webtable_menu_item = driver.find_element(By.LINK_TEXT, "WebTable") # Locate the element
actions.move_to_element(webtable_menu_item).perform()