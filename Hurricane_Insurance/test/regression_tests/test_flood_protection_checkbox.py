from Hurricane_Insurance.conftest import driver, chrome_options
from Hurricane_Insurance.locators.water_proximity_page import (
    RADIO_BUTTON_YES_WATER_PROXIMITY,
    RADIO_BUTTON_NO_WATER_PROXIMITY,
    BUTTON_SUBMIT_WATER_PROXIMITY,
)
from Hurricane_Insurance.locators.quote_page import (
    CHECKBOX_LABEL,
    CHECKBOX_COMPLETE_PLAN,
)
from Hurricane_Insurance.data import (
    WATER_PROXIMITY_PAGE,
)
import time


# Verify the checkbox is checked and disabled for Complete Plan User when user selects "No" for water proximity
def test_checkbox_is_checked_and_disabled(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_NO_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.find_element(*CHECKBOX_COMPLETE_PLAN).is_selected() is True
    assert driver.find_element(*CHECKBOX_COMPLETE_PLAN).is_enabled() is False


# Verify the checkbox is unchecked and enabled for Complete Plan User when user selects "Yes" for water proximity
def test_checkbox_is_unchecked_and_enabled(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.find_element(*CHECKBOX_COMPLETE_PLAN).is_selected() is False
    assert driver.find_element(*CHECKBOX_COMPLETE_PLAN).is_enabled() is True


# Verify the checkbox label has a price indicated when User selects "Yes" for water proximity
def test_checkbox_label_price_indication_yes_water_proximity(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    checkbox_label = driver.find_element(*CHECKBOX_LABEL)

    assert "(+$0)" in checkbox_label.text


# Verify the checkbox label does not have a price indicated when User selects "No" for water proximity
def test_checkbox_label_price_indication_no_water_proximity(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_NO_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    checkbox_label = driver.find_element(*CHECKBOX_LABEL)

    assert "(+$0)" not in checkbox_label.text
