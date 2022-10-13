from pathlib import Path

from selene import have, command
from selene.support.shared import browser

import demoqa_e2e_tests


def get_path_for_file(file):
    """Находим текущий путь, вычитаем папку с тестами, добавляем папку с ресурсами и файл"""
    # abs_file_path = os.path.abspath('../resources/test.txt')
    return str(
        Path(demoqa_e2e_tests.__file__).parent.parent.joinpath(f'resources/{file}')
    )


def wait_and_remove_ads(element):
    ads = browser.all(element)
    '''ждет чтобы все отобразилась, одна реклама и если дожидается то удаляет иначе скипает'''
    if ads.with_(timeout=10).wait_until(have.size_greater_than_or_equal(1)):
        ads.perform(command.js.remove)
        '''
        OR
        browser.execute_script(
        'document.querySelectorAll("#adplus-anchor").forEach(element => element.remove())'
        )
        
        '''
