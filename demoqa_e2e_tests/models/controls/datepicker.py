import selene
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
