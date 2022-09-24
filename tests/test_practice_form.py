from selene import have, be, command
from selene.support.shared import browser

from demoqa_e2e_tests.models.pages import registration_form
from demoqa_e2e_tests.models.pages.registration_form import wait_and_remove_ads
from demoqa_e2e_tests.utils import get_path_for_file
from demoqa_e2e_tests.models.controls import dropdown
from tests.test_data.users import yuri
from demoqa_e2e_tests import (
    models,
)  # если в init прописать рути то можно собрать единую точку для вриложения

# from demoqa_e2e_tests.models import pages as app # импорт страниц с синонимом app app.registration_form.add_hobbies()


def test_registration_form():
    registration_form.given_opened()
    browser.should(have.title("ToolsQA"))
    browser.element(".main-header").should(be.visible)
    browser.element("#firstName").type(yuri.first_name)
    browser.element("#lastName").type(yuri.last_name)
    browser.element("#userEmail").type(yuri.user_email)
    browser.all('[for^=gender-radio]').by(
        have.exact_text(yuri.gender.value)
    ).first.click()
    '''
    OR
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.click()
    '''
    browser.element("#userNumber").type(yuri.mobile)
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select').send_keys(yuri.year)
    browser.element('.react-datepicker__month-select').send_keys(yuri.month)
    browser.element(
        f'.react-datepicker__day--0{yuri.day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    '''
    OR
    browser.element('.react-datepicker__year-select [value="2019"]').click()
    browser.element('.react-datepicker__month-select [value="5"]').click()
    browser.element('[aria-label="Choose Friday, June 28th, 2019"]').click()
    '''

    registration_form.add_subjects(yuri.subjects)

    '''
    OR
    browser.element("#subjectsInput").type("history").press_enter().type(
        "Ch"
    ).press_enter()'''

    registration_form.add_hobbies(yuri.hobbies)

    browser.element("#uploadPicture").send_keys(get_path_for_file('test.txt'))
    browser.element("#currentAddress").type(yuri.currentAddress)
    browser.element("#subjectsInput").perform(command.js.scroll_into_view)

    registration_form.set_state(yuri.state)
    registration_form.set_city(yuri.city)

    browser.element("#submit").perform(command.js.click)
    browser.element("#example-modal-sizes-title-lg").should(be.visible)

    def should_have_table(rows):
        for row, value in rows:
            dialog = browser.element('.modal-content').element('.table')
            rows = dialog.all('tbody tr')
            rows.by(have.text(row)).first.all('td')[1].should(have.exact_text(value))

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

    '''
    OR
        browser.all(".table-responsive td").should(
        have.texts(
            'Student Name',
            'yuri Ivanov',
            'Student Email',
            'Ivanov@mail.ru',
            'Gender',
            'Male',
            'Mobile',
            '1234567890',
            'Date of Birth',
            '30 September,2015',
            'Subjects',
            'Maths, History',
            'Hobbies',
            'Sports, Music',
            'Picture',
            'test.txt',
            'Address',
            'chbsdhjcb cdsjbcjsdbc jcsdjcndncj',
            'State and City',
            'Uttar Pradesh Lucknow'
        )
    )
    '''


def test_fill_in_web_tables():
    browser.open("/webtables")
    registration_form.wait_and_remove_ads()
    browser.should(have.title("ToolsQA"))
    browser.element("#addNewRecordButton").click()
    browser.element("#registration-form-modal").should(be.visible)
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("Ivan@Ivanov.ru")
    browser.element("#age").type(33)
    browser.element("#salary").type(500000)
    browser.element("#department").type("IT")
    browser.element("#submit").click()
    browser.element(".main-header").should(be.visible)
    browser.element("#edit-record-2").click()
    browser.element("#registration-form-modal").should(be.visible)
    browser.element("#firstName").clear().type("Petr")
    browser.element("#lastName").clear().type("Petrov")
    browser.element("#userEmail").clear().type("Petr@Petrov.ru")
    browser.element("#age").clear().type(83)
    browser.element("#salary").clear().type(800000)
    browser.element("#department").clear().type("ITR")
    browser.element("#submit").click()
    browser.element(".main-header").should(be.visible)
    browser.element("#delete-record-3").click()
