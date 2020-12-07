import tweepy as tw
import copy

consumer_key= 'SNyLfnh03XCeQL5YpM5iFaNoK'
consumer_secret= 'wehbp8P4qvpyNwb4JEUmwUXDHVRVD0WlSGXIocAz9E8IUxujkU'
access_token= '313361299-frikc8w0sFQTGNebsy4n6f9H6fN9Tt9pdj4kO4I7'
access_token_secret= 'OTfiF1gjGo9unsmiNAaAyC5S5O5QIIta9Zefh66ZQXLQM'


TWEET_SCHEMA = {
    "link":"",
    "full_text" : "",
    "retweet_count": "",
    "favorite_count": ""
}


def get_tweets(keyword, date_since):

    print("Pulling tweets for : " + keyword)

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    output = []
    tweets = None

    # Collect tweets
    try:
        tweets = tw.Cursor(api.search,
                           q=keyword+ " -filter:retweets",
                           lang="en",
                           result_type='popular',
                           tweet_mode='extended',
                           since='2020-11-01',
                           count=50).items(50)

    #

    except Exception as e:
        print(e)
        return []

    print("Collected some tweets")

    count = 0

    # Iterate and print tweets
    for tweet in tweets:
        try:
            # print(tweet.id)
            # print(tweet.retweet_count)

            parsed_tweet = copy.deepcopy(TWEET_SCHEMA)

            parsed_tweet["link"] = "https://twitter.com/twitter/statuses/" + str(tweet.id)
            parsed_tweet["full_text"] = tweet.full_text
            parsed_tweet["retweet_count"] = tweet.retweet_count
            parsed_tweet["favorite_count"] = tweet.favorite_count

            output.append(parsed_tweet)
            count += 1

        except Exception as e:
            print(e)
    print(count)
    print(output)

    return output

#
# #
# get_tweets('Supply chain','')