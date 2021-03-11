import sys
from configparser import ConfigParser
from importlib import resources 
sys.path.append('Unfollow_bot')
import twitter_unfollow as twb
import tweepy as tp


twitter = twb.unfollow_bot(API_KEY = '',
                           API_KEY_SECRET = '', 
                           ACCESS_TOKEN = '',
                           ACCESS_TOKEN_SECRET = '',
                           user = 'dussyb', days_without_activity = 1,
                           daily_tweet_freq = 1,
                           count = 0)

twitter.auth()

twitter.get_users()

if __name__ == "__main__":
    main() 
