from app import db
from sqlalchemy.dialects.postgresql import JSON

class Handlesdb(db.Model):
	__tablename__ = 'results'

	user_id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String())
	handles = db.Column(db.String());


	def __init__(self, user_id, name, handles):
		self.user_id = user_id
		self.name = name
		self.handles = handles


	def __repr__(self):
		return 'Handlesdb %r' %self.user_id	