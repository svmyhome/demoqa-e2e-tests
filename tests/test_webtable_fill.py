from selene import have
from selene.support.shared import browser

from demoqa_e2e_tests.models.pages import webtables_fill


def test_fill_in_web_tables():
    webtables_fill.given_opened()
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
