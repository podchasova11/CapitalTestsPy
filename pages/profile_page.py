from base.base_page import BasePage


class ProfilePage(BasePage):

    _PAGE_URL = "https://capital.com/trading/profile"

    # Локаторы личного кабинета (открывается после успешного логина)
    _WELCOME_TITLE = "//h1[contains(@class,'welcome')]"
    _LOGOUT_BUTTON = "//button[@id='logout']"
    _BALANCE_WIDGET = "//div[contains(@class,'balance')]"

    def is_opened(self) -> bool:
        return self.is_element_visible(self._WELCOME_TITLE, timeout=10)

    def click_logout_button(self):
        self.driver.find_element(*self._LOGOUT_BUTTON).click()
        return self

    def get_balance_text(self) -> str:
        return self.get_text(self._BALANCE_WIDGET)
