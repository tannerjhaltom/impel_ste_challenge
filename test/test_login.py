import pytest
from src.pages.login_page import LoginPage

# Constants
EMAIL = "tannerhaltom@impel.io"
PASSWORD = "0Och2nL5"


class TestLogin:
    """Tests login and account creation functionality"""

    def test_create_account_and_login(self, create_account_and_login):
        """Verify that an account can be created and that account can be used to login"""
        # STEP: Navigate to login page and login
        LoginPage().login(email=EMAIL, password=PASSWORD)

        # EXPECT: We've reached the landing page
        assert LoginPage().is_displayed(), "Landing page not reached, login was not successful"

        

