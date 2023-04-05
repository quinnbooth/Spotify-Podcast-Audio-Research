import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

df = pd.read_csv("refined_metadata_v2.1.csv")
prefixes = set()
for row in df.show_filename_prefix:
    row = row.strip('][').split(', ')
    show = row[0]
    prefix = show[6:8]
    prefixes.add(prefix)
print(prefixes)
print(len(prefixes))

driver = webdriver.Chrome(
  executable_path='/usr/lib/chromium-browser/chromedriver')
driver.get('https://app.box.com/login')
driver.implicitly_wait(10)
driver.maximize_window()

username = "xxx"
uname = driver.find_element("id", "login-email") 
uname.send_keys(username)

# Click on the "Next" button
next_button = driver.find_element("id", "login-submit")
next_button.click()

# Wait for the password input field to appear
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password-login"))
)

# Enter your password and click on the "Log In" button
password = "XXX"
password_field.send_keys(password)
login_button = driver.find_element("id", "login-submit-password")
login_button.click()

# Click on Spotify-Podcasts folder
link_element = driver.find_element(by=By.XPATH, value='//a[@href="/folder/107932668321"]')
link_element.click()

# Click on EN
link_element = driver.find_element(by=By.XPATH, value='//a[@href="/folder/175742097782"]')
link_element.click()

# Click on OpenSmile
link_element = driver.find_element(by=By.XPATH, value='//a[@href="/folder/140172208712"]')
link_element.click()
