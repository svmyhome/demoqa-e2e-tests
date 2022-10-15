from typing import Tuple

import allure
import selene
from selene import have
from selene.support.shared import browser


class SetOption:
    def set_option(self):
        browser.all('[for^=gender-radio]').by(have.exact_text('Male')).first.click()
