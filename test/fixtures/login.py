import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def navigate_to_login_page() -> webdriver.Chrome:
    """Navigates to the login page"""
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://prod.url.paylocity.com/?q=39cee9f5ed4945e0b9540a0a443441a7")
    driver.maximize_window()
    time.sleep(5)
    return driver
