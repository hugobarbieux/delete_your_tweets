# Import modules

import sys
import time
from datetime import datetime
import os
import twitter
from dateutil.parser import parse
import numpy as np
import pandas as pd
import json

# API credentials

CONSUMER_KEY = "xxx"
CONSUMER_SECRET = "xxx"
ACCESS_TOKEN_KEY = "xxx"
ACCESS_TOKEN_SECRET = "xxx"


api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN_KEY,
                  access_token_secret = ACCESS_TOKEN_SECRET)


# Create a function to delete tweet by ID

def deleteTweet(tweetId):
   try:
     print("Deleting tweet #{0})".format(tweetId))
     api.DestroyStatus(tweetId)
     print("Deleted")

   except Exception as err:
      print("Exception: %s\n" % err)

myData = None
with open('tweet.json', encoding='utf-8') as json_file:
    myData = json.load(json_file)

print(myData)

# Range between you want your tweets deleted

range_start = datetime.strptime('Sep 10 00:00:00 +0000 2012','%b %d %H:%M:%S %z %Y')
range_end = datetime.strptime('Sep 10 00:00:00 +0000 2017','%b %d %H:%M:%S %z %Y')


# List of tweet IDs where tweetsToBeDeleted will be
# used for deleting tweet


tweetsToBeDeleted = []
tweetsToBeIgnored = []

for element in myData["data"]:
  tweet_post_time = datetime.strptime(element["tweet"]["created_at"],'%a %b %d %H:%M:%S %z %Y')
  if (tweet_post_time>= range_start and tweet_post_time<= range_end ):
    tweetsToBeDeleted.append(element["tweet"]["id_str"])
  else:
    tweetsToBeIgnored.append(element["tweet"]["id_str"])

print(len(tweetsToBeDeleted),len(tweetsToBeIgnored))

for id in tweetsToBeDeleted:
  deleteTweet(id)