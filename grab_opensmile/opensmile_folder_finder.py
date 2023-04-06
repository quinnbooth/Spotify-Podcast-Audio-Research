import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def wait_for_load(old_element):
    while True:
        try:
            old_element.find_element(by=By.XPATH, value="//div[contains(@role, 'row')]")  # Ping element
        except StaleElementReferenceException:
            break   # Break once element expires


def get_prefixes(csv_filename): # Extract show_filename_prefix fields from csv
    df = pd.read_csv(csv_filename)
    prefixes = set()
    for row in df.show_filename_prefix:
        row = row.strip('][').split(', ')
        show = row[0]
        prefix = show[6:8]
        prefixes.add(prefix)
    return prefixes


def navigate_to_opensmile(credentials_filename):    # Get to openSMILE folder
    # Start driver and navigate to Box login
    service = Service('/usr/lib/chromium-browser/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get('https://app.box.com/login')
    driver.implicitly_wait(10)

    # Grab Box credentials from external file
    creds = open(credentials_filename, "r")
    username = creds.readline().replace("username:", "").strip()
    password = creds.readline().replace("password:", "").strip()
    creds.close()

    # Pass username to email prompt
    uname = driver.find_element("id", "login-email")
    uname.send_keys(username)

    # Click on the "Next" button
    next_button = driver.find_element("id", "login-submit")
    next_button.click()

    # Wait for the password input field to appear
    password_field = WebDriverWait(driver, 10).until(
         expected_conditions.visibility_of_element_located((By.ID, "password-login"))
    )

    # Enter your password and click on the "Log In" button
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

    # Wait for previous link to expire
    wait_for_load(link_element)

    return driver


if __name__ == "__main__":

    # Get show_filename_prefix fields from csv and go to proper folder in Box
    prefixes = get_prefixes("refined_metadata_ratings.csv")
    driver = navigate_to_opensmile("credentials.txt")

    # Grab table elements, the rows of the first one are folders
    folders = driver.find_elements(by=By.XPATH,
                                   value="//div[contains(@class, 'ReactVirtualized__Table__row table-row ')]")

    for folder in folders:
        try:
            folder_index = folder.get_attribute("data-item-index")
            folder_id = folder.get_attribute("data-resin-folder_id")
            folder_name = folder.text
            print(str(folder_index) + ":\t" + str(folder_name) + " <-> " + str(folder_id) + "\n")
        except StaleElementReferenceException:
            print("\n\nRETRYING\n\n")
            # refresh the page and find the element again
            driver.refresh()
            time.sleep(5)  # wait 5 seconds before finding elements again
            folders = driver.find_elements(by=By.XPATH,
                                           value="//div[contains(@class, 'ReactVirtualized__Table__row table-row ')]")
            continue

    #     """
    #     if folder_name.startswith(folder_prefix) and folder_id not in downloaded_folders:
    #         # download the folder
    #         downloaded_folders.add(folder_id)
    #         folder.click()
    #         # do something to download the files in this folder
    #         # then go back to the previous page with driver.back()
    #     """
