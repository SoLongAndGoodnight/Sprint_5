import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "https://stellarburgers.nomoreparties.site/"



def test_successful_registration(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    input_element = driver.find_element(By.XPATH, "//input[@type='text']")
    password_element = driver.find_element(By.XPATH, "//input[@type='password']")
    button = driver.find_element(By.XPATH, "//button[text()='Войти']")

    input_element.send_keys("lizakorotkova14123@yandex.ru")
    password_element.send_keys("1234567")
    button.click()

    driver.find_element(By.XPATH, "//a/p").click()
    time.sleep(1)
    constructor = driver.find_element(By.XPATH, "//ul/li[1]/a/p")
    assert constructor.is_displayed(), "Элемент не отображается на странице"

    constructor.click()
    main_page = driver.find_element(By.XPATH, "//section[1]/h1")
    assert main_page.is_displayed(), "Элемент не отображается на странице"

    driver.find_element(By.XPATH, "//nav/a/p").click()
    time.sleep(1)

    logo = driver.find_element(By.XPATH, "//nav/div")
    logo.click()

    driver.quit()
