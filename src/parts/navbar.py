import logging
import time
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

LOGGER = logging.getLogger(__name__)


class NavigationBar(PageFactory):
    """The 360 manager Navigation Bar"""

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        time.sleep(5)

    locators = {
        'login_dropdown_button': ('id', "navbar-login-menu")
    }

    def select_navigation_option(self, nav_header: str, dropdown_option: str = None) -> None:
        """Selects an option from the navigation bar

        Args:
            nav_header: The main navigation bar option to select (ex: Home, Customers, Admin)
            dropdown_option: The text for the dropdown option to select if one exists
        """
        for element in list(self.nav_headers()):
            if element.text == nav_header:
                element.click()
                if dropdown_option:
                    for list_option in list(self.dropdown_options()):
                        if list_option.text == dropdown_option:
                            list_option.click()
                            break
                break
                # There are even more dropdowns within the dropdown menu
                # I could account for that, but that's beyond the scope of this assignment
            else:
                LOGGER.info("nav header not found")

    def logout(self) -> None:
        self.login_dropdown_button.click_button()
        self.dropdown_options()[0].click()
        time.sleep(5)

    def user_is_logged_in(self, username: str) -> bool:
        """Verifies whether a given user is currently logged in

        Args:
            username: the username of the expected user
        Returns:
            True if provided user is logged in, False if not
        """
        return bool(username == self.login_dropdown_button.get_text())

    # Group Element selectors

    def nav_headers(self): return self.driver.find_elements(By.CSS_SELECTOR, ".nav > li")
    def dropdown_options(self): return self.driver.find_elements(By.CSS_SELECTOR, ".dropdown.open li")
