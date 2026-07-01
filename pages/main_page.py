from base.base_page import BasePage


class MainPage(BasePage):

    _PAGE_URL = "https://capital.com/"

    # Локаторы главной страницы
    _LOGIN_BUTTON = "//a[contains(@href,'login')]"
    _SIGNUP_BUTTON = "//a[contains(@href,'signup') or contains(@href,'registration')]"
    _MAIN_LOGO = "//a[contains(@class,'logo')]"
    _SEARCH_INSTRUMENT_INPUT = "//input[@placeholder='Search']"
    _NAV_MENU = "//nav"

    def click_login_button(self):
        self.wait_for_element_clickable(self._LOGIN_BUTTON).click()
        return self

    def click_signup_button(self):
        self.wait_for_element_clickable(self._SIGNUP_BUTTON).click()
        return self

    def search_instrument(self, instrument_name: str):
        field = self.wait_for_element_visible(self._SEARCH_INSTRUMENT_INPUT)
        field.clear()
        field.send_keys(instrument_name)
        return self

    def is_logo_visible(self) -> bool:
        return self.is_element_visible(self._MAIN_LOGO)

    def is_nav_menu_visible(self) -> bool:
        return self.is_element_visible(self._NAV_MENU)