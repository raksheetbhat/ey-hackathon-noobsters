from summarizer import Summarizer
import json
import copy

#
#
# def get_summary(path):
#
#     with open(path,'r') as file:
#         raw_text = file.read()
#         processed = json.loads(raw_text)
#
#     model = Summarizer()
#
#     for news in processed:
#
#         result = model(news["text"], min_length=20, max_length=200)
#         summary = "".join(result)
#         print(news["link"])
#         print(summary)
#         print("\n")
#
#
# get_summary('/opt/airflow/data/1/source/news.json')
#
#
#
#
# import spacy
# from collections import Counter
# from string import punctuation
#
# nlp = spacy.load("en_core_web_md")
#
#
# def get_keywords(path):
#
#     with open(path,'r') as file:
#         raw_text = file.read()
#         processed = json.loads(raw_text)
#
#     text = ""
#
#     for news in processed:
#         text += " " + news["text"]
#
#     keywords = get_hotwords(text)
#     for x in Counter(keywords).most_common(20):
#         print(x[0] + str(x[1]))
#
#     print("\n")
#
#     # for news in processed:
#     #     print(news["link"])
#     #     keywords = get_hotwords(news["text"])
#     #     for x in Counter(keywords).most_common(10):
#     #         print(x)
#     #
#     #     print("\n")
#
#
# def get_hotwords(text):
#     result = []
#     pos_tag = ['PROPN', 'ADJ', 'NOUN']  # 1
#     doc = nlp(text.lower())  # 2
#     for token in doc:
#         # 3
#         if token.text in nlp.Defaults.stop_words or token.text in punctuation:
#             continue
#         # 4
#         if token.pos_ in pos_tag:
#             result.append(token.text)
#
#     return result  # 5


from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


def get_sentiment(text):

    sia = SIA()

    pol_score = sia.polarity_scores(text)

    # print(text)
    # print(pol_score)
    # print("\n")

    if pol_score["compound"] > 0.4:
        return 1

    elif pol_score["compound"] < 0.2:
        return -1

    return 1


TWEET_SCHEMA = {
    "link": "",
    "text": "",
    "sentiment": "",
    "keywords": [],
    "retweet_count": "",
    "favorited": ""
}


def analyze_tweets(tweets, insights):

    sentiments = []
    keywords = []

    for tweet in tweets:

        tweet_insight = copy.deepcopy(TWEET_SCHEMA)

        tweet_insight["link"] = tweet["id"]
        tweet_insight["text"] = tweet["full_text"]
        tweet_insight["retweet_count"] = tweet["retweet_count"]
        tweet_insight["favorite_count"] = tweet["favorite_count"]

        sentiment = get_sentiment(tweet["full_text"])

        sentiments.append(sentiment)
        tweet_insight["sentiment"] = sentiment

        insights["items"].append(tweet_insight)

    insights["sentiment"] = sum(sentiments)
    print(json.dumps(insights))


# with open("/opt/airflow/data/1/source/twitter.json", 'r') as file:
#
#     tweets = file.read()
#     insights = {
#         "source": "twitter",
#         "count": "",
#         "sentiment": "",
#         "keywords": [],
#         "items": []
#     }
#
#     analyze_tweets(json.loads(tweets), insights)


# get_keywords('/opt/airflow/data/2/source/news.json')