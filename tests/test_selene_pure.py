from selene import be, by
from selene.support.shared.jquery_style import s
from .utils import *


def test_github():
    open_page("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys(requested_text)
    s(".header-search-input").submit()

    s(by.link_text(requested_text)).click()

    s("#issues-tab").click()

    s(by.partial_text(text_part)).should(be.visible)
