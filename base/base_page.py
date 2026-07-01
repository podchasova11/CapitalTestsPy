from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):
    """
    Базовый класс для всех Page Object'ов проекта.
    Содержит общие для всех страниц capital.com локаторы и методы:
    принятие cookie-баннера, клик по логотипу, ожидания и т.д.
    """

    # Общие локаторы (встречаются почти на любой странице сайта)
    _COOKIE_ACCEPT_BUTTON = "//button[@id='onetrust-accept-btn-handler']"
    _LOGO_LINK = "//a[contains(@class,'logo')]"

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self):
        """Открывает страницу по её PAGE_URL (задаётся в наследнике)."""
        self.driver.get(self._PAGE_URL)
        return self

    def accept_cookies_if_present(self):
        """Закрывает баннер согласия на cookie, если он появился."""
        try:
            button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self._COOKIE_ACCEPT_BUTTON)
            )
            button.click()
        except Exception:
            pass
        return self

    def click_logo(self):
        self.wait_for_element_clickable(self._LOGO_LINK).click()
        return self

    # ---------- Обёртки над ожиданиями ----------

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_element_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def get_text(self, locator) -> str:
        return self.wait_for_element_visible(locator).text

    def get_current_url(self) -> str:
        return self.driver.current_url

    def wait_for_url_contains(self, part: str, timeout: int = 10) -> bool:
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(part))
