import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'  # SQLite database URL
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)


def create_tables():
	with app.app_context():
		db.create_all()


@app.route('/')
def home():
	return render_template('home.html')


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))  # Get the port from the environment variable or use 5000
	app.run(host='0.0.0.0', port=port)  # Listen on the correct port


def route(param):
	return None
