from src.parts.navbar import NavigationBar
from seleniumpagefactory.Pagefactory import PageFactory


class ThreeSixtyManager(PageFactory):
    """The 360 manager page"""

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {}

    def navigate_to(self, nav_header: str, dropdown_option: str = None) -> None:
        NavigationBar(driver=self.driver).select_navigation_option(nav_header, dropdown_option)
