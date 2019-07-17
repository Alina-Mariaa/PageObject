from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_EMAIL_FIELED = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELED = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL_FIELED = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FIELED = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELED = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
