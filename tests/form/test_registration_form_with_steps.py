import allure
from allure_commons.types import Severity
from selene import have, be, command
from selene.support.shared import browser

import demoqa_e2e_tests.models.controls.checkbox
import demoqa_e2e_tests.models.controls.datepicker
import demoqa_e2e_tests.models.controls.radio_button
from demoqa_e2e_tests.models.controls import datepicker
from demoqa_e2e_tests.models.pages import registration_form
from tests.test_data.users import yuri


# from demoqa_e2e_tests.models import pages as app # импорт страниц с синонимом app app.registration_form.add_hobbies()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarychev Vladimir")
@allure.epic("Это епик")
@allure.feature("Это фича")
@allure.story("Это история")
@allure.link("https://github.com", name="gitflow")
def test_registration_form_steps():

    registration_form.given_opened()

    browser.should(have.title("ToolsQA"))
    browser.element(".main-header").should(be.visible)

    registration_form.type_first_name(yuri.first_name)
    registration_form.type_last_name(yuri.last_name)

    registration_form.type_user_email(yuri.user_email)
    with allure.step('Выбираем пол'):
        demoqa_e2e_tests.models.controls.radio_button.set_option(
            '[for^=gender-radio]', yuri.gender.value
        )

    registration_form.type_user_phone_number(yuri.mobile)

    datepicker.set_date('#dateOfBirthInput', yuri.year, yuri.month, yuri.day)

    registration_form.add_subjects(yuri.subjects)
    with allure.step('Выбираем хобби'):
        demoqa_e2e_tests.models.controls.checkbox.add_option(
            '[id^=hobbies]', yuri.hobbies
        )

    registration_form.add_pictures(yuri.picture)

    registration_form.type_current_address(yuri.currentAddress)

    registration_form.scroll_to_subject_input(command.js.scroll_into_view)
    registration_form.set_state(yuri.state)
    registration_form.set_city(yuri.city)

    registration_form.click_submit_button(command.js.click)

    browser.element("#example-modal-sizes-title-lg").should(be.visible)

    registration_form.should_have_submitted(
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
