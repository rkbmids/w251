import numpy as np
import cv2

import paho.mqtt.client as mqtt

HOST="broker"
PORT=1883
TOPIC="facedetect"

def on_connect(clnt, user, flags, rc):
    print("connected with rc:" + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(HOST, PORT)

cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(1)

while(True):
    ret, frame = capture.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = cascade.detectMultiScale(grayframe, 1.3, 5)

    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]

        print("\nFound a face!\nShape: ", face.shape, '\nType: ', face.dtype)

        rc,jpg = cv2.imencode('.png', face)

        msg = jpg.tobytes()
        client.publish(TOPIC, payload=msg, qos=0, retain=False)
        print("Published Message!")

