from selenium.webdriver.common.by import By

RADIO_BUTTON_YES_WATER_PROXIMITY = (
    By.XPATH,
    '//div[@role="radiogroup"]//*[@value="true"]',
)

RADIO_BUTTON_NO_WATER_PROXIMITY = (
    By.XPATH,
    '//div[@role="radiogroup"]//*[@value="false"]',
)

BUTTON_SUBMIT_WATER_PROXIMITY = (By.XPATH, '//button[@type="submit"]')
