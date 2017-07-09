from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime
import random
import numpy as np
from urllib.request import urlopen
import cv2

greetings = [ "hi", "hello", "hey", "yo", "greetings" ]
greetings_responses = [ "Hi there." , "Greetings man.", "Hello there.", "Hey." ]

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
  else:
    ReplyToActivity(fill=message, text="I am low-level classifyingBot. Please send a image.").send()
                            
def classify(message):
  url = message["attachments"][0]["contentUrl"]
  IMG_SIZE = 50
  data = url_to_img(url)
  #img = cv2.resize(data, (IMG_SIZE, IMG_SIZE))
  #res = img
  return data

def url_to_img(url):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
 
    return image
