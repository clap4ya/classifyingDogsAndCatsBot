from microsoftbotframework import ReplyToActivity
from urllib.request import urlopen
import numpy as np
import cv2
import os
import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

#image size
IMG_SIZE = 50
#learning rate(0.001)
LR = 1e-3

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
                            
def classify(message):
  url = message["attachments"][0]["contentUrl"]
  #url to image
  data = url2img(url)
  #reshape
  data = data.reshape(IMG_SIZE,IMG_SIZE,1)
  #load model
  model = load_model()
  #predict
  model_out = model.predict([data])
  #classify dog and cat by prediction
  if np.argmax(model_out) == 1: str_label='Dog'
  else: str_label='Cat'
  return str_label

#url to image
def url2img(url):
  resp = urlopen(url)
  img = np.asarray(bytearray(resp.read()), dtype="uint8")
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
  img = np.array(img)
  return img

#load trained cnn model
def load_model():
  tf.reset_default_graph()

  convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')

  convnet = conv_2d(convnet, 32, 5, activation='relu')
  convnet = max_pool_2d(convnet, 5)

  convnet = conv_2d(convnet, 64, 5, activation='relu')
  convnet = max_pool_2d(convnet, 5)

  convnet = conv_2d(convnet, 128, 5, activation='relu')
  convnet = max_pool_2d(convnet, 5)

  convnet = conv_2d(convnet, 64, 5, activation='relu')
  convnet = max_pool_2d(convnet, 5)
    
  convnet = conv_2d(convnet, 32, 5, activation='relu')
  convnet = max_pool_2d(convnet, 5)

  convnet = fully_connected(convnet, 1024, activation='relu')
  convnet = dropout(convnet, 0.8)

  convnet = fully_connected(convnet, 2, activation='softmax')
  convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

  model = tflearn.DNN(convnet, tensorboard_dir='log')

  MODEL_NAME = "dogsvscats-{}-{}.model".format(LR, "2conv-basic")
  
  if os.path.exists(MODEL_NAME):
    model.load(MODEL_NAME)
    
  return model  
