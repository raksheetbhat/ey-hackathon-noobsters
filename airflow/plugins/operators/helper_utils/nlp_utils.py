# from summarizer import Summarizer
# import json

import copy


# def get_summary(text):
#
#     model = Summarizer()
#     summary = ""
#
#     try:
#         summary = model(text, min_length=20, max_length=200)
#     except Exception as e:
#         print(e)
#
#     return summary


import spacy
from collections import Counter
from string import punctuation

nlp = spacy.load("en_core_web_md")


def get_keywords(text, stop_words):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN']  # 1

    print("Stop Words : " + str(stop_words))

    doc = nlp(text.lower())  # 2
    for token in doc:
        # 3
        if token.text in nlp.Defaults.stop_words or token.text in punctuation or token.text in stop_words:
            continue
        # 4
        if token.pos_ in pos_tag:
            result.append(token.text)

    keywords = {}

    for x in Counter(result).most_common(20):
        keywords[x[0]] = x[1]

    return keywords


from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()


def get_sentiment(text):

    pol_score = sia.polarity_scores(text)

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

NEWS_SCHEMA = {
    "title" : "",
    "link": "",
    "summary": "",
    "sentiment": "",
    "keywords": "",
    "source": ""
}

VIDEO_SCHEMA = {
    "link": "",
    "title": "",
    "views": "",
    "sentiment": "",
    "keywords": [],
    "published": "",
    "channel": "",
    "duration":"",
    "summary": ""
}

SENTIMENT_LOOKUP = {
    "0": "neutral",
    "1": "positive",
    "-1": "negative"
}

SENTIMENTS_SCHEMA = {
    "positive": 0,
    "negative": 0,
    "neutral": 0
}


def analyze_tweets(tweets, insights, stop_words):

    text = ""
    sentiments = copy.deepcopy(SENTIMENTS_SCHEMA)
    count = 0

    for tweet in tweets:

        tweet_insight = copy.deepcopy(TWEET_SCHEMA)

        tweet_insight["link"] = tweet["link"]
        tweet_insight["text"] = tweet["full_text"]
        tweet_insight["retweet_count"] = tweet["retweet_count"]
        tweet_insight["favorite_count"] = tweet["favorite_count"]

        sentiment = get_sentiment(tweet["full_text"])

        sentiments[SENTIMENT_LOOKUP[str(sentiment)]] += 1

        tweet_insight["sentiment"] = sentiment

        insights["items"].append(tweet_insight)

        text += " " + tweet["full_text"]
        count += 1

    keywords = get_keywords(text, stop_words)

    insights["sentiment"] = sentiments
    insights["keywords"] = keywords
    insights["count"] = count
    # print(keywords)
    return insights


def analyze_news(news_articles, insights, stop_words):

    text = ""
    sentiments = copy.deepcopy(SENTIMENTS_SCHEMA)
    count = 0

    for news in news_articles:

        if len(news["text"]) < 50:
            continue

        news_insight = copy.deepcopy(NEWS_SCHEMA)

        news_insight["link"] = news["link"]
        news_insight["title"] = news["title"]

        sentiment = get_sentiment(news["text"])

        sentiments[SENTIMENT_LOOKUP[str(sentiment)]] += 1

        news_insight["sentiment"] = sentiment
        news_insight["keywords"] = get_keywords(news["text"], stop_words)

        news_insight["summary"] = news["summary"]

        insights["items"].append(news_insight)

        text += " " + news["text"]
        count += 1

    keywords = get_keywords(text, stop_words)

    insights["sentiment"] = sentiments
    insights["keywords"] = keywords
    insights["count"] = count

    # print(keywords)
    return insights


def analyze_videos(videos, insights, stop_words):

    text = ""
    sentiments = copy.deepcopy(SENTIMENTS_SCHEMA)
    count = 0

    for video in videos:

        # if len(video.get("transcript", 0)) < 50:
        #     continue

        video_insight = copy.deepcopy(VIDEO_SCHEMA)

        video_insight["link"] = video["link"]
        video_insight["title"] = video["title"]
        video_insight["views"] = video["views"]
        video_insight["duration"] = video["duration"]
        video_insight["channel"] = video["channel"]
        video_insight["published"] = video["published"]

        if video.get("transcript") is not None:
            sentiment = get_sentiment(video["transcript"])

            sentiments[SENTIMENT_LOOKUP[str(sentiment)]] += 1

            video_insight["sentiment"] = sentiment
            video_insight["keywords"] = get_keywords(video["transcript"], stop_words)
            text += " " + video["transcript"]

        insights["items"].append(video_insight)

        count += 1

    keywords = get_keywords(text, stop_words)

    insights["sentiment"] = sentiments
    insights["keywords"] = keywords
    insights["count"] = count

    return insights


# with open("/opt/airflow/data/1/source/news.json", 'r') as file:
#
#     tweets = file.read()
#     insights = {
#         "source": "news",
#         "count": "",
#         "sentiment": "",
#         "keywords": [],
#         "items": []
#     }
#
#     analyze_news(json.loads(tweets), insights, ["supply","chain"])


# get_keywords('/opt/airflow/data/2/source/news.json')