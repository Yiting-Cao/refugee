import datetime
import const
import tweepy
import func
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

# Twitter API Initialisation
# client = tweepy.Client(const.bearer_token)
# auth = tweepy.OAuth2AppHandler(const.client_id, const.client_secret)
# auth = tweepy.OAuth2BearerHandler(const.bearer_token)   
# auth.set_access_token(const.access_key, const.access_secret)
# api = tweepy.API(auth)

authenticator = IAMAuthenticator(const.nlu_api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator)
natural_language_understanding.set_service_url(const.nlu_url)

client = tweepy.Client(const.bearer_token)
tweets = client.search_all_tweets(query="ukraine crime lang:en -is:retweet", start_time='2022-07-19T00:00:00.00Z', end_time='2022-07-20T07:20:50.52Z', max_results=10)

# tweets = tweepy.Cursor(api.search_tweets, q="@elonmusk until:2022-08-21", lang="en", tweet_mode='extended').items(5)
# print(type(tweets))

for tweet in tweets.data:
    tweet = str(tweet)
    print(str(tweet))
    response = natural_language_understanding.analyze(
            text=tweet,
            features=Features(sentiment=SentimentOptions(targets=['crime']))).get_result()
    print(json.dumps(response, indent=2))
    res = response['sentiment']['targets']
    for x in res:
        r = str(x['score']) + '\n'

    print(r)
    print('\n')

