import allure
from allure_commons.types import Severity

from demoqa_e2e_tests.models.pages import searching_issue


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarychev")
@allure.epic("Использование всех функций Аллюр")
@allure.story("Я пытаюсь использовать максимально много от Аллюра")
@allure.feature("Ищем репозиторий и размечаем все по максимуму аллюром")
@allure.link("https://github.com", name="demoqa-e2e-tests")
def test_issue_exist():

    searching_issue.browser_opened()
    searching_issue.searching_repository()
    searching_issue.select_repository()
    searching_issue.select_tab_issue()
    searching_issue.issue_visible()
