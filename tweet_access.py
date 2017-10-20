import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'T2TyJqqZBuOQ4JXRfvj2W1Tbf'
CONSUMER_SECRET = 'mXtqw02cAgb2sNLy82lCpGQoRC3FSGoBQF1QQtvuoJex4pvKsc'
OAUTH_TOKEN = '921002279045615617-Kzo9wrRLB2NoU2YzT4On8Glbhu6UMlH'
OAUTH_TOKEN_SECRET = '3w58ur3pdPTPfb2RNL4DW1GcDZY4icXZ2ZIe9CoOSJYl2'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)

api = get_api()


count = 10
query = "Dublin"

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print(result)