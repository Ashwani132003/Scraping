from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

print(driver.title)

# Username: Admin, Password: admin123
wait = WebDriverWait(driver, 10)  # wait for page to be loaded before doing 1st task

# driver.find_element(By.NAME,'username').send_keys('Admin')
username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))

# FIrst clear any present value in the element
username_field.clear()
username_field.send_keys('Admin')

driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys('admin123')
driver.find_element(By.CLASS_NAME,'oxd-button').click()

print(driver.title)




driver.close()