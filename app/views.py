
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
def search_tweets_with_next_token(request,keyword="",next_token=""):
    if keyword == "":
        raise  NotFound(detail="Please enter text")
    
    if next_token == "":
        
        root_data = search_tweet(keyword=keyword)

    else :
        root_data = search_tweet(keyword=keyword,next_token=next_token)

    
    tweet_list = []
    for tweet in root_data.data :
         t  = Tweet(text = tweet["text"])
         tweet_list.append(t)
        
    analyzed_tweets = []
    for tweet in tweet_list:
        analyzed_tweet = analyze_tweet(tweet)
        analyzed_tweets.append(analyzed_tweet)
        
    # json_data = json.dumps(analyzed_tweets,indent=2)
    return Response(data = {"tweets" : analyzed_tweets,"next_token" : root_data.meta["next_token"]})
    
    
@api_view(['GET'])
def search_tweets(request,keyword=""):
    if keyword == "":
        raise  NotFound(detail="Please enter text")
    
   
    root_data = search_tweet(keyword=keyword)

   

    
    tweet_list = []
    for tweet in root_data.data :
         t  = Tweet(text = tweet["text"])
         tweet_list.append(t)
        
    analyzed_tweets = []
    for tweet in tweet_list:
        analyzed_tweet = analyze_tweet(tweet)
        analyzed_tweets.append(analyzed_tweet)
        
    # json_data = json.dumps(analyzed_tweets,indent=2)
    return Response(data = {"tweets" : analyzed_tweets,"next_token" : root_data.meta["next_token"]})
    
@api_view(["GET"])
def analyze_single_text(request,text=""):
    if text == "":
        raise NotFound(detail="Please enter text")
    
    analyzed_text = analyze_tweet(Tweet(text=text))
    
    return Response(data=analyzed_text)
 
    