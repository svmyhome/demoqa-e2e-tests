from pathlib import Path

import demoqa_e2e_tests


def get_path_for_file(path):
    """Находим текущий путь, вычитаем папку с тестами, добавляем папку с ресурсами и файл"""
    # abs_file_path = os.path.abspath('../resources/test.txt')
    return str(
        Path(demoqa_e2e_tests.__file__).parent.parent.joinpath(f'resources/{path}')
    )
