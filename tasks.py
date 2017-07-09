from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime
import random
from dataLoader import *

greetings = [ "hi", "hello", "hey", "yo", "greetings" ]
greetings_responses = [ "Hi there." , "Greetings man.", "Hello there.", "Hey." ]

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
  else:
    ReplyToActivity(fill=message, text="I am low-level classifyingBot. Please send a image.").send()
                            
def classify(message):
  data = load_data(message)
  return "gogogo"
