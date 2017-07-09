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
  res = "I am low-level classifyingBot. Please send a image."
    
  if message["attachments"][0]["contentType"] == "image/jpeg":
    data = message["attachments"][0]["contentUrl"]
  
  return res
