"""
Twitter ETL
This ETL process extracts data from the Twitter API,
transforms it into a format suitable for analysis, and loads it into a s3 bucket.

"""

import configparser

import pandas as pd
import s3fs
import tweepy


def twitter_etl():
    """twitter ETL"""
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read("config.ini")
    access_key = config["api"]["access_key"]
    access_secret = config["api"]["access_secret"]
    access_token = config["api"]["access_token"]
    access_token_secret = config["api"]["access_token_secret"]

    # twitter authentication
    auth = tweepy.OAuth1UserHandler(access_key, access_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create twitter api
    api = tweepy.API(auth)
    tweets = api.user_timeline(
        screen_name="@elonmusk", count=20, include_rts=False, tweet_mode="extended"
    )

    df_columns = ["user", "text", "favorite_count", "retweet_count", "created_at"]
    tweets_df = pd.DataFrame(columns=df_columns)

    for tweet in tweets:
        refined_tweet = [
            tweet.user.screen_name,
            tweet._json["full_text"],
            tweet.favorite_count,
            tweet.retweet_count,
            tweet.created_at,
        ]
        tweets_df = pd.concat(
            [tweets_df, pd.DataFrame([refined_tweet], columns=df_columns)],
            ignore_index=True,
        )
    tweets_df.to_csv("s3://twitter-airflow-etl/tweets1212.csv", index=False)
