from Hurricane_Insurance.conftest import driver, chrome_options
from Hurricane_Insurance.locators.landing_page import BUTTON_GET_A_QUOTE
from Hurricane_Insurance.data import (
    LANDING_PAGE,
)


# Verify the landing page is responsive for mobile experience
def test_mobile_responsiveness(driver):
    driver.get(LANDING_PAGE)

    driver.set_window_size(390, 844)

    button_get_a_quote = driver.find_element(*BUTTON_GET_A_QUOTE)

    assert button_get_a_quote.is_displayed()


# Verify the landing page is responsive for tablet experience
def test_tablet_responsiveness(driver):
    driver.get(LANDING_PAGE)

    driver.set_window_size(820, 1180)

    button_get_a_quote = driver.find_element(*BUTTON_GET_A_QUOTE)

    assert button_get_a_quote.is_displayed()
