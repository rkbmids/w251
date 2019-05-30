import numpy as np
import math
import cv2

import paho.mqtt.client as mqtt
print('imports done!')
index = 0

HOST="cloudbroker"
PORT=1883
TOPIC="facedetect"

path = 'data/' #map directory to  /mnt/hw3bucket

def on_connect(clnt, user, flags, rc):
    print("connected with rc:" + str(rc))

def on_message():
    global index
    global path
    f = np.frombuffer(msg.payload, dtype='uint8')
    img = cv2.imdecode(f, flags=1)
    print('message received!', img.shape)
    name = 'face_%s.png'%str(index)
    index+=1
    cv2.imwrite(path+name, img)

client = mqtt.Client()
print('initialized client!')
client.on_connect = on_connect
client.connect(HOST, PORT)
print('connected to host!')
client.subscribe(TOPIC, 1)
print('subscribed to topic!')
client.on_message=on_message
client.loop_forever()

