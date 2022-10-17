#!/bin/bash

# Docker network creation, if it does not exist
docker network ls| grep mynetwork > /dev/null || docker network create mynetwork

cd $(dirname "$0")

# Web server
docker run \
    --rm \
    --name server \
    --net mynetwork \
    -p 8000:8000 \
    -w /html \
    -v `pwd`:/html:ro \
    python:slim \
    python -m http.server

cd -