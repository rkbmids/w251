##!/usr/bin/env bash

docker network create --driver bridge cloudbridge

docker build -t cloudbroker -f Dockerfile.cloudbroker .

docker build -t readandsave -f Dockerfile.readandsave .

docker run -d --name cloudbroker --network cloudbridge cloudbroker

docker run -d --name readandsave --network cloudbridge readandsave
