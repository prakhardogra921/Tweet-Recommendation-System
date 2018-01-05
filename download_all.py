import tweepy
from twython import Twython
import json
import pprint
#from tweepy.parsers import JSONParser

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"
access_key = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

twitter = Twython(consumer_key, consumer_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(consumer_key, access_token=ACCESS_TOKEN)

def get_all_hash(name):

    api = tweepy.API(auth)
    #api = tweepy.API(auth,parser=JSONParser())
    new_tweets = api.search(q=name, count=50)
    return new_tweets

def get_all_tweets(username):

    alltweets = []
    user_timeline = twitter.get_user_timeline(screen_name=username,count=50,include_rts=1)
    alltweets.extend(user_timeline)
    return alltweets

def download_both(username):
    print(username)
    tweets = []
    if username[0] == "@":
        tweets = get_all_tweets(username)
        print ("\nUser timeline tweets downloaded.")
    if username[0] == "#":
        tweets = get_all_hash(username)
        print ("\nAll hashtag tweets downloaded.")
    return tweets

#pprint.pprint(download_both("#changetheratio"))
