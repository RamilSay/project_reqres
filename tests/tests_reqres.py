import requests
from selene import browser, be, have, command

#@pytest.fixture
#def browser_link(scope="function"):
#    browser.config.base_url = "https://reqres.in/"
#    browser.config.timeout = 7.0
#    browser.config.hold_driver_at_exit = True
#    browser.config.window_width = 1920
#    browser.config.window_height = 1080

def test_pozitive():
    status_code = "404"
    browser.open('https://reqres.in')
    browser.element("li[data-id='users-single-not-found']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.text(status_code))

    #r = requests.status_codes = 200
    #if r != 200:
    #    print(f'Код верный', r)
    #else:
    #    print(f'Код неверный',r)
    #
    #    #requests.status_codes = 200

    #
















