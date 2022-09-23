import allure
from selene import be, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from .utils import *


def test_github_with_allure_steps():

    with allure.step("Открываем главную страницу"):
        open_page("https://github.com")

    with allure.step("Ищем репозиторий в поиске"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys(requested_text)
        s(".header-search-input").submit()

    with allure.step("Переходим по найденной ссылке"):
        s(by.link_text(requested_text)).click()

    with allure.step("Переходим в Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем, что есть Issue #1"):
        s(by.partial_text(text_part)).should(be.visible)
