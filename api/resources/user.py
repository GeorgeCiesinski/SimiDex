from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_kwargs

from api.models.user import UserModel


class UserRegister(Resource):

	@use_kwargs({
		"username": fields.String(required=True),
		"password": fields.String(required=True)
	},
		location='json')
	def post(self, **kwargs):
		"""
		Registers a new user and posts the new User object to the database.

		Kwargs:
			username (string): username
			password (string): password

		:return: message, http status
		"""

		# Checks if user already exists
		if UserModel.find_by_username(kwargs['username']):
			return {"message": "A user with that username already exists"}, 400

		user = UserModel(**kwargs)
		user.save_to_db()

		return {"message": "User created successfully."}, 201
