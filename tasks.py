from microsoftbotframework import ReplyToActivity
import requests
import json

def echo_response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=111111111111111111111).send()
