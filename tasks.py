from microsoftbotframework import ReplyToActivity
from urllib.request import urlopen
import numpy as np
import cv2 


def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
                            
def classify(message):
  url = message["attachments"][0]["contentUrl"]
  res = url2img(url)
  return "111111111111111111111"

def url2img(url):
  resp = urlopen(url)
  img = np.asarray(bytearray(resp.read()), dtype="uint8")
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
  return img
