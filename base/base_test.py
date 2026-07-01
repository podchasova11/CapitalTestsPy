from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class BaseTest:
    """
    Базовый класс для всех тестов.
    self.driver создаётся фикстурой driver_init из conftest.py
    (см. request.cls.driver = driver).
    """

    def setup_method(self):
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)