import tweepy
import os
from dotenv import load_dotenv
import json

load_dotenv() # to securely load the env token

class Scrapper:
  def __init__(self): #__init__ automatically runs the function without calling 
    token = os.getenv("BEARER_TOKEN") # token to use the api
    self.client = tweepy.Client(bearer_token=token) # using tweepy's client to login using token

  def user_tweets(self,username,count):
    try:
      user = self.client.get_user(username=username) # gets the user_id
      tweets = self.client.get_users_tweets(id=user.data.id, max_results=count, tweet_fields=["created_at"]) # fetches tweets as object
      
      if tweets.data: 
        export_choice = input("Do you want JSON of your scrapped tweets?(Yes/No) ").lower().strip()
        
        if export_choice == 'yes':
          tweet_list = []
          for tweet in tweets.data:
            tweet_list.append({
              'tweet':tweet.text,
              'username':f'@{username}',
              'created_at':str(tweet.created_at) # Saves Data in a list
            })
          
          with open(f"scrapped-data/{username}-tweets.json","w",encoding="utf-8") as f: # Saves data as JSON 
            json.dump(tweet_list,f,indent=4)
          print(f" Saved to a JSON file")
        
        
        elif export_choice == 'no':
          for tweet in tweets.data:
            print(f"{tweet.text} from @{username} created at {str(tweet.created_at)}") # Prints data
         
        else:
          print("Invalid Choice")
          
      else:
        print("Couldn't fetch tweets or Account Private ")
    
    
    except tweepy.TooManyRequests:
      print('Too many Requests try after a while') # Handles Exceptions
    
    
    except tweepy.BadRequest:
      print("Bad request invalid or private account")
    
    
    except Exception as e:
      print("Unexpected Error",e)
      

scarp = Scrapper() # self is scrap variable

username = (input("Enter Username to Scarp Data From ")) # lower to keep it simplified
count = int(input("How many tweets to scrap? ")) 

scarp.user_tweets(username,count) #Running the Function



