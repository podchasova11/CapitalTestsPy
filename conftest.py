import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver_init(request):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless=new")  # раскомментировать для запуска в CI

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield

    driver.quit()