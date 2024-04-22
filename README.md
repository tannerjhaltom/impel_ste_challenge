# 360 Manager Models

360 Manager Models is a test repository for the 360 Manager that uses the page object model for organization 
and simplicity.

## Usage

Example Test File:
```python
from src.pages.three_sixty_manager import ThreeSixtyManager
from src.pages.login_page import LoginPage
from src.pages.customers_page import CustomersPage

# Define any constants here
EMAIL = "example_email@gmail.com"
PASSWORD = "example_password"

def test_create_account_and_login(self, navigate_to_login_page):
    """Verify that an account can be created and that account can be used to login"""
    # STEP: Navigate to login page and login
    # 360 Manager models uses the driver from this fixture throughout each test. \ 
    # Every page that is instantiated needs to have the driver passed into it
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
```
Example of a 'page' file using the page object model. Each page inherits from Selenium's Page Factory
```python
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

```

## Run a test

To run tests, clone this repo and run the pytest command:
```python
python -m pytest test/<test_file.py>
```
## Contributing

To contribute to this repository, please stick to the page object model by utilizing Selenium's Page Factory.
Element selectors should be placed within files that represent the pages the elements belong to. Test files should
not have element selectors in them.

## Future
To expand on the test model template I've created, I'd like to build out the three_sixty_manager.py file to include 
all major page interactions that are available there since this page seems to be the hub that leads to everything else. 
Adding additional tests for the 360 manager would require these navigation interactions to be modeled out. 
I'm also using a hacky method for getting around the unique name requirements for Customer Names and S3 Buckets. 
With more time, I'd create a fixture that fills out the form with a static username and password 
(using CJK characters for G18n testing) and add a cleanup step to the fixture that goes back and deletes the user after 
the test finishes. With knowledge of internal API's, I would delete the user using an API call to save time and avoid 
issues where deleting the user via the UI fails because of a selector change or other test flakiness issues.
