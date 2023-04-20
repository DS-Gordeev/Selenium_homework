from locators import MainPage, CatalogPage, ProductCardPage, AdminLoginPage, UserRegisterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOpenCart:

    def test_check_main_page(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, timeout=10)
        assert wait.until(EC.visibility_of_element_located(MainPage.SEARCH_INPUT))
        assert wait.until(EC.visibility_of_element_located(MainPage.SEARCH_BUTTON))
        assert wait.until(EC.visibility_of_all_elements_located(MainPage.MENU_CATEGORIES))
        assert wait.until(EC.visibility_of_element_located(MainPage.SLIDE_SHOW))
        assert wait.until(EC.visibility_of_element_located(MainPage.BOTTOM_CAROUSEL))

    def test_check_catalog_page(self, driver, base_url):
        driver.get(base_url + '')
        wait = WebDriverWait(driver, timeout=10)
