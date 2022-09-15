import os
from selene import have, be
from selene.support.shared import browser


def wait_and_remove_ads():
    ads = browser.all('#RightSide_Advertisement')
    '''ждет чтобы все отобразилась, одна реклама и если дожидается то удаляет иначе скипает'''
    if ads.wait_until(have.size_greater_than_or_equal(1)):
        browser.execute_script(
            'document.querySelectorAll("#RightSide_Advertisement").forEach(element => element.remove())')


def get_path_for_file():
    ''' Находим текущий путь, вычитаем папку с тестами, добавляем папку с ресурсами и файл'''
    # abs_file_path = os.path.abspath('../resources/test.txt')
    current_path = os.path.dirname(os.path.abspath(__file__))
    root_path_list = os.path.split(current_path)
    root_path = root_path_list[0]
    file_path = os.path.join(root_path, 'resources', 'test.txt')
    return file_path


def test_fill_in_practice_form():
    browser.open('/automation-practice-form')
    wait_and_remove_ads()
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(be.visible)
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivan@Ivanov.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="2019"]').click()
    browser.element('.react-datepicker__month-select [value="5"]').click()
    browser.element('[aria-label="Choose Friday, June 28th, 2019"]').click()
    browser.element('#subjectsInput').type('history').press_enter().type('Ch').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(get_path_for_file())
    browser.element('#currentAddress').type(' Text text text')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(be.visible)
    '''выбираются все ячейки из таблицы с классом .table-responsive'''
    browser.all('.table-responsive td').should(
        have.texts('Student Name', 'Ivan Ivanov', 'Student Email', 'Ivan@Ivanov.ru', 'Gender', 'Male', 'Mobile',
                   '0123456789', 'Date of Birth', '28 June,2019', 'Subjects', 'History, Chemistry', 'Hobbies',
                   'Sports, Music', 'Picture', 'test.txt', 'Address', 'Text text text', 'State and City',
                   'Haryana Panipat'))


def test_fill_in_web_tables():
    browser.open('/webtables')
    wait_and_remove_ads()
    browser.should(have.title('ToolsQA'))
    browser.element('#addNewRecordButton').click()
    browser.element('#registration-form-modal').should(be.visible)
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivan@Ivanov.ru')
    browser.element('#age').type(33)
    browser.element('#salary').type(500000)
    browser.element('#department').type('IT')
    browser.element('#submit').click()
    browser.element('.main-header').should(be.visible)
    browser.element('#edit-record-2').click()
    browser.element('#registration-form-modal').should(be.visible)
    browser.element('#firstName').clear().type('Petr')
    browser.element('#lastName').clear().type('Petrov')
    browser.element('#userEmail').clear().type('Petr@Petrov.ru')
    browser.element('#age').clear().type(83)
    browser.element('#salary').clear().type(800000)
    browser.element('#department').clear().type('ITR')
    browser.element('#submit').click()
    browser.element('.main-header').should(be.visible)
    browser.element('#delete-record-3').click()
