# -*- coding: utf-8 -*-
__Author__ = 'Gamza'
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     help="Choose browser: chrome or firefox",
                     default='chrome')
    parser.addoption('--language', action='store',
                     help="language: ru, fr, de",
                     default='en')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    lang = request.config.getoption('language')

    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # removes redundant info from logs
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', lang)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser

    time.sleep(5)
    print("\nquit browser..")
    browser.quit()
