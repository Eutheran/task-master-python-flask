from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
DB = SQLAlchemy(APP)


class Todo(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    content = DB.Column(DB.String(300), nullable=False)
    date_created = DB.Column(DB.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@APP.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    APP.run(debug=True)
