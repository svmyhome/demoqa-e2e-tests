import os

import pytest
from selene import by, be
from selene.support.shared import browser


def test_singin_web(browser_web):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)


def test_singin_mobile(browser_mobile):
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
