import allure
from selene import be, by
from selene.support.shared.jquery_style import s
from .utils import *
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("ILYAZGO")
@allure.description("this is another descrition")
@allure.feature("Allure with decorating")
@allure.story("long")
@allure.link("https://github.com")
def test_github_decorate_allure_steps():
    open_main_page()
    searching_repo(requested_text)
    click_lynk(requested_text)
    go_to_issues()
    check_issue(text_part)


@allure.step("Открываем главную страницу")
def open_main_page():
    open_page("https://github.com")


@allure.step("Ищем репозиторий в поиске")
def searching_repo(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по найденной ссылке")
def click_lynk(repo):
    s(by.link_text(repo)).click()


@allure.step("Переходим в Issues")
def go_to_issues():
    s("#issues-tab").click()


@allure.step("Проверяем, что есть Issue #1")
def check_issue(name):
    s(by.partial_text(name)).should(be.visible)
