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
    #if message["contentType"] == "image/jpeg":
    res = message
    
    elif message["text"] in greetings:
      res = random.choice(greetings_responses) + " I am low-level classifyingBot.\nI can ONLY classify dogs and cats.\nPlease sned a image"
      
    #else: 
    #  res = "Sorry, I am low-level classifyingBot.\n Please send a image."
      
    return res
