from selene import have, be
from selene.support.shared import browser

from demoqa_e2e_tests.models.pages import registration_form, webtables_fill


def test_fill_in_web_tables():
    webtables_fill.given_opened()

    browser.should(have.title("ToolsQA"))

    webtables_fill.add_new_record()

    browser.element("#registration-form-modal").should(be.visible)

    webtables_fill.type_first_name("Ivan")

    webtables_fill.type_last_name("Ivanov")

    webtables_fill.type_user_email("Ivan@Ivanov.ru")

    webtables_fill.type_age(33)

    webtables_fill.type_salary(500000)

    webtables_fill.type_departament("IT")

    webtables_fill.click_submit()

    browser.element(".main-header").should(be.visible)

    webtables_fill.edit_second_record()

    browser.element("#registration-form-modal").should(be.visible)

    webtables_fill.edit_first_name("Petr")

    webtables_fill.edit_last_name("Petrov")

    webtables_fill.edit_user_email("Petr@Petrov.ru")

    webtables_fill.edit_age(83)

    webtables_fill.edit_salary(800000)

    webtables_fill.edit_departament("ITR")

    webtables_fill.click_submit()

    browser.element(".main-header").should(be.visible)

    webtables_fill.delete_third_record()
