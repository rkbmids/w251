##!/usr/bin/env bash

docker network create --driver bridge jetsonbridge

docker build -t broker -f Dockerfile.broker .

docker build -t forwardslouch -f Dockerfile.forwardslouch .

docker build -t forwardstraight -f Dockerfile.forwardstraight .

docker build -t facedetect -f Dockerfile.facedetect .

docker run -d --name broker -p 1883:1883 --network jetsonbridge broker

docker run -d --name forwardslouch --network jetsonbridge forwardslouch

docker run -d --name forwardstraight --network jetsonbridge forwardstraight

docker run -d -t --name facedetect --privileged --network jetsonbridge facedetect
