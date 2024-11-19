import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators import ForgotPasswordPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_password_error_less_than_6_characters(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON_MAIN).click()

    driver.find_element(*ForgotPasswordPageLocators.REGISTRATION_LINK).click()
    input_element = driver.find_element(*ForgotPasswordPageLocators.NAME_INPUT)
    email_element = driver.find_element(*ForgotPasswordPageLocators.EMAIL_INPUT_REGISTRATION)
    password_element = driver.find_element(*ForgotPasswordPageLocators.PASSWORD_INPUT_REGISTRATION)
    registration_button = driver.find_element(*ForgotPasswordPageLocators.REGISTRATION_BUTTON)

    input_element.send_keys("Liza Korotkova")

    email_element.send_keys("lizakorotkova14123@yandex.ru")
    assert email_element.get_attribute("value") != "", "Поле email должно быть заполнено"

    password_element.send_keys("12345")

    registration_button.click()

    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "//fieldset[3]/div/p")
    assert error_message.text == "Некорректный пароль", "Сообщение об ошибке некорректно"

def test_registration_is_correct(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON_MAIN).click()

    driver.find_element(*ForgotPasswordPageLocators.REGISTRATION_LINK).click()

    input_element = driver.find_element(*ForgotPasswordPageLocators.NAME_INPUT)
    email_element = driver.find_element(*ForgotPasswordPageLocators.EMAIL_INPUT_REGISTRATION)
    password_element = driver.find_element(*ForgotPasswordPageLocators.PASSWORD_INPUT_REGISTRATION)
    registration_button = driver.find_element(*ForgotPasswordPageLocators.REGISTRATION_BUTTON)

    input_element.send_keys("Liza Korotkova")

    email_element.send_keys("lizakorotkova14123@yandex.ru")
    assert email_element.get_attribute("value") != "", "Поле email должно быть заполнено"

    password_element.send_keys("1234567")

    registration_button.click()
