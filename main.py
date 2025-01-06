import argparse
from res import *
from time import sleep


def parse_args():
    parser = argparse.ArgumentParser(description="Fill My Week Automation Script")
    parser.add_argument(
        "-ui",
        choices=["laptop", "pc"],
        required=True,
        help="Specify UI type: 'laptop' or 'pc'",
    )
    return parser.parse_args()


if __name__ == "__main__":
    # Parse arguments
    args = parse_args()

    # Set up the driver and wait
    driver, driver_wait = setup_driver()

    try:
        # Load OKTA login page
        load_okta(driver, driver_wait, config.url)

        # Perform actions based on the UI flag
        if args.ui == "laptop":
            sleep(1)
            okta_click(config.laptop_okta_x, config.laptop_okta_y)
            input_text(config.password)
            password_click(config.laptop_pas_x, config.laptop_pas_y)
        else:
            sleep(2)
            input_text(config.password)
            password_click(config.station_pas_x, config.station_pas_y)

        sleep(10)

        # Navigate through the site
        navigate_to_time_absence(driver, driver_wait)
        open_enter_time_off(driver, driver_wait)
        select_this_week(driver, driver_wait)
        click_actions_button(driver, driver_wait)
        click_quick_add(driver, driver_wait)
        click_next_button(driver, driver_wait)
        fill_hours(
            driver, driver_wait, in_time=config.start_time, out_time=config.end_time
        )
        click_checkboxes(driver, driver_wait)
        click_ok_button(driver, driver_wait)
        sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    # finally:
    #     driver.quit()
