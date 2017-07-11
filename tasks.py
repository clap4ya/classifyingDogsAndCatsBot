from microsoftbotframework import ReplyToActivity
from urllib.request import urlopen
import numpy as np
import cv2 
import tensorflow as tf
#from tflearn.layers.conv import conv_2d, max_pool_2d
#from tflearn.layers.core import input_data, dropout, fully_connected
#from tflearn.layers.estimator import regression

IMG_SIZE = 50

def response(message):
  if message["attachments"][0]["contentType"] == "image/jpeg":
    ReplyToActivity(fill=message, text=classify(message)).send()
                            
def classify(message):
  url = message["attachments"][0]["contentUrl"]
  data = url2img(url)
  img_data = data[0]
  data = img_data.reshape(IMG_SIZE,IMG_SIZE,1)
  #load_model()
  #model_out = model.predict([data])[0]
  #if np.argmax(model_out) == 1: str_label='Dog'
  #else: str_label='Cat'
  #print(str_label)
  return "suc"

def url2img(url):
  resp = urlopen(url)
  img = np.asarray(bytearray(resp.read()), dtype="uint8")
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
  img = np.array(img)
  return img

#def load_model():
  #tf.reset_default_graph()

  #convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')

  #convnet = conv_2d(convnet, 32, 5, activation='relu')
  #convnet = max_pool_2d(convnet, 5)

  #convnet = conv_2d(convnet, 64, 5, activation='relu')
  #convnet = max_pool_2d(convnet, 5)

  #convnet = conv_2d(convnet, 128, 5, activation='relu')
  #convnet = max_pool_2d(convnet, 5)

  #convnet = conv_2d(convnet, 64, 5, activation='relu')
  #convnet = max_pool_2d(convnet, 5)

  #convnet = conv_2d(convnet, 32, 5, activation='relu')
  #convnet = max_pool_2d(convnet, 5)

  #convnet = fully_connected(convnet, 1024, activation='relu')
  #convnet = dropout(convnet, 0.8)

  #convnet = fully_connected(convnet, 2, activation='softmax')
  #convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

  #model = tflearn.DNN(convnet, tensorboard_dir='log')

  #MODEL_NAME = 'dogsvscats-0.001-2conv-basic.model.meta'
  #if os.path.exists(MODEL_NAME):
  #  model.load(MODEL_NAME)
    #print('model loaded!')
