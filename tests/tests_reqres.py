import pytest, requests
from selene import browser, be, have, command

@pytest.fixture
def browser_link(scope="function", autouse=True):
    url = browser.config.base_url = "https://reqres.in/"

    yield

    browser.quit()
    
def test_pozitive(browser_link):
    browser.open('url')
    browser.element('[data-http="get"]').perform(command.js.scroll_into_view).click()
    response = browser.element('[class="response"]').should(have.text('200'))
    if response == 200:
        print(response)




















