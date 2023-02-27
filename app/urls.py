

from django.urls import path

from app.views import search_tweets


urlpatterns = [
    path(r'<str:token>',view = search_tweets),
]