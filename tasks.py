from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime
import random

greetings = [ "hi", "hello", "hey", "yo", "greetings" ]
greetings_responses = [ "Hi there." , "Greetings man.", "Hello there.", "Hey." ]

def response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message, text=reply(message)).send()  
  else:
    ReplyToActivity(fill=message, text=type(message).send()  
        
def reply(message):
    if 'bitcoin' in message["text"]:
      url = 'https://api.korbit.co.kr/v1/ticker'
      params = {
          'format': json
      }

      response = requests.get(url, params=params)
      data = response.json()

      price = data['last']
      utcnow = datetime.datetime.utcnow()
      time_gap = datetime.timedelta(hours=9)
      current = str(utcnow + time_gap)

      res = current + " price: " + price
      #print(res)
      
    elif message["text"] in greetings:
      res = random.choice(greetings_responses) + " I am low-level classifyingBot.\nI can ONLY classify dogs and cats.\nPlease sned a image"
      
    else: 
      res = "Sorry, I am low-level classifyingBot.\n Please send a image."
      
    return res
