# 🐦 Twitter Scraper CLI (Tweepy + JSON Export)

A simple Python CLI tool that uses the Twitter API v2 to scrape a user's tweets and optionally export them as a JSON file.

## ⚙️ Features

- 🔐 Uses a `.env` file to store your **Bearer Token**
- ✅ Scrapes latest tweets from any **public Twitter account**
- 📁 Exports tweets (with timestamp) to a `.json` file in `scrapped-data/`
- 🛡 Handles rate limits, invalid usernames, and private accounts
- 🎯 Simple CLI interface

---

## 🖥 Preview

- Enter Twitter username to scrape: elonmusk
- How many tweets to scrape (max 100)? 5
- Do you want JSON of your scraped tweets? (Yes/No) yes
- ✅ Saved to scrapped-data/elonmusk-tweets.json


---

## 📦 Requirements

- Python 3.7+
- Twitter Developer account (for Bearer Token)

Install dependencies:

```bash
pip install tweepy python-dotenv
