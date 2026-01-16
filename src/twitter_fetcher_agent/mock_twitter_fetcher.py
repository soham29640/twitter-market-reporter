# src/twitter_fetcher_agent/mock_twitter_fetcher.py

import random
import time
from datetime import datetime

from mongodb import insert_tweet

STOCK_TWEETS = [
    "Tesla deliveries beat market expectations this quarter",
    "Concerns over Tesla margins due to rising raw material costs",
    "Analysts upgrade TSLA citing strong EV demand",
    "Regulatory pressure could impact Tesla's short term growth",
    "Tesla stock sees strong buying interest from institutions",
    "Bearish outlook as competition in EV market intensifies",
    "Tesla announces expansion of new gigafactory",
    "Profit booking expected after recent Tesla rally",
    "Long term outlook for Tesla remains strong",
    "Short sellers increase positions amid valuation concerns"
]


def generate_mock_tweet():
    tweet_id = str(int(time.time() * 1000)) + str(random.randint(100, 999))

    return {
        "_id": tweet_id,
        "text": random.choice(STOCK_TWEETS),
        "created_at_ts": datetime.utcnow().timestamp(),
        "likes": random.randint(0, 500),
        "retweets": random.randint(0, 200),
        "followers": random.randint(100, 50000)
    }


def run_mock_fetch(count=20):
    for _ in range(count):
        tweet = generate_mock_tweet()
        insert_tweet(tweet)

    print(f"Inserted {count} mock tweets")


if __name__ == "__main__":
    run_mock_fetch()
