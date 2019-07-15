#!/usr/bin/env bash
#build containers
docker build -t cloudbroker -f Dockerfile.cloudbroker .
docker build -t readandsave -f Dockerfile.readandsave .

#run containers
#will make posturedata dir to hold .db file and images. will map image folder to
#storage bucket.
docker run -d --name cloudbroker -p 1883:1883 cloudbroker
docker run -d --name readandsave -v /posturedata:/data
