from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

#DATABASE_URL
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dropbox')
def dropbox():
    return render_template('dropbox.html')

if __name__ == '__main__':
    app.run()
