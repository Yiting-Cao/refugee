import datetime
import const
import os
import tweepy
import re
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

def get_next_monday(d):
    import datetime
    days_ahead = 0 - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def get_dates(d):
    import datetime
    dates = []
    next_dates = []
    tz = 'T00:00:00.00Z'
    dates.append(d.strftime('%Y-%m-%d'))
    next_d = d + datetime.timedelta(days=3)
    next_dates.append(next_d.strftime('%Y-%m-%d'))
    for _ in range(9):
        new_d = d + datetime.timedelta(weeks=1)
        next_new_d = new_d + datetime.timedelta(days=3)
        dates.append(new_d.strftime('%Y-%m-%d'))
        next_dates.append(next_new_d.strftime('%Y-%m-%d'))
        d = new_d
    for date in dates:
        date = date + tz
    for next_date in next_dates:
        next_date = next_date + tz
    return dates, next_dates

# d = datetime.date(2022, 5, 5)
# dates, next_dates = get_dates(d)
# print(dates)
# print(next_dates)

def get_next_day(d):
    import datetime
    new_d = d + datetime.timedelta(days=1)
    return new_d

# d = datetime.date.today()
# next_monday = get_next_monday(d) 
# print(next_monday)
# dates, next_dates = get_dates(next_monday)
# print(dates)
# print(next_dates)


def create_idx_dir(parent_dir, indexes):
    for idx in indexes:
        path = parent_dir + idx
        os.mkdir(path)

def create_country_dir(parent_dir, countries, date):
    for country in countries:
        path = parent_dir + country + date
        os.mkdir(path)

def get_tweets(country, idx, date, next_date):
    q = country + ' ' + idx + ' -is:retweet'
    client = tweepy.Client(const.bearer_token)
    tweets = client.search_all_tweets(query=q, 
                                      start_time=date, 
                                      end_time=next_date, max_results=10)
    return tweets


def clean_up(tweet):
    tweet = tweet._json["full_text"]
    tweet = re.sub('@[^\s]+','',tweet)
    tweet = re.sub('https[^\s]+','',tweet)
    return tweet


def nlu(tweet, idx, natural_language_understanding):
    try:
        response = natural_language_understanding.analyze(
            text=tweet,
            features=Features(sentiment=SentimentOptions(targets=[idx]))).get_result()
        # print(tweet)
        # print("\n")
        res = response['sentiment']['targets']
        for x in res:
            r = str(x['score']) + '\n'
        # print(response)
        # text.write(r)
        return r
    except Exception:
        pass


def turn_file_into_list(in_file):
    import random
    l = []
    with open(in_file, 'r') as infile:
        contents = [line for line in infile.readlines()]
        for content in contents:
            new_content = content.strip()
            new_content = float(new_content)
            l.append(new_content)
        infile.close()
    l = [x for x in l if x !=0]
    ll = len(l)
    if ll == 0:
        l = [0.0 for x in range(10)]
    elif ll < 10:
        s = sum(l)
        for _ in range(10-ll):
            n = round(s/ll + random.uniform(-0.1, 0.1), 6)
            while n <= -1 or n >= 1:
                n = round(s/ll + random.uniform(-0.1, 0.1), 6)
            l.append(n)
    return l

def turn_file_into_number(in_file):
    import random
    l = []
    with open(in_file, 'r') as infile:
        contents = [line for line in infile.readlines()]
        for content in contents:
            new_content = content.strip()
            new_content = float(new_content)
            l.append(new_content)
        infile.close()
    l = [x for x in l if x !=0]
    ll = len(l)
    if ll == 0:
        n = 0.0
    else:
        n = round(sum(l)/ll, 6)
    return n

# res = turn_file_into_list('tweets/ukraine/crime/2022-05-02.txt')
# print(res)