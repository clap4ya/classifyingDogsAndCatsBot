from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime

def response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=reply()).send()

def reply():
    url = 'https://api.korbit.co.kr/v1/ticker'
    params = {
        'format': json
    }

    response = requests.get(url, params=params)
    data = response.json()

    price = data['last']
    current = datetime.datetime.now()
    
    res = current + " price: " + price + "won!"
    print(res)
    return res
