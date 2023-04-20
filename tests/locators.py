from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div#search button")
    MENU_CATEGORIES = (By.XPATH, "//nav[@id='menu']/div/ul/li")
    SLIDE_SHOW = (By.ID, "slideshow0")
    BOTTOM_CAROUSEL = (By.ID, "carousel0")


class CatalogPage:
    pass


class ProductCardPage:
    pass


class AdminLoginPage:
    pass


class UserRegisterPage:
    pass
