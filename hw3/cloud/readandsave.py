import numpy as np
import math
import cv2

import paho.mqtt.client as mqtt

index = 0

HOST="cloudbroker"
PORT=1883
TOPIC="cloudfaces"

path = 'data/' #folder inside docker container that maps to folder on host that
    #is mapped to cloud storage

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
client.on_connect = on_connect
client.connect(HOST, PORT)
client.on_message=on_message
client.loop_forever()
