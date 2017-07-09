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
  if message["attachments"][0]["contentType"] == "image/jpeg":
    res = message["attachments"][0]["contentUrl"]
  else:
    res = "I am low-level classifyingBot. Please send a image."
  return res
