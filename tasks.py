from microsoftbotframework import ReplyToActivity
import cv2
import numpy 
from urllib.request import urlopen

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
                            
def classify(message):
  url = message["attachments"][0]["contentUrl"]
  res = url2img(url)
  return url

def url2img(url):
  resp = urlopen(url)
  img = np.asarray(bytearray(resp.read()), dtype="uint8")
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
  return img
