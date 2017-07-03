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
      
    elif:
      if greetings in message["text"]:
        res = random.choice(greetings_responses) 
        + " I am low-level bitcoinBot.\n I can ONLY reply current bitcoin price.\n Please ask including 'bitcoin'."
      
    else: 
      res = "Sorry, I am low-level bitcoinBot.\n Please ask including 'bitcoin'."
    return res
