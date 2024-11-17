import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_successful_registration(driver):
    driver.get(BASE_URL)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    time.sleep(1)

    input_element = driver.find_element(By.XPATH, "//input[@type='text']")
    password_element = driver.find_element(By.XPATH, "//input[@type='password']")
    button = driver.find_element(By.XPATH, "//button[text()='Войти']")

    input_element.send_keys("lizakorotkova14123@yandex.ru")
    password_element.send_keys("1234567")
    button.click()

    driver.quit()

