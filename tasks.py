from microsoftbotframework import ReplyToActivity
from urllib.request import urlopen
import numpy as np
import cv2 

IMG_SIZE = 50

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
                            
def classify(message):
  url = message["attachments"][0]["contentUrl"]
  data = url2img(url)
  img_data = data[0]
  #data = img_data.reshape(IMG_SIZE,IMG_SIZE,1)
  return url

def url2img(url):
    resp = urlopen(url)
    img = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
    img = np.array(img)
    return img
