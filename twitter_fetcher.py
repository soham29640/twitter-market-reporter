import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True
)

query = (
    "TSLA OR Tesla lang:en "
    "-is:retweet "
    "-giveaway -free -crypto -airdrop -follow -dm"
)


response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["created_at", "public_metrics"]
)

tweets = []
if response.data:
    for tweet in response.data:
        tweets.append({
            "text": tweet.text,
            "likes": tweet.public_metrics["like_count"],
            "retweets": tweet.public_metrics["retweet_count"],
            "created_at": tweet.created_at
        })

print("Tweets fetched:", len(tweets))
print(tweets[:2])
