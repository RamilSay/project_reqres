import pytest
from selene import browser, be, have, command


@pytest.fixture
def link():
    browser.config.base_url = 'https://reqres.in/'
    browser.config.timeout = 7.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_good(link):
    status_code = "200"
    browser.open('/')
    browser.config.hold_driver_at_exit = True
    browser.element("li[data-id='users']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.text(status_code))


def test_negative(link):
    status_code = "404"
    browser.open('/')
    browser.element("li[data-id='users-single-not-found']").click()
    browser.element(".response-code").should(have.text(status_code))

    # r = requests.status_codes = 200
    # if r != 200:
    #    print(f'Код верный', r)
    # else:
    #    print(f'Код неверный',r)
    #
    #    #requests.status_codes = 200

    #
