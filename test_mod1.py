# write a pytest selenium script to verify the google.com search box
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_flight_booking(browser):
    browser.get("https://demo.guru99.com/test/newtours/")
    user_name = browser.find_element(By.NAME, "userName")
    user_name.send_keys("selenium")
    user_password = browser.find_element(By.NAME, "password")
    user_password.send_keys("selenium")
    submit_button = browser.find_element(By.NAME, "submit")
    submit_button.click()
    wait = WebDriverWait(browser, 5)

# validate the SIGN-OFF link after login happens
    element = wait.until(lambda driver: driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a"))
    assert "SIGN-OFF" in element.text
    print("Test Case Passed")
    browser.save_screenshot("screenshot.png")
    with open("screenshot.png", "rb") as f:
        screenshot_data = f.read()
        # save screenshot data to a file
    print("Screenshot Captured")





