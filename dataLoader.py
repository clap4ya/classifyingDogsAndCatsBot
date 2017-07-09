import cv2
import numpy as np
from urllib.request import urlopen

IMG_SIZE = 50

def load_data(message):
  url = message["attachments"][0]["contentUrl"]
  #img = url2img(url)
  #img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
  return url

def url2img(url):
  resp = urlopen(url)
  img = np.asarray(bytearray(resp.read()), dtype="uint8")
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  return img
