#!/bin/bash

#######################################################
## IMPORTANT: set environment variables before running
#######################################################

# create directories
mkdir -f /root/cache

# build latest image of api
cd ../../pastebin-api
docker build -t pastebin-api:latest .
cd ../deploy/master

# bring down images
docker-compose -f docker-compose.yml down

# detached mode (so command will finish)
docker-compose -f docker-compose.yml up -d
