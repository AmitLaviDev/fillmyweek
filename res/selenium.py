from .config import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def load_okta():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option(
        "detach", True
    )  # Prevents Chrome from closing

    # Initialize the Chrome driver with service and options explicitly
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    URL = url
    driver.get(URL)
    driver_wait = WebDriverWait(driver, 10)

    # Wait for up to 10 seconds for the "Select" button to appear
    select_button = driver_wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.button.select-factor.link-button")
        )
    )
    if select_button is None:
        raise Exception("The 'Select' button was not found on the screen.")
    select_button.click()
    sleep(2)
    return driver, driver_wait


def navigate_site(driver, driver_wait):
    try:
        # Locate and click the third "Time & Absence" button
        time_absence_buttons = driver_wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.css-1o9r68h-tileButtonContent")
            )
        )

        if len(time_absence_buttons) >= 3:
            time_absence_buttons[2].click()
            print("Clicked on the third 'Time & Absence' button.")
        else:
            print("Less than three 'Time & Absence' buttons found.")

        # Wait for 5 seconds
        sleep(5)

        # Locate and click the "Enter Time / Time Off" option
        enter_time_off_button = driver_wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@data-automation-id='promptOption' and @data-automation-label='Enter Time / Time Off']",
                )
            )
        )
        enter_time_off_button.click()
        print("Clicked on 'Enter Time / Time Off' button, which opens a new tab.")

        # Wait for the new tab to open and switch to it
        sleep(3)  # Allow a brief pause for the new tab to open
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the latest tab
        print("Switched to the new tab.")

        # Wait for the "This Week" button to appear in the new tab and click it
        this_week_button = driver_wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@data-automation-activebutton='true' and @data-automation-id='label' and contains(@title, 'This Week')]",
                )
            )
        )
        this_week_button.click()
        print("Clicked on 'This Week (0 Hours)' button in the new tab.")

        # Wait for the "Actions" button and click the first one
        actions_buttons = driver_wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//button[@class='WATM WBGN WETM WMRM' and @data-automation-activebutton='true' and contains(@title, 'Actions')]",
                )
            )
        )

        if actions_buttons:
            actions_buttons[0].click()  # Click on the first "Actions" button (index 0)
            print("Clicked on the first 'Actions' button.")
        else:
            print("No 'Actions' buttons found.")

        # Wait for the "Quick Add" element, scroll into view, and click it using JavaScript
        quick_add_element = driver_wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='WBSQ WNRQ WCRQ WKSQ WISQ' and @data-automation-id='dropdown-option' and @data-automation-label='Quick Add']",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", quick_add_element)
        driver.execute_script("arguments[0].click();", quick_add_element)
        print("Clicked on the first 'Quick Add' element using JavaScript.")

        # Add an explicit wait for the "Next" button to be visible and clickable
        next_button = driver_wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='WATM WH5N WBGN WFUM WETM' and @data-automation-activebutton='true' and @data-automation-id='wd-CommandButton' and contains(@title, 'Next')]",
                )
            )
        )

        # Ensure the "Next" button is scrolled into view and clickable
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        sleep(2)  # Additional sleep to ensure any animations or overlays are cleared
        driver.execute_script("arguments[0].click();", next_button)
        print("Clicked on 'Next' button using JavaScript.")

    except Exception as e:
        print(f"Error navigating the site: {e}")
