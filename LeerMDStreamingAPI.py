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

twitter_userstream = TwitterStream(auth=oauth, domain='userstream.twitter.com')
for msg in twitter_userstream.user():
  if 'direct_message' in msg:
    print
    print json.dumps(msg)