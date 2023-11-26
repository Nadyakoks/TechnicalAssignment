import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Hurricane_Insurance.locators.landing_page import INPUT_FIELD, BUTTON_GET_A_QUOTE
from Hurricane_Insurance.data import (
    LANDING_PAGE,
    ZIP_CODE
)


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-javascript")
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


# Verify the application requires JavaScript to be enabled in order to operate
def test_javascript_disabled_element_visibility(driver):
    driver.get(LANDING_PAGE)

    input_field = driver.find_element(*INPUT_FIELD)
    input_field.send_keys(ZIP_CODE)
    driver.find_element(*BUTTON_GET_A_QUOTE).click()

    assert driver.current_url == LANDING_PAGE
