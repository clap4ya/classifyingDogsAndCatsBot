from microsoftbotframework import ReplyToActivity
import requests
import json
import datetime

def response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message, text=reply(message)).send()  
        
def reply():
    if 'bitcoin' in message["text"]:
      url = 'https://api.korbit.co.kr/v1/ticker'es 
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
    else: 
      res = "Sorry, I am bitcoinBot. please ask 'bitcoin' price"
    return res
