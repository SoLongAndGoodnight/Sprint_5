import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "https://stellarburgers.nomoreparties.site/forgot-password"


def test_login_from_forgot_password_page(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//div/p/a").click()

    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("lizakorotkova14123@yandex.ru")
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("1234567")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(1)

    driver.quit()