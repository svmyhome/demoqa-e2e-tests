import os
from requests import Response
import pytest
from dotenv import load_dotenv

from utils.base_session import BaseSession


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def reqres_session():
    with BaseSession(base_url='https://reqres.in') as session:
        yield session


@pytest.fixture(scope='session')
def shop_session():
    with BaseSession(base_url='https://demowebshop.tricentis.com') as session:
        yield session


@pytest.fixture(scope='session')
def demoqa_session():
    api_url = os.getenv('api_url')
    with BaseSession(base_url=api_url) as session:
        yield session


@pytest.fixture(scope='function')
def demoqa_authorized_user(demoqa_session):
    LOGIN = os.getenv('api_email')
    PASSWORD = os.getenv('api_password')

    response: Response = demoqa_session.post(
        url=f'/login',
        params={'Email': LOGIN, 'Password': PASSWORD},
        headers={'content-type': 'application/x-www-form-urlencoded'},
        allow_redirects=False,
    )
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    return cookie
