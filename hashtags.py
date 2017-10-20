import json

results=[]

tweets_file = open("tweet_mining.json", "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
    
new_ht = []

for tweet in results:
    hashtags = tweet["entities"]["hashtags"]
    for ht in hashtags:
        if ht["text"] not in new_ht:
            new_ht.append(ht["text"])
        
print(new_ht)