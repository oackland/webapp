from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
	app = Flask(__name__)

	# Configure the app
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Initialize extensions
	db.init_app(app)
	migrate.init_app(app, db)

	# Import and register blueprints and routes
	import routes
	app.register_blueprint(routes.bp)

	return app
