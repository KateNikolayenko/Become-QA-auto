import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui 
def test_check_incorrect_ysername():
    # Creating Object for using browser
    driver = webdriver.Chrome(
        service=Service(r"c:/Users/Kateryna/Become-QA-auto' + 'chromedriver.exe")
    )

    #Opening page https://github.com/login
    driver.get("https://github.com/login")

    #Finding needed field to enter unvalid data
    login_elem = driver.find_element(By.ID, "login_field")

    #Entering unvalid data
    login_elem.send_keys("nikolayenko.kate@ukr.net")

    #Finding password field
    pass_elem = driver.find_element(By.ID, "password")

    #Entering wrong password
    pass_elem.send_keys("wrong password")
    
    #Search button Sign in
    but_elem = driver.find_element(By.NAME, "commit")

    #Click on button
    but_elem.click()
    
    #Checking page name
    print("============")
    print (driver.title)

    print("============")
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3)

    # Closing browser
    driver.close()


