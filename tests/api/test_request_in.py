# Разработайте 5 автотестов на запросы из https://reqres.in/ c проверкой статус кода,
# ответа, схемы ответа и логики.
# Пример логики: что пользователь действительно был создан или удален.

from pprint import pprint

import requests
from pytest_voluptuous import S
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA, Date

from utils.base_session import reqres_session

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


def test_list_users():
    result: Response = reqres_session().get('/api/users', params={'page': 2})
    # pprint(result.json())
    assert result.status_code == 200
    assert result.json() == S(schema)
    assert isinstance(result.json()['data'], list)
    assert len(result.json()['data']) > 0
    assert result.json()['data'][0]['first_name'] == 'Michael'


create_user_schema = Schema(
    {
        'createdAt': Date(format='%Y-%m-%dT%H:%M:%S.%fZ'),
        'id': str,
        'job': str,
        'name': str,
    }
)


def test_create_user():
    result: Response = reqres_session().post(
        '/api/users', json={"name": "morpheus", "job": "leader"}
    )
    pprint(result.json())
    assert result.status_code == 201
    assert result.json() == S(create_user_schema)
    assert result.json()['job'] == 'leader'
    assert result.json()['name'] == 'morpheus'


def test_update_user():

    response: Response = reqres_session().post(
        '/api/users', json={"name": "morpheus", "job": "leader"}
    )

    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'

    update_user = {"name": "morpheus1", "job": "zion resident"}
    result: Response = reqres_session().put(
        f'/api/users/{response.json()["id"]}', json=update_user
    )

    assert result.status_code == 200
    assert result.json()['name'] == 'morpheus1'
    assert result.json()['job'] == 'zion resident'


def test_delete_user():

    response: Response = reqres_session().post(
        '/api/users', json={"name": "morpheus", "job": "leader"}
    )

    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'

    result: Response = reqres_session().delete(f'/api/users/{response.json()["id"]}')

    assert result.status_code == 204
    assert (
        reqres_session().get(f'/api/users/{response.json()["id"]}').status_code == 404
    )
