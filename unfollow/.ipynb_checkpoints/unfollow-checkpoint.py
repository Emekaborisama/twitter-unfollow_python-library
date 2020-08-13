

import os
import tweepy as tp
import pandas as pd
from datetime import datetime, timedelta



class unfollow_bot():
    def __init__(self, API_KEY, API_KEY_SECRET,  ACCESS_TOKEN,ACCESS_TOKEN_SECRET, user, days_without_activity,
                 daily_tweet_freq, count):
        self.user = user
        self.days_without_activity = days_without_activity
        self.daily_tweet_freq = daily_tweet_freq
        self.count =0
        self.API_KEY = API_KEY
        self.API_KEY_SECRET = API_KEY_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
            #self.threshold = threshold
            
    def auth(self):
        auth = tp.OAuthHandler(self.API_KEY, self.API_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tp.API(auth,  wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
        #return api
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
            return api
    
              
    #self.threshold = datetime.now() - timedelta(days=self.days_without_activity)
    #self.data = []
    def get_users(self):
        self.threshold = datetime.now() - timedelta(days=self.days_without_activity)
        self.data = []
        for user in api.friends_ids(self.user):
            status = api.user_timeline(self.user, self.count)
            span = ((status[0].created_at - status[-1].created_at).days)
            frequency = (len(status) / span) if span > 0 else None
            if status[0].created_at < threshold or (frequency is not None and frequency < self.days_without_activity ):
                print(f"Unfollowing @{status[0].user.screen_name} ({status[0].user.name}). Last status update on {status[0].created_at}. Frequency: {frequency:.2f}")
                api.destroy_friendship(self.user)
                self.count += 1
                print(f"You just unfollowed {self.count} accounts. @{self.user} is now following {len(api.friends_ids(self.user))}.")
                
if __name__ == "__main__":
      main()
    
    