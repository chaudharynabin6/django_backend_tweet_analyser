
import json
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from app.domain.tweet import Tweet
from utils.analyse_tweet import analyze_tweet


from utils.tweepy_api import search_tweet

# Create your views here.

@api_view(['GET'])
def search_tweets(request,token=""):
    if token == "":
        raise  NotFound(detail="Please enter text")
    

    root_data = search_tweet(token=token)

    
    tweet_list = []
    for tweet in root_data.data :
         t  = Tweet(text = tweet["text"])
         tweet_list.append(t)
        
    analyzed_tweets = []
    for tweet in tweet_list:
        analyzed_tweet = analyze_tweet(tweet)
        analyzed_tweets.append(analyzed_tweet)
        
    json_data = json.dumps(analyzed_tweets,indent=2)
    return Response(data = json_data)
    
 
    