import allure
from data import UrlPage
from locators.home_page_locators import HomeLocators
from pages.home_page import HomePage
from pages.logo_page import LogoHomePage


class TestLogoPage:
    @allure.title('Проверка перехода на Дзен, при клике на логотип "Яндекс"')
    @allure.description('На главной странице, кликаем на логотип "Яндекс", переходим на главную страницу Дзен и там '
                        'ищем кнопку "Найти"')
    def test_logo_click_redirects_to_dzen_and_search_button(self, driver):
        driver.get(UrlPage.PAGE_URL)
        logo_page = LogoHomePage(driver)
        actual_text = logo_page.check_logo_yandex()
        expected_text = 'Найти'
        assert actual_text == expected_text

    @allure.title('Проверка перехода на главную страницу самоката')
    @allure.description('На главной странице, кликаем на кнопку "Заказать", затем кликаем на логотип "Самокат", '
                        'переходим на главную и ищем в блоке с вопросами первый вопрос')
    def test_logo_click_to_scooter_home_and_shows_text(self, driver):
        driver.get(UrlPage.PAGE_URL)
        logo_page = LogoHomePage(driver)
        home_page = HomePage(driver)
        home_page.click_on_cookie_confirm_btn()
        logo_page.click_to_element(HomeLocators.UP_ORDER_BTN)
        actual_text = logo_page.check_logo_scooter(8)
        expected_text = 'Сколько это стоит? И как оплатить?'
        assert actual_text == expected_text
