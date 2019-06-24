##!/usr/bin/env bash

docker network create --driver bridge cloudbridge

docker build -t cloudbroker -f Dockerfile.cloudbroker .

docker build -t readandsave_slouch -f Dockerfile.readandsave_slouch .
docker build -t readandsave_straight -f Dockerfile.readandsave_straight .
docker run -d --name cloudbroker -p 1883:1883 --network cloudbridge cloudbroker

docker run -d --name readandsave_slouch -v /mnt/hw3bucket:/data --network cloudbridge readandsave
docker run -d --name readandsave_straight -v /mnt/hw3bucket:/data --network cloudbridge readandsave
