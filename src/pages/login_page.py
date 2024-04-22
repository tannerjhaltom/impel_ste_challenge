from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    """Impel Login Page"""

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'email_field': ('ID', "email"),
        'password_field': ('CSS', "input#password"),
        'login_button': ('ID', "submit")
    }

    def login(self, email, password) -> None:
        """Logs into 360 manager

        Args:
            email: the email for the user to log in with
            password: the password to use for login
        """
        self.email_field.set_text(email)
        self.password_field.set_text(password)
        self.login_button.click_button()
