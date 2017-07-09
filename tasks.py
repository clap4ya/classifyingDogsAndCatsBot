from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime
import random
#from dataLoader import *

greetings = [ "hi", "hello", "hey", "yo", "greetings" ]
greetings_responses = [ "Hi there." , "Greetings man.", "Hello there.", "Hey." ]

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
                            
def classify(message):
  #data = load_data(message)
  return "11111111111111"
