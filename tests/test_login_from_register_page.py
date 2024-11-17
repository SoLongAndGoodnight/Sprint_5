import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "https://stellarburgers.nomoreparties.site/register"

def test_sussesfull_login_from_register_page(driver):
    driver.get(BASE_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, "//p/a").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("lizakorotkova14123@yandex.ru")
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("1234567")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(2)

    driver.quit()