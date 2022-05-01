# -*- coding: utf-8 -*-
__Author__ = 'Gamza'
from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), 'cart isn`t empty'

    def should_be_message_about_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_MESSAGE), 'there is no message about empty cart'
