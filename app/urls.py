

from django.urls import path

from app.views import search_tweets,analyze_single_text


urlpatterns = [
    path(r'tweets/<str:token>',view = search_tweets),
    path(r'text/<str:text>',view = analyze_single_text),
    
]