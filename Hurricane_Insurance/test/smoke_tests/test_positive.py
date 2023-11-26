from Hurricane_Insurance.conftest import driver, chrome_options
from Hurricane_Insurance.locators.landing_page import INPUT_FIELD, BUTTON_GET_A_QUOTE
from Hurricane_Insurance.locators.building_material_page import (
    RADIO_BUTTON_STRAW,
    RADIO_BUTTON_STICKS,
    RADIO_BUTTON_BRICKS,
    BUTTON_SUBMIT_BUILDING_MATERIAL,
)
from Hurricane_Insurance.locators.water_proximity_page import (
    RADIO_BUTTON_YES_WATER_PROXIMITY,
    RADIO_BUTTON_NO_WATER_PROXIMITY,
    BUTTON_SUBMIT_WATER_PROXIMITY,
)
from Hurricane_Insurance.locators.quote_page import (
    PLAN_OPTION_COMPLETE,
    PLAN_OPTION_STANDARD,
)
from Hurricane_Insurance.data import (
    LANDING_PAGE,
    ZIP_CODE,
    BUILDING_MATERIAL_PAGE,
    WATER_PROXIMITY_PAGE,
    QUOTE_PAGE,
)
import time


# User is able to proceed with valid 5-digit zip code
def test_valid_zip_code_input(driver):
    driver.get(LANDING_PAGE)

    driver.find_element(*INPUT_FIELD).send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE


# User is able to submit Straw selection of type of building material
def test_build_material_selection_straw(driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*RADIO_BUTTON_STRAW).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE


# User is able to submit Sticks selection of type of building material
def test_build_material_selection_sticks(driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*RADIO_BUTTON_STICKS).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE


# User is able to submit Bricks selection of type of building material
def test_build_material_selection_bricks(driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*RADIO_BUTTON_BRICKS).click()
    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE


# User is able to submit Yes selection of water proximity
def test_water_proximity_selection_yes(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE


# User is not able to proceed without selection of water proximity
def test_water_proximity_selection_no(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_NO_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE


# User is able to see Standard and Complete plan options when selects "Yes" for water proximity
def test_yes_water_proximity_plan_options_displayed(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_YES_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE

    visible_box_plan_standard = driver.find_element(*PLAN_OPTION_STANDARD)
    visible_box_plan_complete = driver.find_element(*PLAN_OPTION_COMPLETE)

    assert visible_box_plan_standard.is_displayed()
    assert visible_box_plan_complete.is_displayed()


# User is able to see Standard and Complete plan options when selects "No" for water proximity
def test_no_water_proximity_plan_options_displayed(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*RADIO_BUTTON_NO_WATER_PROXIMITY).click()
    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == QUOTE_PAGE

    visible_box_plan_standard = driver.find_element(*PLAN_OPTION_STANDARD)
    visible_box_plan_complete = driver.find_element(*PLAN_OPTION_COMPLETE)

    assert visible_box_plan_standard.is_displayed()
    assert visible_box_plan_complete.is_displayed()
