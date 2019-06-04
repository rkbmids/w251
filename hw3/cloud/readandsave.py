import numpy as np
import math
import cv2

import paho.mqtt.client as mqtt
print('imports done!')
index = 0

HOST="108.168.189.85"
PORT=1883
TOPIC="cloudfaces"

path = '/data/' #map directory to  /mnt/hw3bucket

def on_connect(clnt, user, flags, rc):
    client.subscribe(TOPIC)
    print('subscribed to topic!')
    print("connected with rc:" + str(rc))

def on_message(client, userdata, msg):
    print('message function triggered!! hallelujah')
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
client.connect(HOST, PORT, 60)
print('connected to host!')
client.on_message=on_message
print('message function set!')
client.loop_forever()
