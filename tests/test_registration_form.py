from selene import have, be, command
from selene.support.shared import browser

from demoqa_e2e_tests.models.pages import registration_form
from demoqa_e2e_tests.utils import get_path_for_file
from tests.test_data.users import yuri


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
