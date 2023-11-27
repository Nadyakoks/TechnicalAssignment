import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from Hurricane_Insurance.locators.landing_page import INPUT_FIELD, BUTTON_GET_A_QUOTE
from Hurricane_Insurance.locators.building_material_page import (
    RADIO_BUTTON_STRAW,
    BUTTON_SUBMIT_BUILDING_MATERIAL,
)
from Hurricane_Insurance.locators.water_proximity_page import (
    RADIO_BUTTON_YES_WATER_PROXIMITY,
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


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    return options


@pytest.fixture
def firefox_options():
    options = FirefoxOptions()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--private")
    options.add_argument("--headless")
    return options

@pytest.fixture
def safari_options():
    options = SafariOptions()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--private")
    return options

@pytest.fixture
def edge_options():
    options = EdgeOptions()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--private")
    options.add_argument("--headless")
    return options


@pytest.fixture(params=["chrome", "firefox", "safari", "edge"])
def driver(request, chrome_options, firefox_options, safari_options, edge_options):
    if request.param == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        driver = webdriver.Firefox(options=firefox_options)
    elif request.param == "safari":
        driver = webdriver.Safari(options=safari_options)
    elif request.param == "edge":
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError("Invalid browser specified in fixture")

    yield driver
    driver.quit()


# Verify The application is supported on the latest versions of Chrome, Firefox, Safari and Edge browsers
def test_cross_browser_happy_path(driver):
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

    assert driver.find_element(*PLAN_OPTION_STANDARD).is_displayed()
    assert driver.find_element(*PLAN_OPTION_COMPLETE).is_displayed()


