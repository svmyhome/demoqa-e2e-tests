from pprint import pprint

import requests
from requests import Response
from pytest_voluptuous import S
from voluptuous import Schema, PREVENT_EXTRA, ALLOW_EXTRA

from utils.base_session import reqres_session

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def test_get_user():
    result: Response = requests.get('https://reqres.in/api/users', params={'page': '2'})
    # # print(result.status_code)
    # # print(f'REQUEST HEADERS ======== {result.request.headers}')
    # # print(f'RESPONSE HEADERS ======== {result.headers}')
    # # pprint(result.json())
    # # pprint(result.json()['data'][0]['first_name'])
    # # pprint(result.json()['support']['text'])
    assert result.status_code == 200
    assert result.json()['page'] == 2
    assert result.json()['data'][0]['first_name'] == 'Michael'
    assert (
        result.json()['support']['text']
        == 'To keep ReqRes free, contributions towards server costs are appreciated!'
    )


def test_create_user():
    name: str = 'morpheus'
    leader: str = 'leader'
    result: Response = requests.post(
        'https://reqres.in/api/users', json={'name': name, "job": leader}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == leader
    assert isinstance(result.json()['id'], str)

    # assert result.json() == {
    #     "name": name,
    #     "job": leader,
    #     "id": "605",
    #     "createdAt": "2022-10-26T18:11:59.458Z",
    # }


def test_request_schema():

    name: str = 'morpheus'
    leader: str = 'leader'
    result: Response = requests.post(
        'https://reqres.in/api/users', json={'name': name, "job": leader}
    )
    assert result.json() == S(create_user_schema)


def test_request_schema_base_url():

    name: str = 'morpheus'
    leader: str = 'leader'
    result: Response = reqres_session().post(
        '/api/users', json={'name': name, "job": leader}
    )
    print(result.request.url)
    assert result.json() == S(create_user_schema)
