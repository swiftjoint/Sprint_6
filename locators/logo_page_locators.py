from selenium.webdriver.common.by import By


class LogoHomeLocators:
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    DZEN_LOCATORS = (By.XPATH, "//button[@class='dzen-search-arrow-common__button' and @type='submit' and text("
                               ")='Найти']")
