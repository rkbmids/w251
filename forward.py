import paho.mqtt.client as mqtt

HOST = "mosquitto"
PORT = 1883
TOPIC = "facedetect"

REMOTE_HOST = 169.53.7.212
REMOTE_PORT = 1883
REMOTE_TOPIC = "cloudfaces"

def on_connect_local(client, userdata, flags, rc):
    print('connected locally with rc: ', str(rc))
    client.subscribe(TOPIC)

def on_connect_remote(client, userdata, flags, rc):
    print('connected remotely with rc: ', str(rc))

def on_message(client, userdata, msg):
    client.publish(REMOTE_TOPIC, payload=msg.payload, qos=0, retain=False)

local_client = mqtt.Client()
local_client.on_connect = on_connect_local
local_client.conect(HOST, PORT, 60)
local_client.on_message = on_message

remote_client = mqtt.Client()
remote_client.on_connect = on_connect_remote
remote_client.connect(REMOTE_HOST, REMOTE_PORT, 60)

local_client.loop_forever()

