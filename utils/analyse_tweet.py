import re

from app.domain.tweet import Tweet, TweetAnalyzed
from transformers import pipeline
pipe = pipeline("text-classification")   
 
# https://catriscode.com/2021/05/01/tweets-cleaning-with-python/
def clean_tweet(tweet):
    temp = tweet.lower()
    # temp = re.sub("'", "", temp) # to avoid removing contractions in english
    # Removing hashtags and mentions
    temp = re.sub("@[A-Za-z0-9_]+","", temp)
    temp = re.sub("#[A-Za-z0-9_]+","", temp)
    # Removing links
    temp = re.sub(r'http\S+', '', temp)
    # Removing punctuations
    # temp = re.sub('[()!?]', ' ', temp)
    # temp = re.sub('\[.*?\]',' ', temp)
    temp = re.sub("[^a-z0-9]"," ", temp)

    return temp



def analyze_tweet(tweet : Tweet) -> "TweetAnalyzed":
    

        
    text = tweet["text"]
    clean_text = clean_tweet(text)
    output = pipe(clean_text)[0]
    label = output.get("label")
    score = output.get('score')
    analyzed_tweet = TweetAnalyzed(text=text,score=score,label=label)
    
    print(f"{tweet} analyses")
        
    return analyzed_tweet
       