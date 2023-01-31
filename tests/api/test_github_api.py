import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_non_exist(github_api):
    r = github_api.get_user('kateniko')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    #print(r)
    assert r['total_count'] == 26
    assert 'become-qa-auto-aug2020' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('kate_test_not_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_one_symbol_repo_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
