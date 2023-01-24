import pytest


class User:

    def __init__(self) -> None:
        self.name = "Kate"
        self.lastname = "Niko"


@pytest.fixture
def user():
    yield User()
    

def test_remove_name(user):
    user.name = ''
    assert user.name == ''

 
def test_name(user):
    assert user.name == "Kate"


def test_lastname(user):
    assert user.lastname == "Niko"
