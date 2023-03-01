from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
import time

@pytest.mark.pageobject
def test_check_incorrect_username_page_object():
    #Creation object of the page
    sign_in_page = SignInPage()

    #Open login page of GitHub
    sign_in_page.go_to()

    #Try to login
    sign_in_page.try_login("wrongemail@ukr.net", "badpassword")

    #Checking that name of the page is expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    time.sleep(3)

    #Closing browser
    sign_in_page.close()

