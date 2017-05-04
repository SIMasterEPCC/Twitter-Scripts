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

followers = twitter.followers.ids(screen_name="cristobalgc2411")
#timeline = twitter.statuses.user_timeline(screen_name="cristobalgc2411", result_type='recent', count=1)

#print json.dumps(followers, indent=4)
for id_follower in followers["ids"]:
  subquery = twitter.users.lookup(user_id = id_follower)

  for user in subquery:
    #-----------------------------------------------------------------------
    # now print out user info, starring any users that are Verified.
    #-----------------------------------------------------------------------
    print "%s - %s" % (user["screen_name"], user["location"])
#print json.dumps(timeline, indent=4)