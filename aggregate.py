import datetime
import func
import const
import tweepy
import time
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

# IBM Natural Language Understanding API Initialisation
authenticator = IAMAuthenticator(const.nlu_api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator)
natural_language_understanding.set_service_url(const.nlu_url)

# Twitter API Initialisation
client = tweepy.Client(const.bearer_token)


indexes = ['crime', 'gdp', 'employment', 'corruption', 'inequality', 'law', 'right', 'security', 'conflict', 'health']
countries = ['uk', 'france', 'germany', 'us', 'afghanistan']
# countries = ['afghanistan']

d = datetime.date(2021, 3, 15) # change date here
# next_monday = func.get_next_monday(d)
dates, next_dates = func.get_dates(d)

parent = 'tweets/'
func.create_country_dir(parent, countries, '20210315') # change date here

for country in countries:
    home = parent + country + '20210315/' # change date here
    func.create_idx_dir(home, indexes)
    for idx in indexes:
        for i in range(10):
            f_date = dates[i] + 'T00:00:00.00Z'
            f_next_date = next_dates[i] + 'T00:00:00.00Z'
            tweets = func.get_tweets(country, idx, f_date, f_next_date)
            if not tweets:
                print('There is not tweets about ' + idx + ' on ' + dates[i])
                continue
            address = home + idx + '/' + dates[i] + '.txt'
            file = open(address, "w")
            try:
                for tweet in tweets.data:
                    tweet = str(tweet)
                    r = func.nlu(tweet, idx, natural_language_understanding)
                    if not r:
                        continue
                    file.write(r)
            except TypeError:
                time.sleep(15)
                file.write('0')
            file.close()


