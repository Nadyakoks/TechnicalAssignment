import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def new_driver(chrome_options):
    new_driver = webdriver.Chrome(options=chrome_options)
    yield new_driver
    new_driver.quit()