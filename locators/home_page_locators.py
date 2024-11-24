from selenium.webdriver.common.by import By


class HomeLocators:
    QUESTIONS_LOCATORS = (By.XPATH, "//*[@id='accordion__heading-{}']")
    ANSWER_LOCATORS = (By.XPATH, "//*[@id='accordion__panel-{}']")
    UP_ORDER_BTN = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    DOWN_ORDER_BTN = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    COOKIE_CONFIRM_BTN = (By.XPATH, ".//button[text()='да все привыкли']")
