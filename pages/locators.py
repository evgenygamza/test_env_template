# -*- coding: utf-8 -*-
__Author__ = 'Gamza'
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CART_SUM = (By.CSS_SELECTOR, '.basket-mini')
    BOOK_NAME = (By.CSS_SELECTOR, '.alert:first-child strong')
