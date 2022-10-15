from typing import Tuple

import allure
import selene
from selene import have
from selene.support.shared import browser

from tests.test_data.users import Hobby


class Add_Option:
    def __init__(self, elements: selene.Collection):
        self.elements = elements

    @allure.step("Выбираем хобби")
    def add_option(self, values: Tuple[Hobby]):
        for hobby in values:
            self.elements.by(have.value(hobby.value)).first.element('..').click()
