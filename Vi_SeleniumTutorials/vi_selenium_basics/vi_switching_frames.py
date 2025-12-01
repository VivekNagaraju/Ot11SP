'''
Created on 01-Dec-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)

# 2. Navigating to application URL

driver.get("https://demo.automationtesting.in/Frames.html")

# 3. Switch to single frame
driver.switch_to.frame("singleframe")

# 4. Enter name in single frame
input_txt_bx = driver.find_element(By.TAG_NAME, 'input')
input_txt_bx.send_keys("Vivek")
