#! /bin/bash

podman run --net=host --privileged -v $(pwd)/.drc_sim:/root/.drc_sim drc help