from app import db
# from sqlalchemy.dialects.postgresql import JSON

# class Handlesdb(db.Model):
# 	__tablename__ = 'results'

# 	user_id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String())
# 	handles = db.Column(db.String());


# 	def __init__(self, user_id, name, handles):
# 		self.user_id = user_id
# 		self.name = name
# 		self.handles = handles


# 	def __repr__(self):
# 		return 'Handlesdb %r' %self.user_id	


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.BigInteger, unique = True)
	lastFetchedTweetId = db.Column(db.BigInteger(), unique= True)
	handles = db.relationship('Handle', backref='owner', lazy='dynamic')


	# def __init__(self, user_id, handles):
	# 	self.user_id = user_id
	# 	self.handles = handles


	# def __repr__(self):
	# 	return 'users %r' %self.user_id	

class Handle(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	handle_name = db.Column(db.String(20))
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))