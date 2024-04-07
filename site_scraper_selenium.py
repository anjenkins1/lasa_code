from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your webdriver
webdriver_path = "/usr/lib/chromium-browser/chromedriver"

# URL of the website
url = "https://app.v1.statusplus.net/membership/provider/index?society=ipps"

# # Configure Chrome options for headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# # Initialize the webdriver with Chrome options
# driver = webdriver.Chrome(service=webdriver_path, options=chrome_options)

driver = webdriver.Chrome()

# Open the website
driver.get(url)

driver.implicitly_wait(20) 
# Find the search bar element and send keys (replace 'search_term' with your actual search term)
search_bar = Select(driver.find_element(By.ID, "country"))
selector = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="country"]/option[233]')))
driver.execute_script("arguments[0].scrollIntoView(true);",selector)
#search_bar.click()
#search_bar.send_keys("United States (USA)")
# search_bar.
search_bar.select_by_value("234")

# Simulate hitting Enter/Return
search_bar.submit()

# Wait for the results to load (you may need to adjust the wait time)
time.sleep(5)

# Once the results are loaded, scrape the data
# Find the elements containing the data you want to scrape and extract their text
# Replace 'element_selector' with the appropriate selector for the element containing the data
# For example, if the data is in <div> elements with class 'result', you would use 'div.result'
data_elements = driver.find_elements_by_css_selector("div.address-container")

# Extract the text from each data element and print it
for element in data_elements:
    print(element.text)

# Close the browser
driver.quit()
