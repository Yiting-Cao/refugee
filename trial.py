import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

test = "USA TODAY NEWS USA Criminal Manipulations!Turn things around for your sole benifit though it may be a Crime!First you were out of Nato.Then you prevented delivery of Arms to Ukraine likely to help Putin planning his invasion.Then you had Armed Extremist Groups attack the Capital. "


authenticator = IAMAuthenticator('I9SoDxAjklZO8nrfxXqNXY9eBZUGSSMcj_jj18MKxEgB')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/bffc46a2-d5fc-4471-bb72-b933927cfc56')

response = natural_language_understanding.analyze(
    text=test,
    features=Features(sentiment=SentimentOptions(targets=['crime']))).get_result()

# print(json.dumps(response, indent=2))


res = response['sentiment']['targets']
res = str(res)
print(type(res))
print(res)