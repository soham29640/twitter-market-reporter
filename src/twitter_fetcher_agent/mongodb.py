# src/twitter_fetcher_agent/mongodb.py

from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "twitter_market"
COLLECTION_NAME = "tweets"


def get_collection():
    """
    Create MongoDB connection and return tweets collection
    """
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]


def insert_tweet(tweet_data: dict):
    """
    Insert a single tweet document into MongoDB
    """
    collection = get_collection()

    # avoid duplicate tweets
    if collection.find_one({"_id": tweet_data["_id"]}):
        return

    collection.insert_one(tweet_data)


def fetch_last_24h_tweets():
    """
    Fetch tweets from last 24 hours
    """
    collection = get_collection()
    now = datetime.utcnow()
    last_24h = now.timestamp() - (24 * 60 * 60)

    tweets = collection.find({
        "created_at_ts": {"$gte": last_24h}
    })

    return list(tweets)
