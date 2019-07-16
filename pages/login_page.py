from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELED), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELED), "Login password is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELED), "Register email is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD1_FIELED), "Register pass1 is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD2_FIELED), "Register pass2 is not presented"
        assert True
