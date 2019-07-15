import numpy as np
import math
import cv2
import json
import sqlite3

import paho.mqtt.client as mqtt
print('imports done!')
index = 0

HOST="169.61.86.153"
PORT=1883
TOPIC = 'posture'

path = '/data/images/' #path to folder mounted
DB_FILE = '/data/posture.db'

#Connect to SQLite
try:
    c = sqlite3.connect(DB_FILE)
    print('\nConnected to %s using SQLite Version %s...\n'%(db_file,
        sqlite3.version))
except sqlite3.Error as e:
    print("Connection to %s failed:"%db_file)
    print(e)
    quit()

def on_connect(clnt, user, flags, rc):
    client.subscribe(TOPIC_IMAGE)
    print('subscribed to topic!')
    print("connected with rc:" + str(rc))

def on_message(client, userdata, msg):
    print('message function triggered!! hallelujah')
    global index
    global path
    #save images
    f = np.frombuffer(msg.payload.image, dtype='uint8')
    img = cv2.imdecode(f, flags=1)
    print('message received!', img.shape)
    name = 'image_%s.png'%str(index)
    cv2.imwrite(path+name, img)
    print('image saved')
    #write data
    global c
    data = msg.payload.data
    sql = "INSERT INTO posture_summary (image_id, user, datetime, classification)"
    sql += " VALUES (%d, %s, %s, %s);"%(index, data.user, data.datetime, data.classification)
    c.execute(sql)
    print('classification populated')
    data = msg.payload.data
    sql = "INSERT INTO posture_detail (image_id, features)"
    sql += " VALUES (%d, %s)"%(index, features)
    #c.execute(sql) #uncomment this when schema populated
    index+=1

client = mqtt.Client()
print('initialized client!')
client.on_connect = on_connect
client.connect(HOST, PORT, 60)
print('connected to host!')
client.on_message=on_message
print('message function set!')
client.loop_forever()
