from src.pages.three_sixty_manager import ThreeSixtyManager
from src.pages.login_page import LoginPage
from src.pages.customers_page import CustomersPage
from src.parts.navbar import NavigationBar
from test.fixtures.login import navigate_to_login_page

# Constants
EMAIL = "tannerhaltom@impel.io"
PASSWORD = "0Och2nL5"


class TestLogin:
    """Tests login and account creation functionality"""

    def test_create_account_and_login(self, navigate_to_login_page):
        """Verify that an account can be created and that account can be used to login"""
        # STEP: Navigate to login page and login
        driver = navigate_to_login_page
        LoginPage(driver).login(email=EMAIL, password=PASSWORD)

        # STEP: Navigate to Customer Page
        three_sixty_manager = ThreeSixtyManager(driver)
        three_sixty_manager.navigate_to(nav_header="Customers", dropdown_option="List")

        # STEP: Add a new customer, retrieve credentials, and submit form
        customers_page = CustomersPage(driver)
        customers_page.add_customer()
        username = customers_page.complete_form(name="Bob Ross", s3_folder="happy_accidents")
        credentials = customers_page.get_credentials()
        customers_page.save_customer()

        # STEP: Log out and log back in with new customer
        NavigationBar(driver).logout()
        LoginPage(driver).login(email=credentials[0], password=credentials[1])

        # EXPECT: Login attempt succeeded
        assert NavigationBar(driver).user_is_logged_in(username), "Expected user is not logged in"
