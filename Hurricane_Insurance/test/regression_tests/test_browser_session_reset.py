from selenium import webdriver
from Hurricane_Insurance.conftest import driver, chrome_options, new_driver
from Hurricane_Insurance.locators.landing_page import INPUT_FIELD, BUTTON_GET_A_QUOTE
from Hurricane_Insurance.locators.building_material_page import (
    RADIO_BUTTON_STRAW, BUTTON_SUBMIT_BUILDING_MATERIAL)
from Hurricane_Insurance.locators.water_proximity_page import (
    RADIO_BUTTON_YES_WATER_PROXIMITY,
    BUTTON_SUBMIT_WATER_PROXIMITY,
)
from Hurricane_Insurance.data import (
    LANDING_PAGE,
    ZIP_CODE,
    BUILDING_MATERIAL_PAGE,
    WATER_PROXIMITY_PAGE,
    QUOTE_PAGE,
)
import time


# Verify entered zip code is cleared upon closing the browser window
def test_zip_code_is_cleared_upon_closing_browser_window(driver, new_driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    driver.quit()

    new_driver.get(LANDING_PAGE)

    assert new_driver.find_element(*INPUT_FIELD).get_attribute("value") == ""

    new_driver.quit()


# Verify selection of building material is cleared upon closing the browser window
def test_build_material_selection_is_cleared_upon_closing_browser_window(driver, new_driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE

    driver.quit()

    new_driver.get(BUILDING_MATERIAL_PAGE)

    time.sleep(1)

    assert new_driver.find_element(*RADIO_BUTTON_STRAW).is_selected() is False

    new_driver.quit()


# Verify selection of water proximity is cleared upon closing the browser window
def test_water_proximity_selection_is_cleared_upon_closing_browser_window(driver, new_driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE

    driver.close()

    new_driver.get(WATER_PROXIMITY_PAGE)

    assert (
        new_driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).is_selected()
        is False
    )

    new_driver.quit()


# Verify selection of building material is reset after entering a new zip code from the landing page


def test_building_material_selection_reset(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE

    driver.back()
    driver.back()

    driver.find_element(*INPUT_FIELD).send_keys("54321")
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    assert driver.find_element(*RADIO_BUTTON_STRAW).is_selected() is False


# Verify selection of water proximity is reset after entering a new zip code from the Landing page
def test_water_proximity_selection_reset(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE

    driver.back()
    driver.back()
    driver.back()

    driver.find_element(*INPUT_FIELD).send_keys("54321")
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE

    assert driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).is_selected() is False
