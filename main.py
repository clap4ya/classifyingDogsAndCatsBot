__metaclass__ = type

from microsoftbotframework import MsBot
from tasks import *

import requests
import json

url = 'https://api.korbit.co.kr/v1/ticker'

response = requests.get(url, params=params)
data = response.json()

def makeReply(data):
    price = data['last']
    return price


bot.add_process(makeReply(data))
bot.run()
