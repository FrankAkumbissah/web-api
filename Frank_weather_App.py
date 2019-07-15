import tweepy
import time
import pyowm

def post_cloudy_tweet (location):
    owm = pyowm.OWM()
    loc = owm.three_hours_forecast(location)
    
    #Authenticate connection
    auth = tweepy.OAuthHandler(9l3VUKPeA7Cs4n76JPsYqeIVK, HeIHyVl0MeM3CwpLYTxahQNlHi1gLRjO0cf7e3hjTVqYMkE7a8)
    auth.set_access_token(375313048-M5yaE715TxQe2IakCJIXPQBytSZ93sVBGj3OzulK, CTjbupCpTJllnHgGQHOmxg9O1xjdea0idjvFvcaMbPjyO)
    
    #Start API
    api = tweepy.API(auth)
    
    #Post twweet
    if(loc.will_have_clouds()):
        api.update_status("It will be cloudy in " + location)
    else:
        api.update_status("It will not be cloudy in " + location)
        

def post_tweet_hourly():
    while True:
        post_cloudy_tweet("Cape Coast")
        time.sleep(3600)
    
post_tweet_hourly()