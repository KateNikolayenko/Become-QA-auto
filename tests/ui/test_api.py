import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == "Kate"

@pytest.mark.check
def test_lastname(user):
    assert user.lastname == "Niko"
