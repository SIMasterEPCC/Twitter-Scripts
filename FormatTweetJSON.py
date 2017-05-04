# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = 'streamingAPIResultsEnglish.txt'
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
	    print
	    print
            print "Id tweet: " + str(tweet['id']) # This is the tweet's id
            print "Fecha creacion: " + tweet['created_at'] # when the tweet posted
            print "Contenido del tweet: " + tweet['text'] # content of the tweet
                        
            print "Id usuari@: " + str(tweet['user']['id']) # id of the user who posted the tweet
            print "Nombre de usuario: " + tweet['user']['name'] # name of the user, e.g. "Wei Xu"
            print "Nickname: @" + tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
            	hashtags.append(hashtag['text'])
            print "Hastags incluidos: " + str(hashtags)

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue