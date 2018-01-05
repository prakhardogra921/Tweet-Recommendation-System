__author__ = 'prakhardogra'

import tweepy
from twython import Twython
import time
import json
import os.path
import subprocess

from processing_tweets import get_tweets

from ranking_script import tweet_recom

folder_path = "/home/prakhardogra/PycharmProjects/project4/"

username = "@hmason"

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"
access_key = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

alltweets = []
tweets = []
count = 50

twitter = Twython(consumer_key, consumer_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(consumer_key, access_token=ACCESS_TOKEN)

def user_tweets(username):

    alltweets = []
    user_timeline = twitter.get_user_timeline(screen_name=username,count=50,include_rts=1)
    alltweets.extend(user_timeline)

    print ("Tweets downloaded")
    tweets = []
    filename = os.path.join(folder_path, 'mainuser_tweets.json')

    with open(filename, 'w') as f:

        for tweet in alltweets:
            tweets.append(tweet)

        json.dump(tweets, f)
    print ("JSON file created")

print ("Downloading of ",username.replace("@",""), " tweets started.")

user_tweets(username)

time.sleep(3)

subprocess.call(["mongoimport","-d","test3","-c","tweets1","--jsonArray","--file","mainuser_tweets.json"])

print ("Mongoimport command has run successfully.")

time.sleep(3)

list = get_tweets()

print ("All tweets saved in JSON file.")

time.sleep(3)

subprocess.call(["mongoimport","-d","test3","-c","tweets2","--jsonArray","--file","all_tweets.json"])

print ("Mongoimport command has run successfully.")

time.sleep(3)

tweet_recom(list)
