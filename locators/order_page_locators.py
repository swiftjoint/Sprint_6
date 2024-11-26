from selenium.webdriver.common.by import By


class OrderFormPage:
    FORM_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    FORM_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    FORM_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, ".//*[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//*[text()='Бульвар Рокоссовского']")
    FORM_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    RENTAL_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    INPUT_TIME = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    TIME = (By.XPATH, "//div[@role='option' and @aria-selected='false' and text()='сутки']")
    BTN_NEXT = (By.XPATH, "//button[contains(text(), 'Далее')]")
    BTN_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']")
    BTN_DONE = (By.XPATH, "//button[contains(text(), 'Да')]")
    WORD_DONE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
