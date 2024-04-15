from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class ThreeSixtyManager(WebElement):
    """The 360 manager page"""

    def __init__(self) -> None:
        super().__init__(By.CSS_SELECTOR, "html")
        # This isn't a good selector, but unfortunately this page doesn't have a unique, top-level selector

    
