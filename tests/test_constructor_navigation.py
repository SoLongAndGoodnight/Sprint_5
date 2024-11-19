from selenium.webdriver.common.by import By
from locators import MainPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_constructor_navigation(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    input_element = driver.find_element(*MainPageLocators.INPUT_EMAIL)
    password_element = driver.find_element(*MainPageLocators.INPUT_PASSWORD)
    button = driver.find_element(*MainPageLocators.SUBMIT_BUTTON)

    input_element.send_keys("lizakorotkova14123@yandex.ru")
    password_element.send_keys("1234567")
    button.click()

    driver.find_element(*MainPageLocators.CONSTRUCTOR_SAUCES_TAB).click()
    driver.find_element(*MainPageLocators.CONSTRUCTOR_MAIN_TAB).click()
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUNS_TAB).click()
