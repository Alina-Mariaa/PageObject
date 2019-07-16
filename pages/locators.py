from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators (object):
    LOGIN_EMAIL_FIELED = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELED = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL_FIELED = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FIELED = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELED = (By.CSS_SELECTOR, "#id_registration-password2")
