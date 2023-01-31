import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Responce is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f'Response is {r.text}'.encode("utf-8"))

#@pytest.mark.http
#def test_third_request():
    #r = requests.get('https://api.github.com/users/defunkt')
    #print(f'Response Body is {r.json()}'.encode("utf-8"))
    #print(f'Response Status code is {r.status_code()}')
    #print(f'Response Headers is {r.headers()}')

@pytest.mark.http
def test_fourth_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200 
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404 