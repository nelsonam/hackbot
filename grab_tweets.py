import os
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

limit = 100

from TwitterSearch import *

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['#hackathon']) # what we want to search for
    tso.set_language('en')

    # create a Twitter Search Object with API keys
    ts = TwitterSearch(
        consumer_key = os.environ['consumer_key'],
        consumer_secret = os.environ['consumer_secret'],
        access_token = os.environ['access_token'],
        access_token_secret = os.environ['access_secret']
     )

    # this is where the fun actually starts :)
    tweets = 0 # how many tweets we've looked at so far
    with open('hacktweets.txt','w') as f:
        for tweet in ts.search_tweets_iterable(tso):
            if tweets < limit:
                tweet_text = tweet['text']
                tweet_text.replace('\r\n',' ')
                f.write( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet_text ) )
                f.write("\n")
                tweets += 1

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

