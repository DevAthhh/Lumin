from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fb12af43dfdb76374241475c69bc88ab'
login_manager = LoginManager(app)
