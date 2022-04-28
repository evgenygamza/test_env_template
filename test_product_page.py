# -*- coding: utf-8 -*-
__Author__ = 'Gamza'
import pytest
from .pages.product_page import ProductPage


def test_should_see_addtocart_btn(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_btn()


@pytest.mark.parametrize('link_tail', [0,1,2,3,4,5,6,pytest.param(7, marks=pytest.mark.xfail),8,9])
def test_add_to_cart(browser, link_tail):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_tail}'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()

