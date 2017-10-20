import tweepy
from auth import get_api

api = get_api()

def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)
    
def get_by_search(query, count):
    return tweepy.Cursor(api.search, q=query).items(count)

for status in get_by_search("Storm Brian", 10):
    print(status)
for status in get_my_timeline(1):
    print(status)
    