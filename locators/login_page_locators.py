from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@type = 'checkbox']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Forgot Password?')]")
    CREATE_ACCOUNT_LINK = (By.PARTIAL_LINK_TEXT, "Create an account")
    LOG_BUTTON_WITH_FACEBOOK = (By.XPATH, "//div[@class='d-flex justify-center flex-wrap gap-3']/button[1]")
    LOG_BUTTON_WITH_GOOGLE = (By.XPATH, "//div[@class='d-flex justify-center flex-wrap gap-3']/button[2]")
    LOG_BUTTON_WITH_TWITTER = (By.XPATH, "//div[@class='d-flex justify-center flex-wrap gap-3']/button[3]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//div[text() = 'Email or Password is Invalid']")
