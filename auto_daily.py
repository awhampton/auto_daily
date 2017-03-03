import twitter
import random
import requests
import derp_requests
from config import c_key, c_secret, at_key, at_secret

# connect to twitter with application credentials
api = twitter.Api(consumer_key = c_key, consumer_secret = c_secret, access_token_key = at_key, access_token_secret = at_secret)

# see what's going on with kanye
kanye = [s.text for s in api.GetUserTimeline(screen_name = 'kanyewest', count = 200)]

# get a random tweet
tweet = random.choice(kanye)

# open a session
with requests.Session() as session:
    derp_requests.github_login(session)
    derp_requests.derp_login(session)
    derp_requests.derp_daily(session, tweet)
