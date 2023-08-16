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
	create_tables()  # Create database tables within the application context
	app.run(debug=True)


def route(param):
	return None
