'''
Created on 06-Dec-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")

# 3. Create ActionChains object
actions = ActionChains(driver)

# 4. Select the content in field1 --> Ctrl+a
field1 = driver.find_element(By.ID, "field1")
actions.key_down(Keys.CONTROL, field1).send_keys("a").key_up(Keys.CONTROL).perform()

# 5. Copy content from field1 --> Ctrl+c
# 6. Paste the content into field2 --> Ctrl+v