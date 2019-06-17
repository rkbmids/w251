##!/usr/bin/env bash

docker network create --driver bridge jetsonbridge

docker build -t broker -f Dockerfile.broker .

docker build -t forwarder -f Dockerfile.forwarder .

docker build -t facedetect -f Dockerfile.facedetect .

docker run -d --name broker -p 1883:1883 --network jetsonbridge broker

docker run -d --name forwarder --network jetsonbridge forwarder

docker run -d --name facedetect -v /home/rachael/w251/hw7/edge/:/model_download --privileged --network jetsonbridge facedetect

