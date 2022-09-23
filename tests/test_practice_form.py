from selene import have, be, command
from selene.support.shared import browser

from demoqa_e2e_tests.utils import get_path_for_file
from tests.test_data import users


def wait_and_remove_ads():
    ads = browser.all("#adplus-anchor")
    '''ждет чтобы все отобразилась, одна реклама и если дожидается то удаляет иначе скипает'''
    if ads.wait_until(have.size_greater_than_or_equal(1)):
        browser.execute_script(
            'document.querySelectorAll("#adplus-anchor").forEach(element => element.remove())'
        )


def test_fill_in_practice_form():
    browser.open("/automation-practice-form")
    browser.execute_script(
        'document.querySelectorAll(".GoogleActiveViewElement").forEach(element => element.remove())'
    )
    wait_and_remove_ads()
    browser.should(have.title("ToolsQA"))
    browser.element(".main-header").should(be.visible)
    browser.element("#firstName").type(users.yuri.first_name)
    browser.element("#lastName").type(users.yuri.last_name)
    browser.element("#userEmail").type(users.yuri.user_email)
    browser.all('[for^=gender-radio]').by(
        have.exact_text(users.yuri.gender.value)
    ).first.click()
    '''
    OR
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.click()
    '''
    browser.element("#userNumber").type(users.yuri.mobile)
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select').send_keys(users.yuri.year)
    browser.element('.react-datepicker__month-select').send_keys(users.yuri.month)
    browser.element(
        f'.react-datepicker__day--0{users.yuri.day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    '''
    OR
    browser.element('.react-datepicker__year-select [value="2019"]').click()
    browser.element('.react-datepicker__month-select [value="5"]').click()
    browser.element('[aria-label="Choose Friday, June 28th, 2019"]').click()
    '''

    for subject in users.yuri.subjects:
        browser.element("#subjectsInput").type(subject.value).press_enter()
    '''
    OR
    browser.element("#subjectsInput").type("history").press_enter().type(
        "Ch"
    ).press_enter()'''
    for hobby in users.yuri.hobbies:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()
    browser.element("#uploadPicture").send_keys(get_path_for_file('test.txt'))
    browser.element("#currentAddress").type(users.yuri.currentAddress)
    browser.element("#subjectsInput").perform(command.js.scroll_into_view)
    browser.element("#state").click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(users.yuri.state)
    ).first.click()
    browser.element("#city").click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(users.yuri.city)
    ).first.click()
    '''
    OR
    browser.element("#react-select-3-input").type("Haryana").press_enter()
    browser.element("#city").click()
    browser.element("#react-select-4-input").type("Panipat").press_enter()
    '''
    browser.element("#submit").perform(command.js.click)
    browser.element("#example-modal-sizes-title-lg").should(be.visible)

    def should_have_table(rows):
        for row, value in rows:
            dialog = browser.element('.modal-content').element('.table')
            rows = dialog.all('tbody tr')
            rows.by(have.text(row)).first.all('td')[1].should(have.exact_text(value))

    print(f'{hobby.Sports.value}, {hobby.Music.value}')
    should_have_table(
        [
            ('Student Name', f'{users.yuri.first_name} {users.yuri.last_name}'),
            ('Student Email', users.yuri.user_email),
            ('Gender', users.yuri.gender.value),
            ('Mobile', users.yuri.mobile),
            ('Date of Birth', f'{users.yuri.day} {users.yuri.month},{users.yuri.year}'),
            ('Subjects', f'{subject.Maths.value}, {subject.History.value}'),
            ('Hobbies', 'Sports, Music'),
            ('Picture', 'test.txt'),
            ('Address', users.yuri.currentAddress),
            ('State and City', f'{users.yuri.state} {users.yuri.city}'),
        ]
    )

    '''выбираются все ячейки из таблицы с классом .table-responsive'''
    # browser.all(".table-responsive td").should(
    #     have.texts(
    #         'Student Name',
    #         'yuri Ivanov',
    #         'Student Email',
    #         'Ivanov@mail.ru',
    #         'Gender',
    #         'Male',
    #         'Mobile',
    #         '1234567890',
    #         'Date of Birth',
    #         '30 September,2015',
    #         'Subjects',
    #         'Maths, History',
    #         'Hobbies',
    #         'Sports, Music',
    #         'Picture',
    #         'test.txt',
    #         'Address',
    #         'chbsdhjcb cdsjbcjsdbc jcsdjcndncj',
    #         'State and City',
    #         'Uttar Pradesh Lucknow'
    #     )
    # )


def test_fill_in_web_tables():
    browser.open("/webtables")
    wait_and_remove_ads()
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
