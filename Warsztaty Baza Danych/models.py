def hash_password(password, salt):
    pass


class User:
    def __init__(self, username="", password="", salt=""):
        self.id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)


    @property
    def id(self):
        return self.id

    @property
    def hashed_password(self):
        return self._hashed_password