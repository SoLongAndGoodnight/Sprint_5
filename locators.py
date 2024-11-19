from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")#"//div[1]/div[2]/span"
    CONSTRUCTOR_MAIN_TAB = (By.XPATH, "//span[text()='Начинки']")#"//div[1]/div[3]/span"
    CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[text()='Булки']")

class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти' and @href]")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']") #//fieldset[1]/div/div/input"  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")# Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REGISTRATION_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_INPUT_REGISTRATION = (By.XPATH, "//fieldset[2]//input[@type='text' and @name='name']")
    PASSWORD_INPUT_REGISTRATION = (By.XPATH, "//fieldset[3]//input[@type='password' and @name='Пароль']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    CONSTRUCTOR_PAGE = (By.XPATH, "//h1[text()='Соберите бургер']")


