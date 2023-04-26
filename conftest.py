import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption("--url", default="http://172.27.112.1:8081/")
    parser.addoption("--browser", default="chrome", help="choose one: chrome or firefox")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def browser_options(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        if headless:
            chrome_options.add_argument('--headless=new')
        return chrome_options

    if browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--kiosk')
        if headless:
            firefox_options.add_argument('--headless=new')
        return firefox_options


@pytest.fixture()
def driver(request, browser_options):
    browser_name = request.config.getoption("--browser")

    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=browser_options)
    if browser_name == "firefox":
        driver = webdriver.Firefox(options=browser_options)
    yield driver
    driver.quit()
