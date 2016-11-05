import os
import time
from twitter import *
from flask import Flask, request, render_template, redirect, abort, flash, jsonify
from datetime import datetime



app = Flask(__name__)   # create our flask app

# configure Twitter API

CONSUMER_KEY='WOWfe9QRArl5beDczAMfRP4jU'
CONSUMER_SECRET='XBYI52DvlWNBzqMqpfzk98gxQLwFqUKeNpgJp1qTvIbfMv9hIH'
OAUTH_TOKEN='560955859-MCmIMQ6k5UgVvAxA6fXj7MKBisWmTuUibzpGRI9m'
OAUTH_SECRET='kJkNlPDjZZHWxLsQ6gBSu2tIEj8oEqegLqL9jqI3PTPBX'


twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
timestamp = datetime.now().replace(minute = 0)


# setting up routes 

@app.route('/')
def main():
	counter = 0;
	myvar = 0
	lastFetchedTweetId = 791483941886697500
	handle_name = 'aviaryan123'
	itpTweets = twitter.statuses.user_timeline(screen_name=handle_name, since_id=lastFetchedTweetId)
	r = {}
	for t in itpTweets:
		if(counter==0):
			myvar  = t['id']
			counter += 1
		else:	
			counter += 1
	return  jsonify({'tweets': counter })
	# return "The number of tweets postedby "+ handle_name + " is "+ str(counter)+ " " + t.id


@app.route('/login/', methods=['GET','POST'])
def login():
	return render_template('login.html')	
    
# --------- Server On ----------
# start the webserver

if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)