import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm
from urllib.request import urlopen

IMG_SIZE = 50

def load_data(message):
  url = message["attachments"][0]["contentUrl"]
  data = url_to_img(url)
  img = cv2.resize(data, (IMG_SIZE, IMG_SIZE))
  return img

def url_to_img(url):
  resp = urlopen(url)
  img = np.asarray(bytearray(resp.read()), dtype="uint8")
  img = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
  return img
