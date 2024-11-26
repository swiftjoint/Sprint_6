import allure
import pytest
from data import UrlPage, InputData
from locators.home_page_locators import HomeLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestCreateOrder:

    @allure.title('Проверка оформления заказа, через "Заказать" верхняя')
    @allure.description('Ищем обязательные поля для заказа, заполняем подготовленными данными и проверяем, что заказ '
                        'оформлен')
    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (HomeLocators.UP_ORDER_BTN, InputData.ORDER_DATA_1)
        ]
    )
    def test_create_order_up_btn(self, driver, locator, order_data):
        driver.get(UrlPage.PAGE_URL)
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_on_cookie_confirm_btn()
        home_page.click_btn_order(locator)
        order_page.set_order(*order_data)
        result = order_page.check_order()
        assert 'Заказ оформлен' in result

    @allure.title('Проверка оформления заказа, через "Заказать" нижняя')
    @allure.description('Ищем обязательные поля для заказа, заполняем подготовленными данными и проверяем, что заказ '
                        'оформлен')
    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (HomeLocators.DOWN_ORDER_BTN, InputData.ORDER_DATA_2)
        ]
    )
    def test_create_order_down_btn(self, driver, locator, order_data):
        driver.get(UrlPage.PAGE_URL)
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_on_cookie_confirm_btn()
        home_page.scroll_to_element()
        home_page.click_btn_order(locator)
        order_page.set_order(*order_data)
        result = order_page.check_order()
        assert 'Заказ оформлен' in result
