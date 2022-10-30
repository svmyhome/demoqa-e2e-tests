from pprint import pprint

import allure
import requests
from jsonschema import validate
from requests import Response

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1, "maxLength": 5},
        "job": {"type": "string"},
        "try": {"type": "string"},
    },
    "required": ["name", "job", "try"],
    "additionalProperties": False,
}


def test_schema_validation():
    with allure.step('Проверяем схему'):
        validate(instance={"name": "Eggs3", "job": "34.99", "try": '1'}, schema=schema)


schema2 = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "additionalProperties": False,
        "required": ["userId1", "id", "title", "body"],
    },
    "additionalItems": False,
}


def test_schema_validation2():
    result: Response = requests.get('https://jsonplaceholder.typicode.com/posts')
    with allure.step('Проверяем схему'):
        validate(instance=result.json(), schema=schema2)
