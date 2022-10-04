import allure
from selene import by, be
from selene.support.shared import browser
from allure import attachment_type
from utils import utils


@allure.step('Открыт gihub')
def browser_opened():
    browser.open('https://github.com/')
    allure.attach(
        "<h1>Браузер открыт</h1>", name="Html", attachment_type=attachment_type.HTML
    )


@allure.step('Поиск репозитория')
def searching_repository():
    browser.element('[name=q]').click()
    browser.element('[name=q]').send_keys('svmyhome/demoqa-e2e-tests')
    browser.element('[name=q]').submit()
    allure.attach(
        "Мы нашли репозиторий",
        name="Text",
        attachment_type=attachment_type.TEXT,
    )


@allure.step("Выбираем репозиторий")
def select_repository():
    browser.element(by.partial_link_text('svmyhome/demoqa-e2e-tests')).click()
    allure.attach.file(
        utils.get_path_for_file('tutorial.pdf'),
        name='This is PDF file',
        attachment_type=attachment_type.PDF,
    )


@allure.step("Выбирает вкаладку с Issue")
def select_tab_issue():
    browser.element('#issues-tab').click()


@allure.step("Issue 1 существует")
def issue_visible():
    browser.element('#issue_1_link').should(be.visible)
    allure.attach.file(
        utils.get_path_for_file('image.png'),
        name='Картинка типа мы его нашли )))',
        attachment_type=attachment_type.PNG,
    )
