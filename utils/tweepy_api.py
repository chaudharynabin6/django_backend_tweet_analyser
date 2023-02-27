import os
import sys
import requests
import tweepy

from dotenv import load_dotenv

dotenv_path = os.getcwd()
#ERROR: 
# https://docs.python.org/3/library/sys.html#sys.platform
# checking the os
if 'win' in sys.platform:
    dotenv_path = os.path.join(dotenv_path,".env")
else:
    dotenv_path = os.path.join(dotenv_path,".env")

print(dotenv_path)
load_dotenv(dotenv_path=dotenv_path)
bearer_token = os.getenv("bearer_token")
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


raw_headers="""Accept: */*
User-Agent: Thunder Client (https://www.thunderclient.com)
Accept: */*
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAMWiVgEAAAAAS3oPA4Am9dY39s3b0L%2Fhke5im4I%3DeocuZgNNtGQz2R2oQstPfRWoPB27lDIreMaswLZhn69p7feng1"""

def get_headers_as_dict(headers: str):
    dic = {}
    for line in headers.split("\n"):
        if line.startswith(("GET", "POST")):
            continue
        point_index = line.find(":")
        dic[line[:point_index].strip()] = line[point_index+1:].strip()
    return dic
headers = get_headers_as_dict(headers=raw_headers)


payload = {}
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/quick-start/recent-search
def search_tweet(token):
    url = "https://api.twitter.com/2/tweets/search/recent?query="+token
    response = requests.request("GET",url=url,headers=headers)
    data = response.json()
    return data
