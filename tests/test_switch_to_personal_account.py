import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators import ForgotPasswordPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_switch_to_personal_account(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON_MAIN).click()

    input_element = driver.find_element(*ForgotPasswordPageLocators.EMAIL_INPUT)
    password_element = driver.find_element(*ForgotPasswordPageLocators.PASSWORD_INPUT)
    button = driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON)

    input_element.send_keys("lizakorotkova14123@yandex.ru")
    password_element.send_keys("1234567")
    button.click()

    driver.find_element(*ForgotPasswordPageLocators.PROFILE_BUTTON).click()
    element = driver.find_element(*ForgotPasswordPageLocators.EXIT_BUTTON)
    assert element.is_displayed(), "Элемент не отображается на странице"
