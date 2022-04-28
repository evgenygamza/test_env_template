# -*- coding: utf-8 -*-
__Author__ = 'Gamza'

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        pass

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), 'there is no add-to-cart button!'

    def should_add_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_btn.click()
        self.solve_quiz_and_get_code()
        cart_price = self.browser.find_element(*ProductPageLocators.CART_SUM).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert '0.00' not in cart_price, 'cart is empty!'
        assert 'Coders at Work' == book_name, 'incorrect book name!'
