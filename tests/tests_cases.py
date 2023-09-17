import requests
from selene import browser

url = 'https://reqres.in/'
code = "200"
#response = " Статус кода соответствует запросу"

def browser_manage(browser_setup):
    browser.open(url)
def tests_requests(browser_manage):
    requests.get('/api/users?page=2').status_code = 200
    r = requests.status_codes = 200
    print(r)
# r = requests.status_codes = 200
    # if r != 200:
    #    print(f'Код верный', r)
    # else:
    #    print(f'Код неверный',r)
    #
    #    #requests.status_codes = 200