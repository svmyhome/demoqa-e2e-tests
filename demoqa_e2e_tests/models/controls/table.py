from selene import have

from demoqa_e2e_tests.models.controls import modal


def find_text_in_table(row, value):
    rows = modal.dialog.all('tbody tr')
    rows.by(have.text(row)).first.all('td')[1].should(have.exact_text(value))
