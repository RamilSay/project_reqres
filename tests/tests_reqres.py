import requests
from selene import browser

endpoint = ('/api/users?page=2/', '/api/users/2', '/api/users/23')

#@pytest.fixture
#def browser_link(scope="session", autouse=True):
#    browser.config.base_url = "https://reqres.in/"
#
#    yield
#
#    browser.quit()
def tests_pozitive():
    url = 'https://reqres.in/'
    for point in endpoint:
        r = requests.get(url, params={'q': 'endpoint'})
        #r.status_code == r.raise_for_status()
        #r.raise_for_status()
        print(r)
        
    