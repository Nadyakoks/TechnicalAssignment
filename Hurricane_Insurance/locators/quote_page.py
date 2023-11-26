from selenium.webdriver.common.by import By

PLAN_OPTION_STANDARD = (By.XPATH, '//h3[contains(text(),"Standard")]')

PLAN_OPTION_COMPLETE = (By.XPATH, '//h3[contains(text(),"Complete")]')

CHECKBOX_COMPLETE_PLAN = (By.XPATH, '//span[@data-testid="price_FloodProtection"]')

CHECKBOX_LABEL = (By.XPATH, '//span[contains(text(),"Include Flood Protection")]')
