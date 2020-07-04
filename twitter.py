import tweepy
import os
import dotenv as dv

def setup_Bot():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    dv.load_dotenv(dotenv_path)

    consumerKey = os.environ.get("API_KEY")
    consumerSecret = os.environ.get("API_KEY_SECRET")
    accessToken = os.environ.get("ACCESS_TOKEN")
    accessTokenSecret = os.environ.get("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)

    return api

def get_Tweet():
    pass