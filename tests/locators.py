from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div#search button")
    MENU_CATEGORIES = (By.XPATH, "//nav[@id='menu']/div/ul/li")
    SLIDE_SHOW = (By.ID, "slideshow0")
    BOTTOM_CAROUSEL = (By.ID, "carousel0")


class CatalogPage:
    HOME_HREF = (By.CSS_SELECTOR, "ul.breadcrumb li:first-child a")
    CART_BUTTON = (By.CSS_SELECTOR, "div#cart button")
    CART_TOTAL = (By.ID, "cart-total")
    INPUT_SORT = (By.ID, "input-sort")
    INPUT_LIMIT = (By.ID, "input-limit")


class ProductCardPage:
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    ADD_TO_FAVORITE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")
    DESCRIPTION = (By.ID, "tab-description")


class AdminLoginPage:
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "form button.btn.btn-primary")
    FORGOT_PASSWORD_HREF = (By.XPATH, "//a[text()='Forgotten Password']")
    HEADER_LOGO_HREF = (By.CSS_SELECTOR, "div#header-logo a")


class UserRegisterPage:
    FIRST_NAME_INPUT = (By.NAME, "firstname")
    EMAIL_NAME_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
