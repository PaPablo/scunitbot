# Import credetials
from credentials import *
from phrases import get_phrase
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

phrase = get_phrase()

text = "\"{0}\"\n\n{1}".format(phrase['phrase'],phrase['name'])

api.update_status(text)





