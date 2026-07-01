from base.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_login_page_opens_from_main_page(self):
        """Проверяем, что кнопка Log in на главной странице ведёт на страницу логина."""
        self.main_page.open()
        self.main_page.accept_cookies_if_present()

        self.main_page.click_login_button()
        self.login_page.wait_for_url_contains("login")

        assert "login" in self.login_page.get_current_url()

    def test_login_with_invalid_credentials_shows_error(self):
        """Негативный сценарий: неверные логин/пароль -> сообщение об ошибке."""
        self.login_page.open()
        self.login_page.accept_cookies_if_present()

        self.login_page.login("invalid_user@example.com", "wrongPassword123")

        assert self.login_page.is_error_message_visible(), \
            "Сообщение об ошибке не появилось при вводе неверных данных"

    def test_login_with_empty_fields_keeps_user_on_login_page(self):
        """Проверяем, что форма не отправляется с пустыми полями."""
        self.login_page.open()
        self.login_page.accept_cookies_if_present()

        self.login_page.click_submit_button()

        assert "login" in self.login_page.get_current_url()

    def test_full_login_flow_navigation(self):
        """
        Многостраничный тест:
        1. Открываем главную страницу
        2. Переходим на страницу логина через кнопку Log in
        3. Возвращаемся на главную страницу через клик по логотипу
        """
        # Шаг 1
        self.main_page.open()
        self.main_page.accept_cookies_if_present()
        assert self.main_page.is_logo_visible()

        # Шаг 2
        self.main_page.click_login_button()
        self.login_page.wait_for_url_contains("login")
        assert "login" in self.login_page.get_current_url()

        # Шаг 3
        self.login_page.click_logo()
        self.main_page.wait_for_url_contains("capital.com")
        assert self.main_page.is_logo_visible()
