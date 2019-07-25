from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

class TestUserAddToCartFromProductPage(object):


    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = LoginPage(browser, link)
        self.link.open()
        self.link.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.link.register_new_user(email, password)
        self.link.should_be_authorized_user()


    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_see_button()
        page.should_be_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_see_button()
    page.should_be_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = CartPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_message_basket_is_empty()