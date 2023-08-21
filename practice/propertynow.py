from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()
driver.get(url='https://app.propertynow.com.au/search/')

wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
print(driver.title)

# ... Your previous code to click on search and set num_pages ...

# Collect URLs of the detail pages
detail_page_urls = []

for page in range(2):
    web_list = driver.find_element(By.XPATH, "//div[@class='flex flex-col items-start justify-start gap-y-4 mt-4']")
    child_elements = web_list.find_elements(By.XPATH, "./*")

    for l in child_elements:
        detail_page_urls.append(l.get_attribute("href"))

    # Go to the next page
    next_page_link = driver.find_element(By.XPATH, "(//a[@class='relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-pn-grey-100'])[1]")
    next_page_link.click()

# Now, loop through the collected URLs and extract data from each detail page
all_addresses = []
all_mobile = []
all_names = []
all_emails = []

for detail_url in detail_page_urls:
    driver.get(detail_url)
    
    # Extract data as you did before
    address = driver.find_element(By.XPATH, "//h1[@class='w-full text-2xl sm:text-3xl font-medium']").text
    mobile = driver.find_element(By.CSS_SELECTOR, "div[class='text-sm'] div:nth-child(2)").text
    name = driver.find_element(By.CSS_SELECTOR, ".leading-6.mt-2").text
    email = driver.find_element(By.CSS_SELECTOR, "div[class='text-sm'] div:nth-child(2)").text

    all_addresses.append(address)
    all_emails.append(email)
    all_mobile.append(mobile)
    all_names.append(name)

# ... Rest of your code to write data to CSV ...

print(all_mobile)
driver.quit()
