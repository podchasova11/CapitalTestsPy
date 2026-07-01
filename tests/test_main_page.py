from base.base_test import BaseTest


class TestMainPage(BaseTest):

    def test_main_page_opens_successfully(self):
        self.main_page.open()
        self.main_page.accept_cookies_if_present()

        assert self.main_page.is_logo_visible(), "Логотип на главной странице не отображается"
        assert "capital.com" in self.main_page.get_current_url()

    def test_navigation_menu_is_visible(self):
        self.main_page.open()
        self.main_page.accept_cookies_if_present()

        assert self.main_page.is_nav_menu_visible(), "Меню навигации не отображается"

    def test_search_instrument_field_accepts_input(self):
        self.main_page.open()
        self.main_page.accept_cookies_if_present()

        self.main_page.search_instrument("Bitcoin")

        field_value = self.main_page.driver.find_element(
            *self.main_page._SEARCH_INSTRUMENT_INPUT
        ).get_attribute("value")
        assert field_value == "Bitcoin"
