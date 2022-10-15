from typing import Tuple

import allure
import selene
from selene import have
from selene.support.shared import browser


class SetOption:
    def __init__(self, elements: selene.Collection):
        self.elements = elements

    def set_option(self, value: str):
        self.elements.by(have.exact_text(value)).first.click()
