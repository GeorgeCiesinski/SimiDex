from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from api.security import authenticate, identity
from api.db import db

from api.resources.user import UserRegister

# Create and configure Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.database'  # Store database in database directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'temporary'  # Todo: Temporary secret_key. Move to permanent location
api = Api(app)


@app.before_first_request
def create_tables():
	"""
	Creates all tables before first request
	"""
	db.create_all()


jwt = JWT(app, authenticate, identity)


# Resources
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
	# Initialize SQLAlchemy object
	db.init_app(app)
	# Start app
	app.run(port=5000, debug=True)
