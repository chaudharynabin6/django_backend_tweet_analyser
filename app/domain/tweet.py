from other import constants as constant

class Tweet(dict):
    
    def __init__(self,text : str):
        dict.__init__(self,text = text)

        
  

 

class TweetAnalyzed(dict):
    def __init__(self,text : str,score : float, label : str ):
        if(score < 0 or score > 1):
            raise ValueError(f"score cannot be greater that 1 and less than 0 but found >> {score} <<")
        
        
        # if(label not in [constant.POSITIVE,constant.NEGATIVE]):
        #     raise ValueError(f"label should be either positive or negative but found >> {label} <<")
        dict.__init__(self,text = text,score = score,label = label)
        
        

def main():
    tweet = Tweet(text="hello")
    assert(tweet.text == "hello")
    
    tweetAnalyzed = TweetAnalyzed(text = tweet.text,score = 0.5,label=constant.NEGATIVE)
    print(tweetAnalyzed)
    
if __name__ == "__main__":
    main()
    