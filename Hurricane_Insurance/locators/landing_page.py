from selenium.webdriver.common.by import By

INPUT_FIELD = (By.XPATH, '//input[@name="postalCode"]')

BUTTON_GET_A_QUOTE = (By.XPATH, '//*[text()="Get a quote"]')

VALIDATION_MESSAGE_REQUIRED = (
    By.XPATH,
    '//p[@class="MuiFormHelperText-root Mui-error"]',
)

VALIDATION_MESSAGE_INVALID = (
    By.XPATH,
    '//p[@class="MuiFormHelperText-root Mui-error MuiFormHelperText-filled"]',
)
