import allure
from allure_commons.types import Severity
from selene import have, be, command
from selene.support.shared import browser


from demoqa_e2e_tests.models import app
from demoqa_e2e_tests.models.controls import radio_button, checkbox
from demoqa_e2e_tests.models.controls.radio_button import SetOption
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

    app.registration_form.given_opened().type_first_name(
        yuri.first_name
    ).type_last_name(yuri.last_name).type_user_email(
        yuri.user_email
    ).type_user_phone_number(
        yuri.mobile
    )
    with allure.step('Выбираем пол'):
        set_gender = SetOption()
        set_gender.set_option()

    app.registration_form.set_date_Birth(yuri.year, yuri.month, yuri.day).add_subjects(
        yuri.subjects
    )
    with allure.step('Выбираем хобби'):
        checkbox.add_option('[id^=hobbies]', yuri.hobbies)

    app.registration_form.add_pictures(yuri.picture).type_current_address(
        yuri.currentAddress
    ).scroll_to_subject_input(command.js.scroll_into_view).set_state(
        yuri.state
    ).set_city(
        yuri.city
    ).click_submit_button(
        command.js.click
    )

    browser.element("#example-modal-sizes-title-lg").should(be.visible)

    app.registration_form.should_have_submitted(
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
