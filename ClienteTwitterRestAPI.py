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
            
# Search for latest tweets about
#iterator = twitter.search.tweets(q= "#Messi")
iterator = twitter.search.tweets(q='Messi', result_type='recent', lang='fr', count=10)

tweet_count = 100
#for tweet in iterator:
for tweet in iterator["statuses"]:
    print "(%s) | @%s | %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"])    
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print
    #print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    #print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 