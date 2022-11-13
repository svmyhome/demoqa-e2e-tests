import os
import time
from pprint import pprint

import requests
from allure_commons._allure import step
from pytest_voluptuous import S
from requests import Response
from selene import have
from selene.support.shared import browser
from dotenv import load_dotenv

# svmyhome@gmail.com
# 1234567890
# voldemar
# s
load_dotenv()


API_EMAIL = os.getenv('api_email')
API_PASSWORD = os.getenv('api_password')
API_URL = os.getenv('api_url')
WEB_URL = os.getenv('web_url')


def test_demo_web_shop():

    with step('Open login page'):
        browser.open(WEB_URL)

    with step('Open authorization form'):
        browser.element('.ico-login').click()

    with step('Fill login form'):
        browser.element('#Email').send_keys(API_EMAIL)
        browser.element('#Password').send_keys(API_PASSWORD)

    with step('Submit login form'):
        browser.element('[value="Log in"]').click()

    with step('Verify successful authorization'):
        browser.element('.account').should(have.text(API_EMAIL))


def test_demo_login():
    browser.config.base_url = WEB_URL
    result: Response = requests.post(
        url=f'{WEB_URL}/login',
        params={'Email': 'svmyhome@gmail.com', 'Password': '1234567890'},
        headers={'content-type': 'application/x-www-form-urlencoded'},
        allow_redirects=False,
    )

    authorization_cooks = result.cookies.get('NOPCOMMERCE.AUTH')

    browser.open('')
    browser.driver.add_cookie(
        {'name': 'NOPCOMMERCE.AUTH', 'value': authorization_cooks}
    )
    browser.open('')

    with step('Verify successful authorization'):
        browser.element('.account').should(have.text(API_EMAIL))


def test_demo_login_base_session(shop_session):
    browser.config.base_url = WEB_URL
    result: Response = shop_session.post(
        url=f'/login',
        params={'Email': 'svmyhome@gmail.com', 'Password': '1234567890'},
        headers={'content-type': 'application/x-www-form-urlencoded'},
        allow_redirects=False,
    )

    authorization_cooks = result.cookies.get('NOPCOMMERCE.AUTH')

    browser.open('')
    browser.driver.add_cookie(
        {'name': 'NOPCOMMERCE.AUTH', 'value': authorization_cooks}
    )
    browser.open('')

    with step('Verify successful authorization'):
        browser.element('.account').should(have.text(API_EMAIL))
