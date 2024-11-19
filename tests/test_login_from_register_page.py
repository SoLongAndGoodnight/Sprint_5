import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators import ForgotPasswordPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site/register"

def test_sussesfull_login_from_register_page(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()

    driver.find_element(*ForgotPasswordPageLocators.EMAIL_INPUT).send_keys("lizakorotkova14123@yandex.ru")
    driver.find_element(*ForgotPasswordPageLocators.PASSWORD_INPUT).send_keys("1234567")
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()
