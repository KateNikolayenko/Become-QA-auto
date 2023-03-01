from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #Finding field with username or email
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Entering invalid username or email
        login_elem.send_keys(username)

        #Finding password field
        pas_elem = self.driver.find_element(By.ID, "password")

        #Entering password
        pas_elem.send_keys(password)

        #Finding signIn button
        button_elem = self.driver.find_element(By.NAME, "commit")

        #Clicking on button
        button_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
