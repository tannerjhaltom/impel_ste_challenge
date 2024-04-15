from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import logging

LOGGER = logging.getLogger(__name__)


class NavigationBar(WebElement):
    """The 360 manager Navigation Bar"""

    def __init__(self) -> None:
        super().__init__(By.CLASS_NAME, "navbar")

    def select_navigation_option(self, nav_header: str, dropdown_option: int = None) -> None:
        """Selects an option from the navigation bar

        Args:
            nav_header: The main navigation bar option to select (ex: Home, Customers, Admin)
            dropdown_option: The index of the dropdown option to select if one exists
        """
        for element in self._nav_headers:
            if element.text == nav_header:
                element.click()
                if dropdown_option:
                    dropdown_list = element.find_elements(By.CSS_SELECTOR, "li")
                    dropdown_list[dropdown_option].click()
                # There are even more dropdowns within the dropdown menu
                # I could account for that, but that's beyond the scope of this assignment
            else:
                LOGGER.info("nav header not found")

    driver = webdriver.Chrome()
    _nav_headers = driver.find_elements(By.CSS_SELECTOR, ".nav > li")
    _dropdown_options = driver.find_elements(By.CSS_SELECTOR, )

