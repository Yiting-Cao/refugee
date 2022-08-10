# string = [{'text': 'crime', 'score': -0.961487, 'label': 'negative'}]
# print(type(string))
# for s in string:
#     print(s['score'])


import json
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

response = natural_language_understanding.analyze(
        text='illegals flooding the country, all the baby formula goes to Mexico/Ukraine, billions to Ukraine while food prices here unchecked, Bidens beholden to China, 1/6 sham trial, election fraud, indoctrination/grooming 4 year olds, socialist big govt, crime, division, hate, lies',
        features=Features(sentiment=SentimentOptions(targets=['crime']))).get_result()

res = response['sentiment']['targets']
for x in res:
        r = str(x['score']) + '\n'
print(res)
print(r)