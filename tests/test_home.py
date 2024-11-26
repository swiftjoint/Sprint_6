import allure
import pytest
from data import UrlPage, AnswerData
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка блока "Вопросы о важном"')
    @allure.description('На главной ищем блок "Вопросы о важном", открываем каждый вопрос и проверяем на него ответ')
    @pytest.mark.parametrize(
        'num, result',
        [
            (key, value) for key, value in AnswerData.ANSWER.items()

        ]

    )
    def test_questions_and_answer(self, driver, num, result):
        driver.get(UrlPage.PAGE_URL)
        home_page = HomePage(driver)
        home_page.click_on_cookie_confirm_btn()
        home_page.scroll_to_element()
        assert home_page.get_text_answer(num) == result
