# -*- coding: utf-8 -*-
__Author__ = 'Gamza'
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_BTN = (By.CSS_SELECTOR, 'span.btn-group a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.register_form .btn-primary')


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CART_SUM = (By.CSS_SELECTOR, '.basket-mini')
    BOOK_NAME = (By.CSS_SELECTOR, '.alert:first-child strong')


class CartPageLocators:
    CART_ITEM = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner')
