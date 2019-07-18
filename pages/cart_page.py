from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import (NoSuchElementException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(object):
    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket is empty"

    def should_be_message_basket_is_empty(self):
#        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "Basket is not empty"
        message_basket_empty = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text
        assert "Your basket is empty" in message_basket_empty, "Basket is not empty"