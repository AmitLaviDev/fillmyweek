from res import *
from time import sleep

if __name__ == "__main__":
    driver, driver_and_wait = load_okta()
    (
        okta_click(config.laptop_okta_x, config.laptop_okta_y)
        if config.ui == "laptop"
        else None
    )
    input_text(config.password)
    (
        password_click(config.laptop_pas_x, config.laptop_pas_y)
        if config.ui == "laptop"
        else password_click(config.station_pas_x, config.station_pas_y)
    )
    sleep(10)
    navigate_site(driver, driver_and_wait)
