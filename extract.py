import tweepy
import re

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

authenticator = IAMAuthenticator('I9SoDxAjklZO8nrfxXqNXY9eBZUGSSMcj_jj18MKxEgB')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/bffc46a2-d5fc-4471-bb72-b933927cfc56')


consumer_key = "5UeKiFHa96pyazNPPIMtJFJWa"
consumer_secret = "qolQVy1UDVO5JkIyZQcQy7vYCfF6wL8EaLJVGuz3F4XO6qTqIK" 
access_key = "3500004257-ltKjPHUHFWpOWmm017ceti3Jr0KSOtfVQjCJmYu"
access_secret = "CY5yPMpAGJ176yS7ILo7Wtz90pgoCjgO0RjxTwcmFCS6B"

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)   
auth.set_access_token(access_key, access_secret) 
  
# Creating an API object 
api = tweepy.API(auth)

username_tweets = tweepy.Cursor(api.search_tweets, 
                                q="ukraine crime -filter:retweets since:2022-07-14", 
                                lang="en", 
                                tweet_mode='extended').items(1)

# for tweet in username_tweets:
#     text = tweet._json["full_text"]
#     print(text)

text = open("tweets/ukraine/crime/20220714.txt", "w")

for tweet in username_tweets:
    tweet = tweet._json["full_text"]
    tweet = re.sub('@[^\s]+','',tweet)
    tweet = re.sub('https[^\s]+','',tweet)

    try:
        response = natural_language_understanding.analyze(
            text=tweet,
            features=Features(sentiment=SentimentOptions(targets=['crime']))).get_result()

        print(tweet)
        print("\n")
        res = response['sentiment']['targets']
        for x in res:
            r = str(x['score']) + '\n'
        text.write(r)
        print(response)
    except Exception:
        pass

text.close()