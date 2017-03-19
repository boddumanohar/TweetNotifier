![logo](http://i.imgur.com/r4Vr8sP.png) 

_Never miss a tweet_
# Overview
TweetNotifer is a service that counts the tweets posted by a particular twitter handles and returns the count of the tweets as a JSON file. This is a wrapper around twitter API and uses database to keep track of the latest tweets of a particular handle.

# Usage
This is very much identical to a service in microservices platform.

![services](http://i.imgur.com/utReGOR.png)

When we run the app, it serves on a port and needs a postgres database to save its data. The ideal way to use this is to run on a docker dontainer or deploy to heroku.

# Deployment

#### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/boddumanohar/TweetNotifier)]

#### Deploy to Docker container
TODO
 
