from typing import Tuple

import allure
import selene
from selene import have
from selene.support.shared import browser

from tests.test_data.users import Hobby


@allure.step("Выбираем хобби")
def add_option(element: selene.Element, values: Tuple[Hobby]):
    for hobby in values:
        browser.all(element).by(have.value(hobby.value)).first.element('..').click()
