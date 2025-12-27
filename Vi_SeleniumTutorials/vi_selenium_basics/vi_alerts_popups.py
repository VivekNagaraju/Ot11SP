'''
Created on 23-Nov-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

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

# 3. Click on simple alert
simple_alert_btn = driver.find_element(By.ID, "alertBtn")
simple_alert_btn.click()

time.sleep(3)

# 4. Click on OK on simple alert
driver.switch_to.alert.accept()

# 5. Click on Prompt Alert
prompt_alert_btn = driver.find_element(By.ID, "promptBtn")
prompt_alert_btn.click()

time.sleep(3)

# 6. Sendkeys to prompt alert
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Vivek")
prompt_alert.accept()

NoSuchElementException