import tweepy

api_key=""
api_secret=""
access_token=""
access_token_secret=""

api=tweepy.Client(consumer_key=api_key,consumer_secret=api_secret,access_token=access_token,access_token_secret=access_token_secret)
tweet_num = 0

while 1:
    tweet_num+=1
    tweet = "#bellletstalk \n${:.2f} raised".format(tweet_num*0.05)
    try:
        api.create_tweet(user_auth=True,text=tweet)
    except Exception as e:
        print(e)
        tweet_num -= 1
    

