from twitter import *
from flask import Flask, request, render_template, redirect, abort, flash, jsonify, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)   # create our flask app
db = SQLAlchemy(app)

# configure Twitter API
CONSUMER_KEY='WOWfe9QRArl5beDczAMfRP4jU'
CONSUMER_SECRET='XBYI52DvlWNBzqMqpfzk98gxQLwFqUKeNpgJp1qTvIbfMv9hIH'
OAUTH_TOKEN='560955859-MCmIMQ6k5UgVvAxA6fXj7MKBisWmTuUibzpGRI9m'
OAUTH_SECRET='kJkNlPDjZZHWxLsQ6gBSu2tIEj8oEqegLqL9jqI3PTPBX'

# Authenticating with Twitter.
twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
timestamp = datetime.now().replace(minute = 0)

# setting up Config files 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# models
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.String, unique = True)
	handles = db.relationship('Handle', backref='owner', lazy='dynamic')

class Handle(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	handle_name = db.Column(db.String(20))
	lastFetchedTweetId = db.Column(db.String(), unique= True)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# routes
@app.route('/', methods=['GET', 'POST'])
def main():
	counter = 0;
	myvar = 0
	empList = []
	empDict = {}
	handlesList = []
	r = User.query.filter_by(user_id="1").first() # "1" because you are the only one using this app.

	
	# TODO: add authentication to identify user.
	# Probabliy facebook login authentication 
	# then the user_id value will be facebook user id which will always be the same.


	for i in r.handles.all():# get all the handles to be checked from the database.
		counter = 0	
		itpTweets = twitter.statuses.user_timeline(screen_name=i.handle_name, since_id=i.lastFetchedTweetId)
		for t in itpTweets:
			if(counter==0): # Getting the latest tweet-id from a particular handle.
				latesttweet  = t['id']
				counter += 1
			else:
				counter += 1
		empDict = {
		"name" : i.handle_name,
		"count" : counter
		}

		# adding
		empList.append(empDict)	
		if(counter > 0): # If there are any new tweets, save the lastest tweet-id to database.
			Handle.query.filter_by(handle_name=i.handle_name).update({"lastFetchedTweetId":latesttweet})
			db.session.commit()

	return jsonify(empList)

@app.route('/login/', methods=['GET','POST'])
def login():
	return render_template('login.html')

@app.route('/addhandle', methods=['GET', 'POST'])
def addinghandle():
	return render_template('addhandle.html')	

@app.route('/postHandle', methods=['POST'])
def addHandle():
	latestTweetID = 0
	myowner = User.query.filter_by(user_id=request.form['user_id']).first()
	new_handle = request.form['handle']
	itpTweets = twitter.statuses.user_timeline(screen_name=new_handle, count = 1)
	latestTweetID = itpTweets[0]['id']
	myhandle = Handle(handle_name=new_handle, lastFetchedTweetId = latestTweetID, owner = myowner)
	db.session.add(myhandle)
	db.session.commit()
	return redirect(url_for('addinghandle'))


    
# --------- Server On ----------
# start the webserver

if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)