import pytest, requests
from selene import browser, be, have, command

#@pytest.fixture
#def browser_link(scope="function"):
#    browser.config.base_url = "https://reqres.in/"
#    browser.config.timeout = 7.0
#    browser.config.hold_driver_at_exit = True
#    browser.config.window_width = 1920
#    browser.config.window_height = 1080

def test_pozitive():
    browser.open('https://reqres.in')
    browser.element("li[data-id='users-single-not-found']").perform(command.js.scroll_into_view).click()
    browser.config.hold_driver_at_exit = True
    #response = browusersve.text('200'))
    #if response == 200:
    #    print(response)



    #
















