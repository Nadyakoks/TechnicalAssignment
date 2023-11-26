from Hurricane_Insurance.conftest import driver, chrome_options
from Hurricane_Insurance.locators.landing_page import INPUT_FIELD, BUTTON_GET_A_QUOTE
from Hurricane_Insurance.locators.building_material_page import (
    RADIO_BUTTON_STRAW,
    BUTTON_SUBMIT_BUILDING_MATERIAL,
)
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


# Verify entered zip code is persist upon navigation
def test_zip_code_persist_upon_navigation(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    driver.back()

    assert driver.find_element(*INPUT_FIELD).get_attribute("value") == ZIP_CODE


# Verify entered zip code is persist upon refresh
def test_zip_code_persist_upon_refresh(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE

    driver.back()
    driver.refresh()

    assert driver.find_element(*INPUT_FIELD).get_attribute("value") == ZIP_CODE


# Verify selection of building material is persisted upon navigation
def test_build_material_selection_persist_upon_navigation(driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE

    driver.back()

    assert driver.find_element(*RADIO_BUTTON_STRAW).is_selected() is True


# Verify selection of building material is persisted upon refresh
def test_build_material_selection_persist_upon_refresh(driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE

    driver.back()
    driver.refresh()

    assert driver.find_element(*RADIO_BUTTON_STRAW).is_selected() is True


# Verify selection of water proximity is persisted upon navigation
def test_water_proximity_selection_persist_upon_navigation(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE

    driver.back()

    assert driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).is_selected() is True


# Verify selection of water proximity is persisted upon refresh
def test_water_proximity_selection_persist_upon_refresh(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE

    driver.back()
    driver.refresh()

    assert driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).is_selected() is True
