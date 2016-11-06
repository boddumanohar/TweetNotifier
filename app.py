import os
import time
from twitter import *
from flask import Flask, request, render_template, redirect, abort, flash, jsonify, url_for
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# # from models import User, Handle
# import models
# # import models.Handle



app = Flask(__name__)   # create our flask app

# configure Twitter API

CONSUMER_KEY='WOWfe9QRArl5beDczAMfRP4jU'
CONSUMER_SECRET='XBYI52DvlWNBzqMqpfzk98gxQLwFqUKeNpgJp1qTvIbfMv9hIH'
OAUTH_TOKEN='560955859-MCmIMQ6k5UgVvAxA6fXj7MKBisWmTuUibzpGRI9m'
OAUTH_SECRET='kJkNlPDjZZHWxLsQ6gBSu2tIEj8oEqegLqL9jqI3PTPBX'


twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
timestamp = datetime.now().replace(minute = 0)

# setting up Config files 

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://manoharreddy@localhost/taskcprecog'

# setting up DB 

db = SQLAlchemy(app)

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

		# def __init__(self, handle_name, owner):
		# 	self.handle_name = handle_name
		# 	self.owner = owner

# setting up routes 
# gets user_id by default 

@app.route('/', methods=['GET', 'POST'])
def main():
	counter = 0;
	myvar = 0

	# lastFetchedTweetId = 791483941886697500
	# handle_name = 'aviaryan123'

	# lastFetchedTweetId = User.query.filter_by(lastFetchedTweetId).first()
	# lastFetchedTweetId = lastFetchedTweetId.Users.all()

	# user_id = request.form['user_id']
	r = Users.query.filter_by(user_id=123456).first()
	for handle_name in r.handles.all():
		itpTweets = twitter.statuses.user_timeline(screen_name=handle_name, since_id=lastFetchedTweetId)
		r = {}
		for t in itpTweets:
			if(counter==0):
				myvar  = t['id']
				counter += 1
			else:	 
				counter += 1

	# update the table with the latestTweetID
	# latestTweetID = myvar
	# stmt = update(Users).where(users.user_id==user_id).\
 #        values(lastFetchedTweetId=latestTweetID)

	return  jsonify({"tweets":counter})


@app.route('/login/', methods=['GET','POST'])
def login():
	return render_template('login.html')

@app.route('/addhandle', methods=['GET', 'POST'])
def addinghandle():
	return render_template('addhandle.html')	

@app.route('/postHandle', methods=['POST'])
def addHandle():
	# db.session.delete(models.User.query.filter_by(user_id=request.form['user_id']).first())
	myowner = User.query.filter_by(user_id=request.form['user_id']).first()
	new_handle = request.form['handle']
	myhandle = Handle(handle_name=new_handle, owner = myowner)
	db.session.add(myhandle)
	db.session.commit()
	return redirect(url_for('addinghandle'))

			
    
# --------- Server On ----------
# start the webserver

if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)