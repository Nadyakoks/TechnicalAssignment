from Hurricane_Insurance.conftest import driver, chrome_options
from Hurricane_Insurance.locators.landing_page import (
    INPUT_FIELD,
    BUTTON_GET_A_QUOTE,
    VALIDATION_MESSAGE_REQUIRED,
    VALIDATION_MESSAGE_INVALID,
)
from Hurricane_Insurance.data import (
    LANDING_PAGE,
    ZIP_CODE_SHORT,
    ZIP_CODE_LONG,
    ZIP_CODE_NON_EXISTING,
    ZIP_CODE_LETTERS,
    ZIP_CODE_SYMBOLS,
    ZIP_CODE_SPACE,
)
import time


# User should see a validation message if the input field left blank
def test_validation_message_blank(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys()

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_REQUIRED)

    assert validation_message.is_displayed()


# User should see a validation message if enters 4-digit zip code
def test_validation_message_short(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE_SHORT)

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_INVALID)

    assert validation_message.is_displayed()


# User should see a validation message if enters 6-digit zip code
def test_validation_message_long(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE_LONG)

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_INVALID)

    assert validation_message.is_displayed()


# User should see a validation message if enters non-existing zip code
def test_validation_message_non_existing(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE_NON_EXISTING)

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_INVALID)

    assert validation_message.is_displayed()


# User should see a validation message if entered zip code contains letters
def test_validation_message_letters(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE_LETTERS)

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_INVALID)

    assert validation_message.is_displayed()


# User should see a validation message if entered zip code contains special characters
def test_validation_message_characters(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE_SYMBOLS)

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_INVALID)

    assert validation_message.is_displayed()


# User should see a validation message if entered zip code contains space
def test_validation_message_space(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE_SPACE)

    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    validation_message = driver.find_element(*VALIDATION_MESSAGE_INVALID)

    assert validation_message.is_displayed()
