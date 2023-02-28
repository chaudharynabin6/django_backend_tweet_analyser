

from django.urls import path

from app.views import search_tweets,analyze_single_text,search_tweets_with_next_token


urlpatterns = [
    path(r'tweets/<str:keyword>/<str:next_token>',view = search_tweets_with_next_token),
    path(r'tweets/<str:keyword>',view = search_tweets),
    path(r'text/<str:text>',view = analyze_single_text),
    
]