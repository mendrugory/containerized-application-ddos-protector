#!/usr/bin/bash

cd $(dirname "$0")

docker run \
    -it \
    --rm \
    -v `pwd`:/code \
    -v /lib/modules:/lib/modules:ro \
    -v /sys:/sys:ro \
    -v /usr/src:/usr/src:ro \
    --net container:server \
    --privileged \
    -w /code \
    mendrugory/bcc python3 ip_blocking.py $@

cd -