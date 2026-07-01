# Capital.com — Selenium + Page Object + pytest

## Структура проекта

```
capital_com_tests/
├── base/
│   ├── base_page.py      # общие локаторы/методы для всех страниц
│   └── base_test.py      # инициализация всех Page Object'ов в setup_method
├── metaclasses/
│   └── meta_locator.py   # автоматически превращает строки-локаторы в кортежи (By, value)
├── pages/
│   ├── main_page.py      # главная страница capital.com
│   ├── login_page.py     # страница логина
│   └── profile_page.py   # личный кабинет (после успешного логина)
├── tests/
│   ├── test_main_page.py
│   └── test_login_page.py   # содержит многостраничный тест test_full_login_flow_navigation
├── conftest.py            # фикстура driver_init, создаёт/закрывает webdriver
├── pytest.ini
└── requirements.txt
```

## Установка

```bash
pip install -r requirements.txt
```

Также нужен установленный Google Chrome и совместимый chromedriver
(если Selenium Manager не подхватит его автоматически, путь
через переменную окружения или Service()).

## Запуск тестов

```bash
pytest -v
```

Запуск конкретного файла:

```bash
pytest -v tests/test_login_page.py
```

## Важно про локаторы

Локаторы в `pages/*.py` подобраны ориентировочно (по типовой структуре
лендинга/логин-формы capital.com на момент написания). Перед реальным
запуском против боевого сайта их нужно актуализировать через
DevTools (F12 → Elements), так как:

- разметка сайта может меняться от версии к версии;
- на сайте активна защита от автоматизации (может потребоваться
  дополнительная настройка undetected-chromedriver / отключение
  флагов автоматизации);
- часть тестов с логином рассчитана на **невалидные** учётные данные
  (проверка сообщения об ошибке), так как реальных тестовых аккаунтов
  для сайта нет.

## Как работает MetaLocator

Вместо того чтобы в каждом Page Object писать:

```python
LOGIN_FIELD = ("xpath", "//input[@id='login']")
```

Можно писать просто:

```python
_LOGIN_FIELD = "//input[@id='login']"
```

`MetaLocator` при создании класса пробегает по всем атрибутам и,
если строка начинается с `//`, `.//` или `(//`, превращает её в
`("xpath", строка)`, а если начинается с `.` или `#` — в
`("css selector", строка)`. Распаковка через `*` в
`find_element(*locator)` всё равно обязательна.
