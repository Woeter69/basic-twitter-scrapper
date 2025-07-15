import tweepy
import os
from dotenv import load_dotenv
import requests

load_dotenv() # to securely load the env token

class Scrapper:
  def __init__(self): #__init__ automatically runs the function without calling 
    token = os.getenv("BEARER_TOKEN") # tokon to use the api
    self.client = tweepy.Client(bearer_token=token) # using tweepy's client to login using token

  def user_tweets(self,username,count):
    user = self.client.get_user(username=username) # gets the user_id
    tweets = self.client.get_users_tweets(id=user.data.id, max_results=count) # fetches tweets as object
    for tweet in tweets.data():
      print(tweet.text)

scarp = Scrapper() # self is scrap variable

username = (input("Enter Username to Scarp Data From")).lower() # lower to keep it simplified
count = int(input("How many tweets to scrap?")) 


'''                       MUST READ TO UNDERSTAND THE CODE
______________________________________________________________________________________

This is OOP (Object Oriented Programming) class defined a mold or we can say blueprint
to define objects in python (when I use vairable scrap it becomes a object in order to
the Scrapper class).

The __init__ intitalzes the code inside its functions automatically without calling as
soon as I run the program.

The self is the object currently in use. In our cases the scrap object is currently in
use so the command are acutally scrap.client.

Self/Object Functions are always called as <object>.<function>()

I'm adding temp.py for practice and some examples

'''

