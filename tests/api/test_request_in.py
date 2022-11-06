from pprint import pprint

from pytest_voluptuous import S
from requests import Response

from tests.api.schemas import schemas
from utils.base_session import reqres_session


def test_list_users():
    result: Response = reqres_session().get('/api/users', params={'page': 2})
    assert result.status_code == 200
    assert result.json() == S(schemas.list_schema)
    assert isinstance(result.json()['data'], list)
    assert len(result.json()['data']) > 0
    assert result.json()['data'][0]['first_name'] == 'Michael'


def test_create_user():
    result: Response = reqres_session().post(
        '/api/users', json={"name": "morpheus", "job": "leader"}
    )
    pprint(result.json())
    assert result.status_code == 201
    assert result.json() == S(schemas.create_user_schema)
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
    assert result.json() == S(schemas.update_user_schema)
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


def test_list_unknown():
    result: Response = reqres_session().get('/api/unknown')
    print(result.request.url)
    pprint(result.json)
    assert result.status_code == 200
    assert result.json() == S(schemas.LIST_UNKNOWN_SCHEMA)
