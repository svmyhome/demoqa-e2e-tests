import allure
import selene
from selene import have
from selene.support.shared import browser


def set_option(element: selene.Element, value: str):
    browser.all(element).by(have.exact_text(value)).first.click()
