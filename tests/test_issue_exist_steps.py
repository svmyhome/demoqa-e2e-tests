import allure

from selene import by, be
from selene.support.shared import browser


def test_issue_exist():

    with allure.step('Открыт gihub'):
        browser.open('https://github.com/')

    with allure.step('Поиск репозитория'):
        browser.element('[name=q]').click()
        browser.element('[name=q]').send_keys('svmyhome/demoqa-e2e-tests')
        browser.element('[name=q]').submit()

    with allure.step("Выбираем репозиторий"):
        browser.element(by.partial_link_text('svmyhome/demoqa-e2e-tests')).click()

    with allure.step("Выбирает вкаладку с Issue"):
        browser.element('#issues-tab').click()

    with allure.step("Issue 1 существует"):
        browser.element('#issue_1_link').should(be.visible)
