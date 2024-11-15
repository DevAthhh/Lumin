from flask_login import UserMixin
from datetime import datetime

class User(UserMixin):
    def __init__(self, username, psw):
        self.username = username
        self.psw = psw
        self.date = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username