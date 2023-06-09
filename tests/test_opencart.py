from locators import MainPage, CatalogPage, ProductCardPage, AdminLoginPage, UserRegisterPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestOpenCart:

    def test_check_main_page(self, driver, base_url):
        driver.get(base_url)
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPage.SEARCH_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPage.SEARCH_BUTTON))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_all_elements_located(MainPage.MENU_CATEGORIES))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPage.SLIDE_SHOW))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPage.BOTTOM_CAROUSEL))

    def test_check_catalog_page(self, driver, base_url):
        driver.get(base_url + 'laptop-notebook')
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(CatalogPage.HOME_HREF))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(CatalogPage.CART_BUTTON))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(CatalogPage.CART_TOTAL))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(CatalogPage.INPUT_SORT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(CatalogPage.INPUT_LIMIT))

    def test_product_card_page(self, driver, base_url):
        driver.get(base_url + 'smartphone/iphone')
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(ProductCardPage.ADD_TO_CART_BUTTON))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(ProductCardPage.QUANTITY_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(ProductCardPage.ADD_TO_FAVORITE_BUTTON))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(ProductCardPage.COMPARE_BUTTON))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(ProductCardPage.DESCRIPTION))

    def test_admin_login_page(self, driver, base_url):
        driver.get(base_url + 'admin')
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(AdminLoginPage.USERNAME_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_BUTTON))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(AdminLoginPage.FORGOT_PASSWORD_HREF))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(AdminLoginPage.HEADER_LOGO_HREF))

    def test_user_register_page(self, driver, base_url):
        driver.get(base_url + 'index.php?route=account/register')
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(UserRegisterPage.FIRST_NAME_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(UserRegisterPage.EMAIL_NAME_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(UserRegisterPage.PASSWORD_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(UserRegisterPage.CONFIRM_PASSWORD_INPUT))
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(UserRegisterPage.CONTINUE_BUTTON))
