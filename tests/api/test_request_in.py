# Разработайте 5 автотестов на запросы из https://reqres.in/ c проверкой статус кода,
# ответа, схемы ответа и логики.
# Пример логики: что пользователь действительно был создан или удален.

from pprint import pprint

import requests
from requests import Response


def test_users_list():
    result: Response = requests.get('https://reqres.in/api/users?page=2')
    pprint(result.json())
    assert result.status_code == 200
