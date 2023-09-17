from selene import browser, have, command

url = 'https://reqres.in/'
check = ("LIST USERS", "SINGLE USER", "")
code = ("200", "201", "404")
response_code = '.response-code'
status = ' Статус кода 200'
# UI тесты
def test_code_pass(browser_setup):
    browser.open(url)
    browser.element("li[data-id='users']").perform(command.js.scroll_into_view).click()
    browser.element(response_code).should(have.exact_text(code[0]))
    print(f"LIST USERS / Статус кода: {code[0]}")
    browser.element("li[data-id='users-single']").perform(command.js.scroll_into_view).click()
    browser.element(response_code).should(have.exact_text(code[0]))
    print(f"SINGLE USER / Статус кода: {code[0]}")
    browser.element("li[data-id='unknown']").perform(command.js.scroll_into_view).click()
    browser.element(response_code).should(have.exact_text(code[0]))
    print(f"LIST RESOURCE /Статус кода: {code[0]}")





def test_code_invalid(browser_setup):
    browser.open(url)
    browser.element("li[data-id='users-single-not-found']").click()
    browser.element(".response-code.bad").should(have.text(code[2]))
    print(f"SINGLE USER NOT FOUND / Статус кода: {code[2]}")
    browser.element("li[data-id='unknown-single-not-found']").perform(command.js.scroll_into_view).click()
    browser.element(response_code).should(have.exact_text(code[2]))
    print(f"Статус кода: {code[2]}")



# browser.config.hold_driver_at_exit = True
