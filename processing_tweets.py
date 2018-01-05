__author__ = 'prakhardogra'

from pymongo import MongoClient
import os.path
import json
import pprint
from download_all import download_both

alltweets = []

folder_path = "/home/prakhardogra/PycharmProjects/project4/"

filename = os.path.join(folder_path, 'all_tweets.json')

def get_tweets():

    client = MongoClient()

    db = client.test3

    c = db.tweets1

    tweets = c.find({},{"text":1,"_id":0})

    list = []
    hashlist = []

    for tweet in tweets:
        for word in tweet["text"].split(" "):
            if "@" in word:                     #check for user mention
                if "." in word:
                    word = word.replace('.','')
                if ":" in word:
                    word = word.replace(':','')
                if "," in word:
                    word = word.replace(',','')
                if "'s" in word:
                    word = word.replace("'s",'')
                if "?" in word:
                    word = word.replace('?','')
                if ")" in word:
                    word = word.replace(')','')
                if word.lower() not in list:
                    if "w/" not in word:
                        list.append(word.lower())
            if "#" in word:                     #check for hashtag
                if "." in word:
                    word = word.replace('.','')
                if ":" in word:
                    word = word.replace(':','')
                if "," in word:
                    word = word.replace(',','')
                if "'s" in word:
                    word = word.replace("'s",'')
                if "?" in word:
                    word = word.replace('?','')
                if ")" in word:
                    word = word.replace(')','')
                if word.lower() not in list:
                    if "w/" not in word:
                        list.append(word.lower())
                        hashlist.append(word.lower())

    print (list)

    with open(filename, 'w') as f:
        for word in list:
            if "@" in word:
                tweets = download_both(word)
                for tweet in tweets:
                    if tweet['user']['listed_count'] == 0:
                        tweet['user']['listed_count'] = 1
                    alltweets.append({"text":tweet['text'],"ratio":tweet['user']['followers_count']/tweet['user']['listed_count'],"fac":tweet['favorite_count'],"rc":tweet['retweet_count'],"hashtags":tweet['entities']['hashtags']})
            if "#" in word:

                tweets = download_both(word)
                for tweet in tweets:
                    if tweet.user.listed_count == 0:
                        tweet.user.listed_count = 1
                    alltweets.append({"text":tweet.text,"fac":tweet.favorite_count,"ratio":(tweet.user.followers_count)/(tweet.user.listed_count),"rc":tweet.retweet_count,"hashtags":hashlist})
        json.dump(alltweets, f)

    return list
