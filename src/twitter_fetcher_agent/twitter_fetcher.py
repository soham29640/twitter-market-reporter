# src/twitter_fetcher_agent/twitter_fetcher.py

import os
import tweepy
from datetime import datetime
from dotenv import load_dotenv

from mongodb import insert_tweet

load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# change this stock anytime
STOCK_QUERY = "(TSLA OR Tesla OR $TSLA) -is:retweet lang:en"


def get_twitter_client():
    return tweepy.Client(
        bearer_token=BEARER_TOKEN,
        wait_on_rate_limit=True
    )


def fetch_and_store_tweets(max_results=50):
    client = get_twitter_client()

    response = client.search_recent_tweets(
        query=STOCK_QUERY,
        tweet_fields=["created_at", "public_metrics", "author_id"],
        max_results=max_results
    )

    if not response.data:
        print("No tweets found")
        return

    for tweet in response.data:
        metrics = tweet.public_metrics

        tweet_doc = {
            "_id": tweet.id,
            "text": tweet.text,
            "created_at_ts": tweet.created_at.timestamp(),
            "likes": metrics.get("like_count", 0),
            "retweets": metrics.get("retweet_count", 0),
            "followers": 0,  # filled later if needed
        }

        insert_tweet(tweet_doc)

    print(f"Inserted {len(response.data)} tweets")


if __name__ == "__main__":
    fetch_and_store_tweets()
