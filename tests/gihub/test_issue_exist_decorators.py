from demoqa_e2e_tests.models.pages import searching_issue


def test_issue_exist():

    searching_issue.browser_opened()
    searching_issue.searching_repository()
    searching_issue.select_repository()
    searching_issue.select_tab_issue()
    searching_issue.issue_visible()
