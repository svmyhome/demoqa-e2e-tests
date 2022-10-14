import allure
import selene
from selene import have
from selene.support.shared import browser


def set_year(year: str):
    browser.element('.react-datepicker__year-select').send_keys(year)


def set_month(month: str):
    browser.element('.react-datepicker__month-select').send_keys(month)


def set_day(day: str):
    browser.element(
        f'.react-datepicker__day--0{day}' f':not(.react-datepicker__day--outside-month)'
    ).click()


@allure.step("Выбор даты")
def set_date(element: selene.Element, year: str, month: str, day: str):
    browser.element("#dateOfBirthInput").click()
    set_year(year)
    set_month(month)
    set_day(day)


def alternative_set_year(year: str):
    browser.element(f'.react-datepicker__year-select [value="{year}"]').click()


def alternative_set_month(month: str):
    browser.element('.react-datepicker__month-select').all('option').by(
        have.exact_text(month)
    ).first.click()


def alternative_set_day(day: str):
    browser.element(
        f'.react-datepicker__day--0{day}' f':not(.react-datepicker__day--outside-month)'
    ).click()


@allure.step("Выбор даты")
def alternative_set_date(year: str, month: str, day: str):
    browser.element('#dateOfBirthInput').click()
    alternative_set_year(year)
    alternative_set_month(month)
    alternative_set_day(day)
