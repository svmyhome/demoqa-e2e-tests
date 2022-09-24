from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_e2e_tests.models import controls
from tests.test_data.users import Subject, Hobby


def given_opened():
    browser.open("/automation-practice-form")
    wait_and_remove_ads()


def wait_and_remove_ads():
    ads = browser.all("#adplus-anchor")
    '''ждет чтобы все отобразилась, одна реклама и если дожидается то удаляет иначе скипает'''
    if ads.with_(timeout=10).wait_until(have.size_greater_than_or_equal(1)):
        ads.perform(command.js.remove)
        '''
        OR
        browser.execute_script(
        'document.querySelectorAll("#adplus-anchor").forEach(element => element.remove())'
        )
        
        '''


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element("#subjectsInput").type(subject.value).press_enter()


def add_hobbies(values: Tuple[Hobby]):
    for hobby in values:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()


def set_state(value: str):
    controls.dropdown.select(browser.element('#state'), value)


def set_city(value: str):
    controls.dropdown.select(browser.element('#city'), value)
