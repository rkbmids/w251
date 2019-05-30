##!/usr/bin/env bash

#MQTT BROKER -  In the cloud, you should have a container with a
#mosquitto broker running inside.
# Create a bridge:
docker network create --driver bridge cloudbridge
# Create an alpine - based mosquitto broker:
#might need to use debian instead
docker run --name mosquitto_cloud --network cloudbridge -p 1883:1883 -ti alpine sh
# we are inside the container now
# install mosquitto
apk update && apk add mosquitto
# run mosquitto
/usr/sbin/mosquitto
# Press Control-P Control-Q to disconnect from the container

#Read images and send to cloud storage
docker run --name save_and_process --network cloudbridge -p 1883:1883 -ti debian /bin/bash
#Write images to cloud storage
sudo apt install -y mosquitto-clients
ping mosquitto
# this should work - note that we are referring to the mosquitto container by name
now=$(date +"%m_%d_%Y")
mosquitto_sub -h mosquitto_cloud -t images >> /mnt/hw3_bucket/$now
# the above should block until some messages arrive
# Press Control-P Control-Q to disconnect from the container
