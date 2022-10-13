from selene.support.shared import browser

from utils.utils import wait_and_remove_ads


def given_opened():
    browser.open("/webtables")
    wait_and_remove_ads('#adplus-anchor')


def add_new_record():
    browser.element("#addNewRecordButton").click()


def type_first_name(value: str):
    browser.element("#firstName").type(value)


def type_last_name(value: str):
    browser.element("#lastName").type(value)


def type_user_email(value: str):
    browser.element("#userEmail").type(value)


def type_age(value: int):
    browser.element("#age").type(value)


def type_salary(value: int):
    browser.element("#salary").type(value)


def type_departament(value: str):
    browser.element("#department").type("IT")


def click_submit():
    browser.element("#submit").click()


def edit_second_record():
    browser.element("#edit-record-2").click()


def edit_first_name(value: str):
    browser.element("#firstName").clear().type(value)


def edit_last_name(value: str):
    browser.element("#lastName").clear().type(value)


def edit_user_email(value: str):
    browser.element("#userEmail").clear().type(value)


def edit_age(value: int):
    browser.element("#age").clear().type(value)


def edit_salary(value: int):
    browser.element("#salary").clear().type(value)


def edit_departament(value: str):
    browser.element("#department").clear().type(value)


def delete_third_record():
    browser.element("#delete-record-3").click()
