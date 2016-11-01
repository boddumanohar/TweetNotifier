import os
import time
from twitter import *
from flask import Flask, request, render_template, redirect, abort, flash, jsonify
from datetime import datetime
# from flask_social import Social
# from flask_social import SQLAlchemyConnectionDatastore

app = Flask(__name__)   # create our flask app

CONSUMER_KEY='WOWfe9QRArl5beDczAMfRP4jU'
CONSUMER_SECRET='XBYI52DvlWNBzqMqpfzk98gxQLwFqUKeNpgJp1qTvIbfMv9hIH'
OAUTH_TOKEN='560955859-MCmIMQ6k5UgVvAxA6fXj7MKBisWmTuUibzpGRI9m'
OAUTH_SECRET='kJkNlPDjZZHWxLsQ6gBSu2tIEj8oEqegLqL9jqI3PTPBX'


# app.config['SOCIAL_FACEBOOK'] = {
#     'consumer_key': '664416747062739',
#     'consumer_secret': 'f05e9697e6a4816f78ff30cd8f434fe7'
# }
# app.config['SECURITY_POST_LOGIN'] = '/profile'

twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
timestamp = datetime.now().replace(minute = 0)



# configure Twitter API

# db = SQLAlchemy(app)

# # ... define user and role models ...

# class Connection(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     provider_id = db.Column(db.String(255))
#     provider_user_id = db.Column(db.String(255))
#     access_token = db.Column(db.String(255))
#     secret = db.Column(db.String(255))
#     display_name = db.Column(db.String(255))
#     profile_url = db.Column(db.String(512))
#     image_url = db.Column(db.String(512))
#     rank = db.Column(db.Integer)

# Security(app, SQLAlchemyUserDatastore(db, User, Role))
# Social(app, SQLAlchemyConnectionDatastore(db, Connection))



@app.route('/')
def main():
	counter = 0;
	lastFetchedTweetId = 791483941886697500
	itpTweets = twitter.statuses.user_timeline(screen_name='aviaryan123', since_id=lastFetchedTweetId)
	templateData = {
		 'itpTweets' : itpTweets
	}
	for _ in itpTweets:
		counter += 1
	return render_template('index3.html')
	# return str(counter)

# social = Social(app,db)
# @app.route('/profile')
# def profile():
#     return render_template(
#         'profile.html',
#         content='Profile Page',
#         facebook_conn=social.facebook.get_connection()
        # )	

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    pyDate = time.strptime(date,'%a %b %d %H:%M:%S +0000 %Y') # convert twitter date string into python date/time
    return time.strftime('%Y-%m-%d %H:%M:%S', pyDate) # return the formatted date.
    
# --------- Server On ----------
# start the webserver


if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 33507)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)