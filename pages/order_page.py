import allure

from locators.order_page_locators import OrderFormPage
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Ищем необходимые поля для создания заказа и заполняем их из списка с файла data')
    def set_order(self, name, last_name, address, phone, date):
        self.add_text_to_element(OrderFormPage.FORM_NAME, name)
        self.add_text_to_element(OrderFormPage.FORM_LAST_NAME, last_name)
        self.add_text_to_element(OrderFormPage.FORM_ADDRESS, address)
        self.click_to_element(OrderFormPage.INPUT_METRO_STATION)
        self.click_to_element(OrderFormPage.METRO_STATION)
        self.add_text_to_element(OrderFormPage.FORM_PHONE, phone)
        self.click_to_element(OrderFormPage.BTN_NEXT)
        self.click_to_element(OrderFormPage.INPUT_TIME)
        self.click_to_element(OrderFormPage.TIME)
        self.add_text_to_element(OrderFormPage.RENTAL_DATE, date)
        self.click_to_element(OrderFormPage.BTN_ORDER)
        self.click_to_element(OrderFormPage.BTN_DONE)

    @allure.step('В конце оформления, ищем сообщение об успешном оформлении и забираем текст')
    def check_order(self):
        return self.get_text_from_element(OrderFormPage.WORD_DONE)
