from flask_login import login_user

from User import User
from config import *


@login_manager.user_loader
def load_user(username):
    return User(username, '')

@app.route('/')
def auth():
    try:
        user = User('Egor', 'verydifficultpassword')
        login_user(user)
        return 'congratilation'
    except:
        return 'failed'

if __name__ == '__main__':
    app.run(debug=True, port=5000)