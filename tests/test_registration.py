import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_password_error_less_than_6_characters(driver):
    driver.get(BASE_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
    time.sleep(1)
    input_element = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    email_element = driver.find_element(By.XPATH, "//fieldset[2]/div/div/input")
    password_element = driver.find_element(By.XPATH, "//fieldset[3]/div/div/input")
    registration_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    time.sleep(1)

    input_element.send_keys("Liza Korotkova")
    time.sleep(1)

    email_element.send_keys("lizakorotkova14123@yandex.ru")
    assert email_element.get_attribute("value") != "", "Поле email должно быть заполнено"

    time.sleep(1)
    password_element.send_keys("12345")

    time.sleep(1)
    registration_button.click()

    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "//fieldset[3]/div/p")
    assert error_message.text == "Некорректный пароль", "Сообщение об ошибке некорректно"

def test_registration_is_correct(driver):
    driver.get(BASE_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
    time.sleep(1)
    input_element = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    email_element = driver.find_element(By.XPATH, "//fieldset[2]/div/div/input")
    password_element = driver.find_element(By.XPATH, "//fieldset[3]/div/div/input")
    registration_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    time.sleep(1)

    input_element.send_keys("Liza Korotkova")
    time.sleep(1)

    email_element.send_keys("lizakorotkova14123@yandex.ru")
    assert email_element.get_attribute("value") != "", "Поле email должно быть заполнено"

    time.sleep(1)
    password_element.send_keys("1234567")

    time.sleep(1)
    registration_button.click()
    time.sleep(2)

    driver.quit()