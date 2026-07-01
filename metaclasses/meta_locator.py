class MetaLocator(type):
    """
    Метакласс, который перебирает все атрибуты создаваемого класса
    и превращает строковые локаторы в кортежи вида (By, локатор),
    которые ожидает Selenium в find_element(*locator).

    Правила:
        - строка начинается с '//', './/' или '(//'  -> ("xpath", строка)
        - строка начинается с '.' или '#'             -> ("css selector", строка)
    """

    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, str):
                if value.startswith("//") or value.startswith(".//") or value.startswith("(//"):
                    attrs[key] = ("xpath", value)
                elif value.startswith(".") or value.startswith("#"):
                    attrs[key] = ("css selector", value)
        return type.__new__(cls, name, bases, attrs)
