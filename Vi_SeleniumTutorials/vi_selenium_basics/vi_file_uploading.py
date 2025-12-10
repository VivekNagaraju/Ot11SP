'''
Created on 06-Dec-2025

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")

# 3. Upload single file
single_file_input = driver.find_element(By.ID, "singleFileInput")
single_file_input.send_keys(r"C:\Users\admin\Downloads\samplefile.pdf") # Option 1
# single_file_input.send_keys("C:\\Users\\admin\\Downloads\\samplefile.pdf") # Option 2
# single_file_input.send_keys("C:/Users/admin/Downloads/samplefile.pdf") # Option 3

# 4. Click on Upload Single File button
upload_single_file_btn = driver.find_element(By.XPATH, "//button[text()='Upload Single File']")
upload_single_file_btn.click()

# 5. Get/fetch the upload status message
single_file_status = driver.find_element(By.ID, "singleFileStatus")
print(single_file_status.text)

'''
Columns: Name, memory, disk, network, cpu
Rows: System, chrome, firefox, ie

//tbody[@id="rows"]/tr[4]/td[4]

//tbody[@id="rows"]/tr[4]/td[contains(text(), "Mbps")]

//tbody[@id="rows"]/tr[4]/td[contains(text(), "MB") and not(contains(text(),"/s"))]
'''