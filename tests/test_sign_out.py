import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_successful_sign_out(driver):
    driver.get(BASE_URL)
    driver.maximize_window()

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    time.sleep(1)

    input_element = driver.find_element(By.XPATH, "//input[@type='text']")
    password_element = driver.find_element(By.XPATH, "//input[@type='password']")
    button = driver.find_element(By.XPATH, "//button[text()='Войти']")

    input_element.send_keys("lizakorotkova14123@yandex.ru")
    password_element.send_keys("1234567")
    button.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//header/nav/a/p").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div/nav/ul/li[3]").click()

    driver.quit()