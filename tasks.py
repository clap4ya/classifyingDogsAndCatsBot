from microsoftbotframework import ReplyToActivity
import requests
import json

def echo_response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=replyBitcoin()).send()

def replyBitcoin():
    url = 'https://api.korbit.co.kr/v1/ticker'
    params = {
        'format': json
    }

    response = requests.get(url, params=params)
    data = response.json()

    price = data['last']
    res = "price: " + price
    print(res)
    return res
