from selene import by, be
from selene.support.shared import browser


def test_issue_exist():
    browser.open('https://github.com/')
    browser.element('[name=q]').click()
    browser.element('[name=q]').send_keys('svmyhome/demoqa-e2e-tests')
    browser.element('[name=q]').submit()

    browser.element(by.partial_link_text('svmyhome/demoqa-e2e-tests')).click()
    browser.element('#issues-tab').click()
    browser.element('#issue_1_link').should(be.visible)
