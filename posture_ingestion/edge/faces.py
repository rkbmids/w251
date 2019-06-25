import numpy as np
import cv2

import paho.mqtt.client as mqtt
import argparse
#docker exec -it facedetect /bin/bash
parser = argparse.ArgumentParser()
parser.add_argument('label', choices=['straight', 'slouch'])
args = parser.parse_args()
label = args.label

TOPIC = label
HOST="broker"
PORT=1883

def on_connect(clnt, user, flags, rc):
    print("connected with rc:" + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(HOST, PORT)
capture = cv2.VideoCapture(1)

while(True):
    ret, frame = capture.read()
    for image in [frame, cv2.flip(frame, 1)]:
        #twice as many images per frame w vertical flip
        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        rc,jpg = cv2.imencode('.png', image_np)

        msg = jpg.tobytes()
        client.publish(TOPIC, payload=msg, qos=1, retain=False)
        print("Published Message!")
