from pprint import pprint

import requests
from requests import Response
from pytest_voluptuous import S
from voluptuous import Schema, PREVENT_EXTRA, ALLOW_EXTRA

supp: tuple = {('text', str), ('url', str)}

schema = Schema(
    {
        'data': [
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
        ],
        'page': int,
        'per_page': int,
        'support': {'url': str, 'text': str},
        'total': int,
        'total_pages': int,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def test_schema_valuptus():
    result: Response = requests.get('https://reqres.in/api/users', params={'page': 2})
    print()
    pprint(result.json())
    assert result.json() == S(schema)
