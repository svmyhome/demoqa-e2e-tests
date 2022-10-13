from typing import Tuple

import allure
from selene.support.shared import browser

from demoqa_e2e_tests.models import controls
from demoqa_e2e_tests.models.controls import table
from utils.utils import get_path_for_file, wait_and_remove_ads
from tests.test_data.users import Subject


@allure.step("Открываем страницу с формой")
def given_opened():
    browser.open("/automation-practice-form")
    wait_and_remove_ads('#adplus-anchor')


@allure.step("Выбираем предметы")
def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element("#subjectsInput").type(subject.value).press_enter()


@allure.step("Выбираем штат")
def set_state(value: str):
    controls.dropdown.select(browser.element('#state'), value)


@allure.step("Выбираем город")
def set_city(value: str):
    controls.dropdown.select(browser.element('#city'), value)


@allure.step("Вводим имя")
def type_first_name(value: str):
    browser.element("#firstName").type(value)


@allure.step("Вводим фамилию")
def type_last_name(value: str):
    browser.element("#lastName").type(value)


@allure.step("Вводим почту")
def type_user_email(value: str):
    browser.element("#userEmail").type(value)


@allure.step("Вводим телефон")
def type_user_phone_number(value: str):
    browser.element("#userNumber").type(value)


'''
OR 
alternative method set data
'''


@allure.step("Выбираем файл")
def add_pictures(picture: str):
    browser.element("#uploadPicture").send_keys(get_path_for_file(picture))


@allure.step("Выбираем адрес")
def type_current_address(currentAddress: str):
    browser.element("#currentAddress").type(currentAddress)


def scroll_to_subject_input(scroll_into_view):
    browser.element("#subjectsInput").perform(scroll_into_view)


@allure.step("Кликаем на кнопке подтверждения")
def click_submit_button(click):
    browser.element("#submit").perform(click)


@allure.step("Проверяем таблицу")
def should_have_submitted(data):
    for row, value in data:
        table.find_text_in_table(row, value)
