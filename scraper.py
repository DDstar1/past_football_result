from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the webpage you want to navigate
url = "https://www.theguardian.com/football/results"

# Path to your webdriver. Update this with the path to your webdriver.
# Make sure you have downloaded the appropriate webdriver for your browser.
# For example, if you're using Chrome, download chromedriver from:
# https://sites.google.com/a/chromium.org/chromedriver/downloads


# Initialize webdriver (assuming Chrome here)
driver = webdriver.Chrome()

# Function to scroll to the bottom of the page
def scroll_to_bottom():
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Function to find and click the "Next page" link
def click_next_page():
    # Find the "Next page" link element
    next_page_link = driver.find_element(By.XPATH, '//a[@title="Next page"]')
    # Scroll to the element to ensure it's in view
    ActionChains(driver).move_to_element(next_page_link).perform()
    # Click the "Next page" link
    next_page_link.click()

# Open the webpage
driver.get(url)

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Main loop
while True:
    # Scroll to the bottom of the page
    scroll_to_bottom()
    # Wait for a short moment for the page to load more content
    driver.implicitly_wait(2)
    # Click on the "Next page" link if it exists
    try:
        click_next_page()
    except Exception as e:
        print("No more next pages found. Exiting loop.")
        break

# Close the webdriver
driver.quit()
