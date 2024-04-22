from __future__ import annotations
from seleniumpagefactory.Pagefactory import PageFactory
import time
import random


class CustomersPage(PageFactory):
    """Impel Customers Page"""

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        time.sleep(10)  # There are better ways to do this, but the add customer button likes to take its time loading

    locators = {
        'add_customer_button': ('class_name', "btn-primary"),
        'email_field': ('css', "input[name='email']"),
        'password_field': ('css', "input[name='password']"),
        'name_field': ('css', "input#name"),
        's3_field': ('css', "input[name='s3_folder']"),
        'save_button': ('class_name', "btn-primary")
    }

    def add_customer(self) -> CustomersPage:
        """Clicks the 'Add Customer' button and moves on to the 'Add Customer' form"""
        self.add_customer_button.click()
        return self

    def get_credentials(self) -> list:
        """Gets new customer's credentials

        Returns:
            Customer credentials in list format ex: ['email', 'password']
        """
        return [self.email_field.getAttribute("value"), self.password_field.getAttribute("value")]

    # To improve this, I would create a fixture with a cleanup step \
    # that deleted the user via API call instead of using a randomizer

    def complete_form(self, name: str, s3_folder: str) -> str:
        """Completes the new customer form by filling out required fields

        Returns:
            The name used to create the user along with the random integer
        """
        randomizer = random.randint(0, 1000000)
        randomized_name = name + str(randomizer)
        self.name_field.set_text(randomized_name)
        self.s3_field.set_text(s3_folder + str(randomizer))
        return randomized_name

    def save_customer(self) -> None:
        """Saves the new customer"""
        self.save_button.click_button()
        time.sleep(5)
