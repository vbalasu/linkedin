from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Set up Chrome options
chrome_options = Options()
chrome_options.headless = False  # Set to False to make the browser visible

# Initialize the WebDriver
browser = webdriver.Chrome(options=chrome_options)

# Set browser window size
browser.set_window_size(1366, 768)

# Navigate to LinkedIn login page
browser.get('https://www.linkedin.com/login')

# Find username field and type the email
username_field = browser.find_element(By.ID, 'username')
username_field.send_keys('vbalasu@gmail.com')

# Find password field and type the password
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys(os.getenv('LINKEDIN_PASSWORD', ''))

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for navigation
time.sleep(5)  # Adjust the sleep time as needed

# Take a screenshot
browser.save_screenshot('linkedin.jpg')

# Close the browser
browser.quit()

print('Saved to linkedin.jpg')
