import os
import time
from pprint import pprint

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
