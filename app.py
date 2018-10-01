from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import Result

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello_world():
    result = Result('https://google.com', 'Hello World', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    print(result.__repr__)
    return render_template('index.html')

@app.route('/dropbox')
def dropbox():
    return render_template('dropbox.html')

if __name__ == '__main__':
    app.run()
