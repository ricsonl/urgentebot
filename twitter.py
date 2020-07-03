import requests
import tweepy
import time
import json

def setup_Bot():
    consumerKey = "YOUR_API_KEY"
    consumerSecret = "YOUR_API_KEY_SECRET"
    accessToken = "YOUR_ACCESS_TOKEN"
    accessTokenSecret = "YOUR_ACCESS_TOKEN_SECRET"
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    return api

def get_Tweet():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]