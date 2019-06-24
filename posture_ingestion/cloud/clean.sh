##!/usr/bin/env bash

docker kill cloudbroker
docker kill readandsave_slouch
docker kill readandsave_straight

docker rm cloudbroker
docker rm readandsave_slouch
docker rm readandsave_straight
