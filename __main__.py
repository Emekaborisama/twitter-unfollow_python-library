import sys
from configparser import ConfigParser
from importlib import resources 
sys.path.append('Unfollow_bot')
import twitter_unfollow as twb
import tweepy as tp


twitter = twb.unfollow_bot(API_KEY = 'B7gGiopOKwArSZtWrFYlwaAZA',
                           API_KEY_SECRET = 'qaC3YjInoeMmLSsRJSTY251Cq500k2qvfw84EMY5F3LdNzhXhk', 
                           ACCESS_TOKEN = '1165331774190292993-FeZtCJXspmbBxUvsvtlVhHNo3p7XCb',
                           ACCESS_TOKEN_SECRET = 'gna5BkzqoapIEf6M8EJV980ga1AgrlDXEapokq9Qn49gh',
                           user = 'dussyb', days_without_activity = 1,
                           daily_tweet_freq = 1,
                           count = 0)

twitter.auth()

twitter.get_users()

if __name__ == "__main__":
    main() 