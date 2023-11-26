from selenium.webdriver.common.by import By

RADIO_BUTTON_STRAW = (By.XPATH, '//div[@role="radiogroup"]//*[@value="straw"]')

RADIO_BUTTON_STICKS = (By.XPATH, '//div[@role="radiogroup"]//*[@value="sticks"]')

RADIO_BUTTON_BRICKS = (By.XPATH, '//div[@role="radiogroup"]//*[@value="bricks"]')

BUTTON_SUBMIT_BUILDING_MATERIAL = (By.XPATH, '//button[@data-testid="submit_cta"]')
