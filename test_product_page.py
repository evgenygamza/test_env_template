# -*- coding: utf-8 -*-
__Author__ = 'Gamza'

import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage


class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login = LoginPage(browser, url='http://selenium1py.pythonanywhere.com/')
        login.open()
        login.go_to_login_page()
        login.register_new_user(str(time.time()) + '@fakemail.org', '122342342ff#')
        login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.check_not_the_success_message()

    @pytest.mark.need_review
    def test_user_can_add_to_cart(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_cart()
        page.should_product_in_cart()


def test_should_see_addtocart_btn(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_btn()


tail_list = [i for i in range(10)]
tail_list[7] = pytest.param(7, marks=pytest.mark.xfail)


@pytest.mark.need_review
# @pytest.mark.parametrize('link_tail', tail_list)  # ten-tests mode
def test_guest_can_add_product_to_cart(browser, link_tail):
    # link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_tail}'  # ten-tests
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.should_product_in_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.check_not_the_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.check_success_message_id_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_message_about_empty_cart()
