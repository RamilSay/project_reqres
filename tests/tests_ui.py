from selene import browser, have, command

url = 'https://reqres.in/'
check = ("LIST USERS", "SINGLE USER", "")
code = ("200", "201", "204", "404", "400")


# UI тесты
def test_code_pass(browser_setup):
    browser.open(url)
    browser.element("li[data-id='users']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"\nGET LIST USERS / Статус кода: {code[0]}")

    browser.element("li[data-id='users-single']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"GET SINGLE USER / Статус кода: {code[0]}")

    browser.element("li[data-id='unknown']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"GET LIST RESOURCE /Статус кода: {code[0]}")

    browser.element("li[data-id='unknown-single']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"GET SINGLE RESOURCE /Статус кода: {code[0]}")

    browser.element("li[data-id='post']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[1]))
    print(f"POST CREATE / Статус кода: {code[1]}")

    browser.element("li[data-id='put']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"PUT UPDATE / Статус кода: {code[0]}")

    browser.element("li[data-id='patch']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"PATCH UPDATE / Статус кода: {code[0]}")

    browser.element("li[data-id='register-successful']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"POST REGISTER - SUCCESSFUL / Статус кода: {code[0]}")

    browser.element("li[data-id='login-successful']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"POST LOGIN - SUCCESSFUL / Статус кода: {code[0]}")

    browser.element("li[data-id='delay']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code").should(have.exact_text(code[0]))
    print(f"GET DELAYED RESPONSE / Статус кода: {code[0]}")


def test_negative(browser_setup):
    browser.open(url)
    browser.element("li[data-id='users-single-not-found']").click()
    browser.element(".response-code.bad").should(have.text(code[3]))
    print(f"\nGET SINGLE USER NOT FOUND / Статус кода: {code[3]}")

    browser.element("li[data-id='unknown-single-not-found']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code.bad").should(have.exact_text(code[3]))
    print(f"GET SINGLE RESOURCE NOT FOUND / Статус кода: {code[3]}")

    browser.element("li[data-id='delete']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code.bad").should(have.exact_text(code[2]))
    print(f"DELETE / Статус кода: {code[2]}")

    browser.element("li[data-id='register-unsuccessful']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code.bad").should(have.exact_text(code[4]))
    print(f"POST REGISTER - UNSUCCESSFUL / Статус кода: {code[4]}")

    browser.element("li[data-id='login-unsuccessful']").perform(command.js.scroll_into_view).click()
    browser.element(".response-code.bad").should(have.exact_text(code[4]))
    print(f"POST LOGIN - UNSUCCESSFUL / Статус кода: {code[4]}")


