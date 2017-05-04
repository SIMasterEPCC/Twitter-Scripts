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


twitter = Twitter(auth=oauth)

#world_trends = twitter.trends.available(_woeid=1)
spain_trends = twitter.trends.place(_id = 23424950)

print json.dumps(spain_trends, indent=4)

#for trend in world_trends:   
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    #print
    #print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
   # print json.dumps(trend, indent=4)