import re
import nltk
import tweepy
from tweepy import OAuthHandler
import json 


consumer_key = "Sw6UssA8g6SujUmCOIpRm0qIv"
consumer_secret = "xzymkyUtCgmAUEn7gRQvH3jTUaEcz1FALm3GxirMxhOU8Xhd4u"
access_token = "1938591426-hcmVqndxjLRJFGD1G87nqcV4gQ1QuNjUy9ry2es"
access_token_secret = "YvAmszNXQvwor4zTqb9EcwkM0x97Lm5aSLyiuOyUc5T9G"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

link_regex = re.compile("(https?:\/\/[^\s]+)|(@[^\s]+)")

def process_json(tweet):
    return {"text":tweet['text'], "source": tweet['user']['name']}


def get_tweets():
    headlines = []
    for status in tweepy.Cursor(api.home_timeline).items(15):
    # Process a single status
        tweet = process_json(status._json)
        headlines.append(re.sub(link_regex, "", tweet['text']))
    return headlines



# all_tweets = get_tweets()
# print(all_tweets)