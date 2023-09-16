from selene import browser, have, command

url = 'https://reqres.in/'
code = "200"
response = " Статус кода соответствует запросу"
#UI тесты сайта
def test_good(browser_setup):
    browser.open(url)
    # browser.config.hold_driver_at_exit = True
    browser.element("li[data-id='users']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.text(code))
    print(response)

def test_negative(browser_setup):
    status_code = "404"
    browser.open(url)
    browser.element("li[data-id='users-single-not-found']").click()
    browser.element(".response-code.bad").should(have.text(status_code))
    print(response)

