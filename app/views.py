import json
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework import status


from utils.tweepy_api import search_tweet

# Create your views here.

@api_view(['GET'])
def search_tweets(request,token=""):
    if token == "":
        raise  NotFound(detail="Please enter text")
    

    tweet_list = search_tweet(token=token)
    
    
    return Response(tweet_list)
    
    