import json

import allure
from allure import attachment_type
from allure_commons.types import Severity
from selene import have, be, command
from selene.support.shared import browser

from demoqa_e2e_tests.models.pages import registration_form
from utils.utils import get_path_for_file, wait_and_remove_ads
from tests.test_data.users import yuri


def test_registration_form():

    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'Sarychev')
    allure.dynamic.feature('Это фича 3')
    allure.dynamic.link('https://Jira.com', name='cjsdcnjsdnc')
    with allure.step('Открываем страницу регистрации'):
        browser.open('/automation-practice-form')
        wait_and_remove_ads('#adplus-anchor')
        allure.attach('Text content', name='Text', attachment_type=attachment_type.TEXT)

    with allure.step('Проверяем что открылась та страница'):
        browser.should(have.title('ToolsQA'))
        browser.element('.main-header').should(be.visible)
        allure.attach(
            '<h1>Hello world</h1>', name='Html', attachment_type=attachment_type.HTML
        )

    with allure.step('Заполняем ФИО и почту'):
        browser.element('#firstName').type(yuri.first_name)
        browser.element('#lastName').type(yuri.last_name)
        browser.element('#userEmail').type(yuri.user_email)
        allure.attach(
            json.dumps({'first': 1, 'second': 2}),
            name='Json',
            attachment_type=attachment_type.JSON,
        )

    with allure.step('Выбираем пол'):
        browser.all('[for^=gender-radio]').by(
            have.exact_text(yuri.gender.value)
        ).first.click()

    with allure.step('Вводим мобильник'):
        browser.element('#userNumber').type(yuri.mobile)

    with allure.step('Выбираем дату'):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(yuri.year)
        browser.element('.react-datepicker__month-select').send_keys(yuri.month)
        browser.element(
            f'.react-datepicker__day--0{yuri.day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()

    with allure.step('Выбираем предметы'):
        registration_form.add_subjects(yuri.subjects)
    with allure.step('Выбираем хобби'):
        registration_form.add_hobbies(yuri.hobbies)

    with allure.step('Загружаем картинку'):
        browser.element('#uploadPicture').send_keys(get_path_for_file('test.txt'))

    with allure.step('Вводим текущий адрес'):
        browser.element('#currentAddress').type(yuri.currentAddress)

    with allure.step('Вводим штат и город'):
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
        registration_form.set_state(yuri.state)
        registration_form.set_city(yuri.city)

    with allure.step('Жмем на кнопку подтверждения'):
        browser.element('#submit').perform(command.js.click)

    with allure.step('Проверяем что открылось окно с результатами'):
        browser.element('#example-modal-sizes-title-lg').should(be.visible)

    def should_have_table(rows):
        for row, value in rows:
            dialog = browser.element('.modal-content').element('.table')
            rows = dialog.all('tbody tr')
            rows.by(have.text(row)).first.all('td')[1].should(have.exact_text(value))

    with allure.step('Проверяем результаты в таблице'):
        should_have_table(
            [
                ('Student Name', f'{yuri.first_name} {yuri.last_name}'),
                ('Student Email', yuri.user_email),
                ('Gender', yuri.gender.value),
                ('Mobile', yuri.mobile),
                ('Date of Birth', f'{yuri.day} {yuri.month},{yuri.year}'),
                (
                    'Subjects',
                    f'{yuri.subjects[0].value}, {yuri.subjects[1].value}',
                ),
                ('Hobbies', 'Sports, Music'),
                ('Picture', 'test.txt'),
                ('Address', yuri.currentAddress),
                ('State and City', f'{yuri.state} {yuri.city}'),
            ]
        )
