Twitter Market Reporter
Purpose

This project automatically generates a daily market expectation report for a specific stock using Twitter data.

The system:

Collects stock-related tweets and stores them in MongoDB

Identifies and ranks high-impact tweets

Generates a concise daily market summary using an LLM

Sends the report automatically via email

This project does not predict stock prices.
It summarizes public market expectations and key discussion themes based on Twitter activity.

Tech Stack

Python

MongoDB

Twitter API

LLM for text generation

Email (SMTP)

How It Runs

Tweet data is collected and stored continuously

A daily job processes the last 24 hours of data

A summary report is generated and emailed to the client