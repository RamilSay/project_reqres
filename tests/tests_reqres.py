import pytest, requests
from selene import browser, be, have, command

#@pytest.fixture
#def browser_link(scope="session"):
#    browser.config.base_url = "https://reqres.in/"
#
#    yield
#
#    browser.quit()
    
def test_pozitive():
    browser.open('https://reqres.in/')
    browser.element('[data-http="get"]').perform(command.js.scroll_into_view).click()
    browser.element('[class="response"]').should(have.text('200'))
    assert browser.element('status_code == 200')




















