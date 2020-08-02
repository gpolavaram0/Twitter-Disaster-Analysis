# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import tweepy
import time
import os


# %%
# consumer_key = "yhrpkTLNagNZI6ospVftHJ9Yh"
consumer_key = os.environ["consumer_key"]
consumer_secret = "f93J3NZBoZ7m3nMgy3FH3LlLPzNbxN6Td1EyaidJi6OtGEvnjV"
access_token = "1260032178907279362-aMgACaF9WHWggwpfMn6EeJTGryKOuM"
access_token_secret = "gwmoo59rWFzdRxfBr0hXYi0vIceqvw7JLxUTWedVu1w7h"


# %%
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# %%
tweets = []
username = 'AP'
count = 50
try: 
# Pulling individual tweets from query
    for tweet in api.user_timeline(id=username, count=count, tweet_mode="extended"):
# Adding to list that contains all tweets
        tweets.append((tweet.created_at,tweet.id,tweet.full_text))
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)


# %%
print(tweets)


# %%
for i in range(len(tweets)):
    print(tweets[i])


# %%
AP_tweetListOf6 = []
AP_numListOf6 = []
for i in range(6):
    print(tweets[i][2])
    AP_tweetListOf6.append(tweets[i][2])
    AP_numListOf6.append(tweets[i][1])


# %%
AP_tweetListOf6


# %%
AP_numListOf6


# %%



