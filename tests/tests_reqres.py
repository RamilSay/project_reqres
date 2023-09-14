import pytest
from selene import browser, be, have, command


@pytest.fixture
def browser_link(scope="session"):
    browser.config.base_url = "https://reqres.in/"

    yield

    browser.quit()
    
def test_pozitive(browser_link):
    browser.open('/')
    browser.element(".li[@class='active']").perform(command.js.scroll_into_view)
    browser.element(".li[@class='active']").should(have.text('response-code, 200'))





    #if r.status_code == 400:
    #    print((r.status_code)'Верно')
    #else:
    #    print(r.status_code)






        #print(data)
        #r.status_code == r.raise_for_status()
        #r.raise_for_status()


