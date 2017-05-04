# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'Your acces token'
ACCESS_SECRET = 'Your acces secret'
CONSUMER_KEY = 'Your consumer key'
CONSUMER_SECRET = 'Your consumer secret'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

twitter.statuses.update(status="Probando API de Twitter")
