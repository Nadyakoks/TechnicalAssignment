from Hurricane_Insurance.conftest import driver, chrome_options
from Hurricane_Insurance.locators.building_material_page import (
    BUTTON_SUBMIT_BUILDING_MATERIAL,
)
from Hurricane_Insurance.locators.water_proximity_page import (
    BUTTON_SUBMIT_WATER_PROXIMITY,
)
from Hurricane_Insurance.data import (
    BUILDING_MATERIAL_PAGE,
    WATER_PROXIMITY_PAGE,
)
import time


# User is not able to proceed without selection of building material
def test_build_material_submission_without_selection(driver):
    driver.get(BUILDING_MATERIAL_PAGE)

    driver.find_element(*BUTTON_SUBMIT_BUILDING_MATERIAL).click()

    time.sleep(1)

    assert driver.current_url == BUILDING_MATERIAL_PAGE


# User is not able to proceed without selection of water proximity
def test_water_proximity_submission_without_selection(driver):
    driver.get(WATER_PROXIMITY_PAGE)

    driver.find_element(*BUTTON_SUBMIT_WATER_PROXIMITY).click()

    time.sleep(1)

    assert driver.current_url == WATER_PROXIMITY_PAGE
