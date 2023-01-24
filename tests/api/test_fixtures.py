class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None
    

    def create(self):
        self.name = "Kate"
        self.lastname = "Niko"

    def remove(self):
        self.name = ''
        self.lastname = ''

def test_change_name():
    user = User()
    user.create()

    assert user.name == "Kate"
    user.remove()

def test_change_lastname():
    user = User()
    user.create()

    assert user.second_name == "Niko"
    user.remove()
    