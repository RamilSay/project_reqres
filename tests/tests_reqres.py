import pytest
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
    browser.element('class="active"').perform(command.js.scroll_into_view)
    #browser.element(".li[@class='active']").should(have.text('response-code, 200'))




















