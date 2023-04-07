import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def get_prefixes(csv_filename): # Extract show_filename_prefix fields from csv
    df = pd.read_csv(csv_filename)
    prefixes = []
    for row in df.show_filename_prefix:
        row = row.strip("][").split(', ')[0].strip("'")
        if row not in prefixes:
            prefixes.append(row)
    return prefixes


def get_parent_folders(csv_filename): # Extract show_filename_prefix fields from csv
    prefixes = get_prefixes(csv_filename)
    parent_folders = set()
    for prefix in prefixes:
        parent_folders.add(prefix[5:7].upper())
    return parent_folders


def get_folder_chain(prefix):
    return [s for s in prefix[5:7].upper()]


def find_scrollable_react_div(driver):
    element = driver.find_element(by=By.XPATH,
                                  value="//div[contains(@class, 'ReactVirtualized__Table__row table-row ')]")
    while True:
        print("testing: " + str(element.get_attribute("class")) + " --> ", end="")
        try:
            driver.execute_script('arguments[0].scrollTop += 500;', element)
            print("INTERACTABLE")
        except:
            print("NOT INTERACTABLE")
        time.sleep(3)
        element = element.find_element(by=By.XPATH, value="./..")


def wait_for_load(old_element):
    while True:
        try:
            old_element.find_element(by=By.XPATH, value="//div[contains(@role, 'row')]")  # Ping element
        except StaleElementReferenceException:
            break   # Break once element expires


def move_and_click(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    element.click()


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


def return_to_opensmile(driver, chain):

    # Try to go back to parent folder --> will bring openSMILE folder in frame
    try:
        parent_folder = driver.find_element(by=By.LINK_TEXT, value=chain[1])
        # print("PARENT:\t" + str(parent_folder))
        move_and_click(driver, parent_folder)
        wait_for_load(parent_folder)
    except:
        time.sleep(0.1)

    # Go back to openSMILE folder, might have already been in frame
    smile_folder = driver.find_element(by=By.XPATH, value='//a[@href="/folder/140172208712"]')
    # print("SMILE:\t" + str(smile_folder) + "\n\n")
    move_and_click(driver, smile_folder)
    wait_for_load(smile_folder)
    print("Returned to openSMILE folder.\n")


def click_parent_folder(driver, chain, prefix, scroll_attempts):

    # Search for parent folder, scroll if fails scroll_attempts times
    # Selenium will only find element if it is visible in the window, hence the need for scrolling
    parent_folder = None
    for i in range(scroll_attempts):
        try:
            parent_folder = driver.find_element(by=By.LINK_TEXT, value=chain[1])
        except:
            scrollable_element = driver.find_element(by=By.XPATH,
                                                     value="//div[contains(@class, 'ItemListLayout-mainContent')]")
            driver.execute_script('arguments[0].scrollTop += 500;', scrollable_element)

    # If the folder was found, attempt to click it
    if parent_folder:
        try:
            print(chain[1], end=" --> ")
            move_and_click(driver, parent_folder)
            wait_for_load(parent_folder)
            return True

        # Couldn't click folder, return to openSMILE folder
        except:
            print("Couldn't click parent folder for: " + prefix)
            return_to_opensmile(driver, chain)
            return False

    # Folder was not found, return to openSMILE folder
    else:
        print("Couldn't find parent folder for prefix: " + prefix)
        return_to_opensmile(driver, chain)
        return False


def click_target_folder(driver, chain, prefix, scroll_attempts):

    # Search for folder with prefix as title, scroll if fails scroll_attempts times
    # Selenium will only find element if it is visible in the window, hence the need for scrolling
    folder = None
    for i in range(scroll_attempts):
        try:
            folder = driver.find_element(by=By.LINK_TEXT, value=prefix)
        except:
            scrollable_element = driver.find_element(by=By.XPATH,
                                                     value="//div[contains(@class, 'ItemListLayout-mainContent')]")
            driver.execute_script('arguments[0].scrollTop += 500;', scrollable_element)

    # If the folder was found, attempt to click it
    if folder:
        try:
            print(prefix)
            move_and_click(driver, folder)
            wait_for_load(folder)
            return True

        # Couldn't click folder, return to openSMILE folder
        except:
            print("Couldn't click target folder for prefix: " + prefix)
            return_to_opensmile(driver, chain)
            return False

    # Folder was not found, return to openSMILE folder
    else:
        print("Couldn't find target folder for prefix: " + prefix)
        return_to_opensmile(driver, chain)
        return False


def find_folder(driver, prefix, download_delay):

    # Get folder chain names
    chain = get_folder_chain(prefix)
    print("\n" + prefix + "\n" + str(chain))

    # Enter first folder in folder tree
    grandparent_folder = driver.find_element(by=By.LINK_TEXT, value=chain[0])
    print(chain[0], end=" --> ")
    move_and_click(driver, grandparent_folder)
    wait_for_load(grandparent_folder)

    # Try to enter second folder in folder tree
    if click_parent_folder(driver, chain, prefix, 10):
        # Try to enter target folder
        if click_target_folder(driver, chain, prefix, 10):
            # Go back to openSMILE folder

            # Download file here
            # Log file as downloaded somehow

            time.sleep(download_delay)
            return_to_opensmile(driver, chain)
        else:
            return False
    else:
        return False

    return True


if __name__ == "__main__":

    # Get show_filename_prefix fields from csv and go to proper folder in Box
    prefixes = get_prefixes("refined_metadata_ratings.csv")
    driver = navigate_to_opensmile("credentials.txt")

    # Test first <count> show_filename_prefixes to see if program navigates to them properly
    successful_prefixes = []
    failed_prefixes = []
    count = 10
    for prefix in prefixes:
        count -= 1
        if count < 0:
            break
        elif find_folder(driver, prefix, 0):
            successful_prefixes.append(prefix)
        else:
            failed_prefixes.append(prefix)

    print("\n\nSuccesses: " + str(len(successful_prefixes)) + "\n" + str(successful_prefixes)
          + "\n\nFailures: " + str(len(failed_prefixes)) + "\n" + str(failed_prefixes))
