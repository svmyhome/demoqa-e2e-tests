from typing import Tuple

import allure
from selene.support.shared import browser

from demoqa_e2e_tests.models import controls
from demoqa_e2e_tests.models.controls import table
from demoqa_e2e_tests.models.controls.datepicker import DatePicker
from utils.utils import get_path_for_file, wait_and_remove_ads
from tests.test_data.users import Subject, yuri


class RegistrationForm:
    def __int__(self):
        self

    @allure.step("Открываем страницу с формой")
    def given_opened(self):
        browser.open("/automation-practice-form")
        wait_and_remove_ads('#adplus-anchor')
        return self

    @allure.step("Выбираем предметы")
    def add_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element("#subjectsInput").type(subject.value).press_enter()
        return self

    @allure.step("Выбираем штат")
    def set_state(self, value: str):
        controls.dropdown.select(browser.element('#state'), value)
        return self

    @allure.step("Выбираем город")
    def set_city(self, value: str):
        controls.dropdown.select(browser.element('#city'), value)
        return self

    @allure.step("Вводим имя")
    def type_first_name(self, value: str):
        browser.element("#firstName").type(value)
        return self

    @allure.step("Вводим фамилию")
    def type_last_name(self, value: str):
        browser.element("#lastName").type(value)
        return self

    @allure.step("Вводим почту")
    def type_user_email(self, value: str):
        browser.element("#userEmail").type(value)
        return self

    @allure.step('Выбираем день рождения')
    def set_date_Birth(self, year: str, month: str, day: str):
        birthday = DatePicker(browser.element('#dateOfBirthInput'))
        birthday.set_date(year, month, day)
        return self

    @allure.step("Вводим телефон")
    def type_user_phone_number(self, value: str):
        browser.element("#userNumber").type(value)
        return self

    # @allure.step("Выбор пола")
    # def set_gender(self, value: DatePicker):
    #     browser.all('[for^=gender-radio]').by(have.exact_text(value)).first.click()

    @allure.step("Выбираем файл")
    def add_pictures(self, picture: str):
        browser.element("#uploadPicture").send_keys(get_path_for_file(picture))
        return self

    @allure.step("Выбираем адрес")
    def type_current_address(self, currentAddress: str):
        browser.element("#currentAddress").type(currentAddress)
        return self

    def scroll_to_subject_input(self, scroll_into_view):
        browser.element("#subjectsInput").perform(scroll_into_view)
        return self

    @allure.step("Кликаем на кнопке подтверждения")
    def click_submit_button(self, click):
        browser.element("#submit").perform(click)
        return self

    @allure.step("Проверяем таблицу")
    def should_have_submitted(self, data):
        for row, value in data:
            table.find_text_in_table(row, value)
        return self
