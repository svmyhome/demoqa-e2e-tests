import allure
from allure_commons.types import Severity
from allure import attachment_type

from demoqa_e2e_tests import utils


@allure.tag("allure")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarychev Vladimir")
@allure.epic("Все про АЛЛЮР")
@allure.feature("Прикрепление HTML")
@allure.story("Использование attachments")
@allure.link("https://github.com", name="gitflow")
def test_allure_attach_HTML():
    pass
    allure.attach(
        "<h1>Hello world</h1>", name="Html", attachment_type=attachment_type.HTML
    )


@allure.tag("allure")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Sarychev Vladimir")
@allure.epic("Все про АЛЛЮР")
@allure.feature("Прикрепление Текста")
@allure.story("Использование attachments")
@allure.link("https://github.com", name="gitflow")
def test_allure_attach_TXT():
    pass
    allure.attach(
        "Это просто прикрепленный текст",
        name="Text",
        attachment_type=attachment_type.TEXT,
    )


@allure.tag("allure")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Sarychev Vladimir")
@allure.epic("Все про АЛЛЮР")
@allure.feature("Прикрепление Текста")
@allure.story("Использование attachments")
@allure.link(
    "https://github.com", name="gitflow"
)  # TODO @allure.link("https://github.com", type="Requirment") type="Issue"
def test_allure_attach_TXT_file():
    allure.attach.file(
        utils.get_path_for_file('test1.txt'),
        name='This is Text file',
        attachment_type=attachment_type.TEXT,
    )
    pass


@allure.tag("allure")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Sarychev Vladimir")
@allure.epic("Все про АЛЛЮР")
@allure.feature("Прикрепление PDF")
@allure.story("Использование attachments")
@allure.link(
    "https://github.com", name="gitflow"
)  # TODO @allure.link("https://github.com", type="Requirment") type="Issue"
def test_allure_attach_PDF_file():
    allure.attach.file(
        utils.get_path_for_file('tutorial.pdf'),
        name='This is PDF file',
        attachment_type=attachment_type.PDF,
    )
    pass


@allure.tag("allure")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Sarychev Vladimir")
@allure.epic("Все про АЛЛЮР")
@allure.feature("Прикрепление PNG")
@allure.story("Использование attachments")
@allure.link(
    "https://github.com", name="gitflow"
)  # TODO @allure.link("https://github.com", type="Requirment") type="Issue"
def test_allure_attach_PNG_file():
    allure.attach.file(
        utils.get_path_for_file('image.png'),
        name='This is PNG file',
        attachment_type=attachment_type.PNG,
    )
    pass
