import allure

from locators.home_page_locators import HomeLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step('На главной странице, кликаем на каждый вопрос и забераем с него текс ответа')
    def get_text_answer(self, num):
        locator_q_formatted = self.format_locators(HomeLocators.QUESTIONS_LOCATORS, num)
        locator_a_formatted = self.format_locators(HomeLocators.ANSWER_LOCATORS, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Кликаем на кнопку "Зказать"')
    def click_btn_order(self, locator):
        self.click_to_element(locator)

    @allure.step('Принимаем куки на главной странице')
    def click_on_cookie_confirm_btn(self):
        self.click_to_element(HomeLocators.COOKIE_CONFIRM_BTN)
