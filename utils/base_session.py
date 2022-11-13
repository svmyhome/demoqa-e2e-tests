import json
import logging
import os

import allure
import curlify
from requests import Session
from requests import Response
from dotenv import load_dotenv

load_dotenv()


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        if os.getenv('ALLURE_LOG') != '0':
            method = response.request.method
            url = response.request.url
            curl_message = curlify.to_curl(response.request)
            logging.info(curl_message)
            logging.info(response.text)
            with allure.step(f'{method} {url}'):
                allure.attach(
                    body=curl_message.encode('utf-8'),
                    name=f'Request {response.request.method} {response.status_code}',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='txt',
                )
                try:
                    allure.attach(
                        body=json.dumps(
                            response.json(), indent=4, ensure_ascii=False
                        ).encode('utf-8'),
                        name=f'Response {response.url} {response.status_code}',
                        attachment_type=allure.attachment_type.JSON,
                        extension='json',
                    )
                except ValueError as error:
                    allure.attach(
                        body=response.text.encode('utf-8'),
                        name=f'Not JSON Response {response.url} {response.status_code}',
                        attachment_type=allure.attachment_type.TEXT,
                        extension='txt',
                    )
        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @allure_request_logger
    def request(self, method, url, **kwargs):
        return super().request(method, url=f'{self.base_url}{url}', **kwargs)
