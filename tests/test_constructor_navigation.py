import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_constructor_navigation(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    input_element = driver.find_element(By.XPATH, "//input[@type='text']")
    password_element = driver.find_element(By.XPATH, "//input[@type='password']")
    button = driver.find_element(By.XPATH, "//button[text()='Войти']")

    input_element.send_keys("lizakorotkova14123@yandex.ru")
    password_element.send_keys("1234567")
    button.click()

    driver.find_element(By.XPATH, "//div[1]/div[2]/span").click()
    driver.find_element(By.XPATH, "//div[1]/div[3]/span").click()
    driver.find_element(By.XPATH, "//div[1]/div[1]/span").click()

    driver.quit()