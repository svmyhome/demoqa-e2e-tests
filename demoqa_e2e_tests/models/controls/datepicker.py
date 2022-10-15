import allure
import selene
from selene import have
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_year(self, year: str):
        browser.element('.react-datepicker__year-select').send_keys(year)

    def set_month(self, month: str):
        browser.element('.react-datepicker__month-select').send_keys(month)

    def set_day(self, day: str):
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()

    def set_date(self, year: str, month: str, day: str):
        self.element.click()
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)


#
# def alternative_set_year(year: str):
#     browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
#
#
# def alternative_set_month(month: str):
#     browser.element('.react-datepicker__month-select').all('option').by(
#         have.exact_text(month)
#     ).first.click()
#
#
# def alternative_set_day(day: str):
#     browser.element(
#         f'.react-datepicker__day--0{day}' f':not(.react-datepicker__day--outside-month)'
#     ).click()
#
#
# @allure.step("Выбор даты")
# def alternative_set_date(year: str, month: str, day: str):
#     browser.element('#dateOfBirthInput').click()
#     alternative_set_year(year)
#     alternative_set_month(month)
#     alternative_set_day(day)
