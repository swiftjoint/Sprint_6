from locators.home_page_locators import HomeLocators
from locators.logo_page_locators import LogoHomeLocators
from pages.base_page import BasePage


class LogoHomePage(BasePage):

    def check_logo_yandex(self):
        self.click_to_element(LogoHomeLocators.LOGO_YANDEX)
        self.switch_to_window()
        self.find_element_with_wait(LogoHomeLocators.DZEN_LOCATORS)
        return self.get_text_from_element(LogoHomeLocators.DZEN_LOCATORS)

    def check_logo_scooter(self, num):
        locator_q_formatted = self.format_locators(HomeLocators.QUESTIONS_LOCATORS, num)
        self.click_to_element(LogoHomeLocators.LOGO_SCOOTER)
        self.scroll_to_element()
        return self.get_text_from_element(locator_q_formatted)
