from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def setup_driver():
    """
    Sets up the Selenium Chrome WebDriver with required options.
    Returns:
        driver (WebDriver): The configured WebDriver instance.
        driver_wait (WebDriverWait): WebDriverWait instance for the driver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    driver_wait = WebDriverWait(driver, 10)
    return driver, driver_wait


def load_okta(driver, driver_wait, url):
    """
    Loads the OKTA login page and clicks the "Select" button.
    """
    driver.get(url)
    select_button = driver_wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.button.select-factor.link-button")
        )
    )
    select_button.click()
    print("Clicked on the 'Select' button.")
    sleep(2)


def navigate_to_time_absence(driver, driver_wait):
    """
    Navigates to the 'Time & Absence' section.
    """
    time_absence_buttons = driver_wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.css-1o9r68h-tileButtonContent")
        )
    )
    if len(time_absence_buttons) >= 3:
        time_absence_buttons[2].click()
        print("Clicked on the third 'Time & Absence' button.")
    else:
        raise Exception("Less than three 'Time & Absence' buttons found.")
    sleep(5)


def open_enter_time_off(driver, driver_wait):
    """
    Opens the 'Enter Time / Time Off' tab.
    """
    enter_time_off_button = driver_wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@data-automation-id='promptOption' and @data-automation-label='Enter Time / Time Off']",
            )
        )
    )
    enter_time_off_button.click()
    print("Clicked on 'Enter Time / Time Off' button.")
    sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to the new tab.")


def select_this_week(driver, driver_wait):
    """
    Selects the 'This Week' option.
    """
    this_week_button = driver_wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@data-automation-activebutton='true' and contains(@title, 'This Week')]",
            )
        )
    )
    this_week_button.click()
    print("Clicked on 'This Week' button.")


def click_actions_button(driver, driver_wait):
    """
    Clicks the first 'Actions' button.
    """
    actions_button = driver_wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class, 'WETM') and contains(@title, 'Actions')]",
            )
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", actions_button)
    driver.execute_script("arguments[0].click();", actions_button)
    print("Clicked on 'Actions' button.")


def click_quick_add(driver, driver_wait):
    """
    Clicks the 'Quick Add' option from the dropdown menu.
    """
    try:
        # Wait for the dropdown popup to be present
        dropdown_popup = driver_wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "WCU.wd-popup.WGVQ.WIVQ"))
        )
        print("Dropdown popup is visible.")

        # Find the "Quick Add" option within the dropdown
        quick_add_option = dropdown_popup.find_element(
            By.XPATH,
            ".//div[@data-automation-id='dropdown-option' and @data-automation-label='Quick Add']",
        )
        print("Found 'Quick Add' option in the dropdown.")

        # Ensure the element is visible and scroll into view if needed
        driver.execute_script("arguments[0].scrollIntoView(true);", quick_add_option)
        driver.execute_script("arguments[0].click();", quick_add_option)
        print("Clicked on 'Quick Add' option.")

    except Exception as e:
        print(f"Error clicking 'Quick Add': {e}")


def click_next_button(driver, driver_wait):
    """
    Clicks the 'Next' button within the popup action bar.
    """
    try:
        # Wait for the action bar containing the 'Next' button to be present
        action_bar = driver_wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "WBQI.WOTI.WERI.WATI.WNSI.WMSI")
            )
        )
        print("Action bar popup is visible.")

        # Locate the 'Next' button within the action bar
        next_button = action_bar.find_element(
            By.XPATH,
            ".//button[@data-automation-id='wd-CommandButton' and @title='Next']",
        )
        print("Found the 'Next' button.")

        # Ensure the button is visible and scroll into view if needed
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

        # Click the 'Next' button
        next_button.click()
        print("Clicked on 'Next' button.")

    except Exception as e:
        print(f"Error clicking 'Next' button: {e}")


def fill_hours(driver, driver_wait, in_time, out_time):
    """
    Fills the 'In' and 'Out' time input fields in the main panel.
    Args:
        driver (WebDriver): Selenium WebDriver instance.
        driver_wait (WebDriverWait): Selenium WebDriverWait instance.
        in_time (str): The time to set for the 'In' field (default: "09:00").
        out_time (str): The time to set for the 'Out' field (default: "18:00").
    """
    try:
        # Wait for the panel container to be present
        panel_container = driver_wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-automation-id='panelSet']")
            )
        )
        print("Panel container is visible.")
        # Locate the 'In' input field within the panel container
        in_input = panel_container.find_element(
            By.XPATH,
            ".//input[@type='text' and @aria-labelledby='56$212662--uid31-formLabel']",
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", in_input)
        in_input.clear()  # Clear any pre-existing value
        in_input.send_keys(in_time)  # Enter the 'In' time
        print(f"Set 'In' time to {in_time}.")

        # Locate the 'Out' input field within the panel container
        out_input = panel_container.find_element(
            By.XPATH,
            ".//input[@type='text' and @aria-labelledby='56$212661--uid32-formLabel']",
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", out_input)
        out_input.clear()  # Clear any pre-existing value
        out_input.send_keys(out_time)  # Enter the 'Out' time
        print(f"Set 'Out' time to {out_time}.")

    except Exception as e:
        print(f"Error filling hours: {e}")


def click_checkboxes(driver, driver_wait):
    """
    Clicks the first 5 checkboxes in the popup panel by directly interacting with the checkbox elements.
    Args:
        driver (WebDriver): Selenium WebDriver instance.
        driver_wait (WebDriverWait): Selenium WebDriverWait instance.
    """
    try:
        # Wait for the checkboxes (input elements) to be present
        checkboxes = driver_wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//input[@type='checkbox' and contains(@class, 'gwt-SimpleCheckBox')]",
                )
            )
        )
        print(f"Found {len(checkboxes)} checkboxes.")

        # Click only the first 5 checkboxes
        for i, checkbox in enumerate(checkboxes[:5]):  # Limit to the first 5 checkboxes
            is_checked = checkbox.get_attribute("aria-checked")
            if is_checked == "false":
                driver.execute_script(
                    "arguments[0].scrollIntoView(true);", checkbox
                )  # Ensure it's visible
                driver.execute_script(
                    "arguments[0].click();", checkbox
                )  # Use JS to click directly
                print(
                    f"Clicked checkbox {i + 1} with ID: {checkbox.get_attribute('id')}"
                )
            else:
                print(
                    f"Checkbox {i + 1} with ID {checkbox.get_attribute('id')} is already checked."
                )

    except Exception as e:
        print(f"Error clicking checkboxes: {e}")


def click_ok_button(driver, driver_wait):
    """
    Clicks the 'OK' button in the popup panel.
    Args:
        driver (WebDriver): Selenium WebDriver instance.
        driver_wait (WebDriverWait): Selenium WebDriverWait instance.
    """
    try:
        # Wait for the 'OK' button to be present
        ok_button = driver_wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@data-automation-id='wd-CommandButton' and @title='OK']",
                )
            )
        )
        print("Found the 'OK' button.")

        # Scroll into view and click the button
        driver.execute_script("arguments[0].scrollIntoView(true);", ok_button)
        ok_button.click()
        print("Clicked the 'OK' button.")

    except Exception as e:
        print(f"Error clicking 'OK' button: {e}")
