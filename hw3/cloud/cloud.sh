##!/usr/bin/env bash

docker network create --driver bridge cloudbridge

docker build -t cloudbroker -f Dockerfile.cloudbroker .

docker build -t readandsave -f Dockerfile.readandsave .

docker run -d --name cloudbroker -p 1883:1883 --network cloudbridge cloudbroker

docker run -d --name readandsave -v /mnt/hw3bucket:/data --network cloudbridge readandsave
