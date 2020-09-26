#!/bin/bash

build_postgres=false
build_redis=false

#######################################################
## IMPORTANT: set environment variables before running
#######################################################

# create directories
mkdir -p /root/dumps
mkdir -p /root/cache

# build latest image of postgres
if [ "$build_postgres" = true ] ; then
    cd ../../database
    docker build -t pastebin-postgres:latest .
    cd ../deploy/master
fi

# build latest image of redis
if [ "$build_redis" = true ] ; then
    cd ../../cache
    docker build -t pastebin-redis:latest .
    cd ../deploy/master
fi

# build latest image of api
cd ../../pastebin-api
docker build -t pastebin-api:latest .
cd ../deploy/master

# bring down images
docker-compose -f docker-compose.yml down

# detached mode (so command will finish)
docker-compose -f docker-compose.yml up -d

# deploy services
cd ../../pastebin-api/

# backup_redis
cp services/backup_redis/backup_redis.service /lib/systemd/system/
cp /lib/systemd/system/backup_redis.service /etc/systemd/backup_redis.service
chmod 644 /lib/systemd/system/backup_redis.service
systemctl enable backup_redis
systemctl start backup_redis
