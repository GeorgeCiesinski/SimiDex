import hmac
from api.models.user import UserModel


"""
The authenticate and identity functions are required for Flask-JWT

hmac is used to compare strings safely
"""


# Authenticates user based on above dictionaries
def authenticate(username, password):
	"""
	Finds the user if exists and safely compares the password strings using hmac

	:param username: username
	:type username: str

	:param password: password
	:type password: str

	:return user: user object
	:rtype user: UserModel
	"""
	user = UserModel.find_by_username(username)
	# Compares two strings safely
	if user and hmac.compare_digest(user.password, password):
		return user


def identity(payload):
	"""
	Flask-JWT identity handler

	:param payload: Flask-JWT payload

	:return: user object
	:rtype: UserModel
	"""

	user_id = payload['identity']
	return UserModel.find_by_id(user_id)
