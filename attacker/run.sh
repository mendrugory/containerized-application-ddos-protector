#!/bin/bash

docker run --net mynetwork --rm busybox /bin/sh -c "while true; do /bin/wget -qO- http://server:8000; /bin/sleep 1; done"
