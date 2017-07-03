from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime

def response(message):
  if message["type"] == "message":
    if 'bitcoin' in message["text"]:
      ReplyToActivity(fill=message,
                    text=currentBitcoin()).send()  
    else:
      ReplyToActivity(fill=message,
                    text=pardon()).send()  
    
def pardon():    
    ReplyToActivity(fill=message,
                    text="Sorry, I am bitcoinBot.\n" + currentBitcoin()).send()
    
def currentBitcoin():
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
    return res
