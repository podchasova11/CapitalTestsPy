from base.base_page import BasePage


class LoginPage(BasePage):

    _PAGE_URL = "https://capital.com/trading/login"

    # Локаторы страницы логина
    _EMAIL_FIELD = "//input[@name='email' or @id='email']"
    _PASSWORD_FIELD = "//input[@name='password' or @id='password']"
    _SUBMIT_BUTTON = "//button[@type='submit']"
    _ERROR_MESSAGE = "//div[contains(@class,'error')]"
    _FORGOT_PASSWORD_LINK = "//a[contains(text(),'Forgot')]"

    def enter_email(self, email: str):
        field = self.wait_for_element_visible(self._EMAIL_FIELD)
        field.clear()
        field.send_keys(email)
        return self

    def enter_password(self, password: str):
        field = self.driver.find_element(*self._PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)
        return self

    def click_submit_button(self):
        self.driver.find_element(*self._SUBMIT_BUTTON).click()
        return self

    def click_forgot_password(self):
        self.driver.find_element(*self._FORGOT_PASSWORD_LINK).click()
        return self

    def is_error_message_visible(self) -> bool:
        return self.is_element_visible(self._ERROR_MESSAGE, timeout=7)

    def get_error_text(self) -> str:
        return self.get_text(self._ERROR_MESSAGE)

    def login(self, email: str, password: str):
        """Составной шаг: заполнить форму и отправить её."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()
        return self