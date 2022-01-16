from api.db import db


class UserModel(db.Model):

	# Table name
	__tablename__ = 'users'

	# Columns
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def save_to_db(self):
		"""
		Adds object to session and commits
		"""

		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_username(cls, username):
		"""
		Finds user object by username

		:param username: username
		:type username: str

		:return: user object
		:rtype: UserModel
		"""

		return cls.query.filter_by(username=username).first()

	@classmethod
	def find_by_id(cls, _id):
		"""
		Finds user object by _id

		:param _id: _id
		:type _id: int

		:return: user object
		:rtype: UserModel
		"""

		return cls.query.filter_by(id=_id).first()  # same as SELECT * FROM items WHERE id=_id
