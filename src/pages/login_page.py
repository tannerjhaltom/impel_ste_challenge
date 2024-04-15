from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(WebElement):
    """Impel Login Page"""

    def __init__(self) -> None:
        super().__init__(By.CLASS_NAME, "side-by-side")

    def login(self, email, password) -> None:
        """Logs into 360 manager

        Args:
            email: the email for the user to log in with
            password: the password to use for login
        """
        self._email_field.clear()
        self._email_field.send_keys(email)
        self._password_field.clear()
        self._password_field.send_keys(password)
        self._login_button.click()

    driver = webdriver.Chrome()
    _email_field = driver.find_element(By.ID, "email")
    _password_field = driver.find_element(By.CSS_SELECTOR, "input#password")
    _login_button = driver.find_element(By.ID, "submit")
